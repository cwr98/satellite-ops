from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.simulate_data import generate_telemetry, save_telemetry
from src.detect_anomalies import detect_anomalies
from src.metrics import generate_metrics, save_metrics
from src.visualize import plot_satellite_telemetry


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "telemetry.csv"
ANOMALY_REPORT_PATH = PROJECT_ROOT / "outputs" / "reports" / "anomalies.csv"
METRICS_PATH = PROJECT_ROOT / "outputs" / "reports" / "metrics.json"
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"


def main() -> None:
    telemetry_df = generate_telemetry(num_satellites=5, num_points=300)
    save_telemetry(telemetry_df, DATA_PATH)

    anomalies_df = detect_anomalies(telemetry_df)
    ANOMALY_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    anomalies_df.to_csv(ANOMALY_REPORT_PATH, index=False)

    metrics = generate_metrics(telemetry_df, anomalies_df)
    save_metrics(metrics, METRICS_PATH)

    for satellite_id in telemetry_df["satellite_id"].unique():
        plot_satellite_telemetry(
            telemetry_df=telemetry_df,
            anomalies_df=anomalies_df,
            satellite_id=satellite_id,
            output_dir=FIGURES_DIR,
        )

    print("Telemetry saved to:", DATA_PATH)
    print("Anomaly report saved to:", ANOMALY_REPORT_PATH)
    print("Metrics saved to:", METRICS_PATH)
    print("Plots saved to:", FIGURES_DIR)
    print("Done.")


if __name__ == "__main__":
    main()