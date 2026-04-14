from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def plot_satellite_telemetry(
    telemetry_df: pd.DataFrame,
    anomalies_df: pd.DataFrame,
    satellite_id: str,
    output_dir: str | Path,
) -> None:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    sat_data = telemetry_df[telemetry_df["satellite_id"] == satellite_id].copy()
    sat_anomalies = anomalies_df[anomalies_df["satellite_id"] == satellite_id].copy()

    if sat_data.empty:
        return

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(sat_data["timestamp"], sat_data["temperature"], label="Temperature")
    ax.plot(sat_data["timestamp"], sat_data["battery_level"], label="Battery Level")
    ax.plot(sat_data["timestamp"], sat_data["signal_strength"], label="Signal Strength")

    if not sat_anomalies.empty:
        ax.scatter(
            sat_anomalies["timestamp"],
            sat_anomalies["temperature"],
            label="Anomalies",
            marker="x",
            s=80,
        )

    ax.set_title(f"Telemetry Overview - {satellite_id}")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)
    fig.autofmt_xdate()

    save_path = output_dir / f"{satellite_id.lower()}_telemetry.png"
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()