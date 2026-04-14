from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


def generate_telemetry(
    num_satellites: int = 5,
    num_points: int = 300,
    start_time: str = "2026-01-01 00:00:00",
    freq: str = "5min",
    seed: int = 42,
) -> pd.DataFrame:
    """
    Generate synthetic satellite telemetry with injected anomalies.
    """
    rng = np.random.default_rng(seed)
    timestamps = pd.date_range(start=start_time, periods=num_points, freq=freq)

    all_rows: list[pd.DataFrame] = []

    for sat_idx in range(1, num_satellites + 1):
        satellite_id = f"SAT-{sat_idx:03d}"

        battery_base = np.linspace(100, 78, num_points) + rng.normal(0, 0.35, num_points)
        temperature_base = 22 + 2 * np.sin(np.linspace(0, 8 * np.pi, num_points)) + rng.normal(0, 0.5, num_points)
        signal_base = 85 + rng.normal(0, 1.5, num_points)

        df_sat = pd.DataFrame(
            {
                "timestamp": timestamps,
                "satellite_id": satellite_id,
                "battery_level": battery_base,
                "temperature": temperature_base,
                "signal_strength": signal_base,
            }
        )

        # Inject anomalies
        temp_idx = rng.integers(low=30, high=num_points - 30, size=2)
        sig_idx = rng.integers(low=30, high=num_points - 30, size=2)
        batt_idx = rng.integers(low=30, high=num_points - 30, size=2)

        df_sat.loc[temp_idx, "temperature"] += rng.uniform(18, 28, size=2)
        df_sat.loc[sig_idx, "signal_strength"] -= rng.uniform(35, 50, size=2)
        df_sat.loc[batt_idx, "battery_level"] -= rng.uniform(20, 30, size=2)

        df_sat["battery_level"] = df_sat["battery_level"].clip(lower=0, upper=100)
        df_sat["signal_strength"] = df_sat["signal_strength"].clip(lower=0, upper=100)

        all_rows.append(df_sat)

    df = pd.concat(all_rows, ignore_index=True)
    df = df.sort_values(["satellite_id", "timestamp"]).reset_index(drop=True)
    return df


def save_telemetry(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)