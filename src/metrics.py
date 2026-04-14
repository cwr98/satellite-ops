from __future__ import annotations

from pathlib import Path
import json
import pandas as pd


def generate_metrics(telemetry_df: pd.DataFrame, anomalies_df: pd.DataFrame) -> dict:
    metrics = {
        "total_telemetry_rows": int(len(telemetry_df)),
        "total_satellites": int(telemetry_df["satellite_id"].nunique()),
        "total_anomalies": int(len(anomalies_df)),
        "anomalies_per_satellite": anomalies_df["satellite_id"].value_counts().to_dict()
        if not anomalies_df.empty
        else {},
    }
    return metrics


def save_metrics(metrics: dict, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)