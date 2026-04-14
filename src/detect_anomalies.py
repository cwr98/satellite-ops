from __future__ import annotations

import pandas as pd


TEMP_THRESHOLD = 40.0
BATTERY_THRESHOLD = 60.0
SIGNAL_THRESHOLD = 45.0
DROP_THRESHOLD = -15.0


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect anomalies using simple thresholds and sudden-change rules.
    """
    working = df.copy()
    working = working.sort_values(["satellite_id", "timestamp"]).reset_index(drop=True)

    working["battery_diff"] = working.groupby("satellite_id")["battery_level"].diff()
    working["signal_diff"] = working.groupby("satellite_id")["signal_strength"].diff()
    working["temp_diff"] = working.groupby("satellite_id")["temperature"].diff()

    anomaly_rows = []

    for _, row in working.iterrows():
        anomaly_types: list[str] = []

        if row["temperature"] > TEMP_THRESHOLD:
            anomaly_types.append("temperature_spike")

        if row["battery_level"] < BATTERY_THRESHOLD:
            anomaly_types.append("low_battery")

        if pd.notna(row["battery_diff"]) and row["battery_diff"] < DROP_THRESHOLD:
            anomaly_types.append("battery_drop")

        if row["signal_strength"] < SIGNAL_THRESHOLD:
            anomaly_types.append("signal_loss")

        if pd.notna(row["signal_diff"]) and row["signal_diff"] < DROP_THRESHOLD:
            anomaly_types.append("sudden_signal_drop")

        if anomaly_types:
            anomaly_rows.append(
                {
                    "timestamp": row["timestamp"],
                    "satellite_id": row["satellite_id"],
                    "battery_level": row["battery_level"],
                    "temperature": row["temperature"],
                    "signal_strength": row["signal_strength"],
                    "battery_diff": row["battery_diff"],
                    "signal_diff": row["signal_diff"],
                    "anomaly_type": ", ".join(anomaly_types),
                }
            )

    return pd.DataFrame(anomaly_rows)