# Satellite Telemetry Monitoring & Anomaly Detection System

## Overview
This project is a Python-based prototype for monitoring satellite telemetry and detecting anomalous behavior in spacecraft health data.

It simulates telemetry streams for multiple satellites, identifies anomalies such as temperature spikes, battery drops, and signal loss, and generates automated reports and visualizations. The goal is to reflect a simplified satellite operations monitoring workflow.

## Features
- Synthetic telemetry generation for multiple satellites
- Detection of anomalies using:
  - threshold-based rules
  - sudden-change detection using differences
  - rolling statistical checks
- Automated anomaly reporting to CSV
- Metrics summary output to JSON
- Telemetry plots with anomaly visualization

## Example Telemetry Fields
- `timestamp`
- `satellite_id`
- `battery_level`
- `temperature`
- `signal_strength`

## Project Structure
```text
satellite-ops/
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── figures/
│   └── reports/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── simulate_data.py
│   ├── detect_anomalies.py
│   ├── metrics.py
│   └── visualize.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
From the project root:

```bash
python -m src.main
```

## Outputs
Running the pipeline generates:

- `data/processed/telemetry.csv`
- `outputs/reports/anomalies.csv`
- `outputs/reports/metrics.json`
- `outputs/figures/*.png`

## Example Use Case
This project demonstrates a lightweight telemetry monitoring workflow similar to those used in satellite operations environments, where engineers need to monitor spacecraft health, identify unexpected changes, and generate actionable reports.

## Example Visualization
![Telemetry Plot](examples/sat_001_telemetry.png)

## Example Anomaly Report

| timestamp | satellite_id | anomaly_type |
|---|---|---|
| 2026-01-01 03:05:00 | SAT-001 | battery_drop |
| 2026-01-01 04:40:00 | SAT-001 | sudden_signal_drop |
| 2026-01-01 06:15:00 | SAT-003 | temperature_spike |

## Skills Demonstrated
- Python scripting
- time-series data simulation
- anomaly detection
- data pipeline design
- automated reporting
- scientific visualization

## Future Improvements
- CLI interface with `argparse`
- configurable thresholds via YAML or JSON
- logging and alerting
- dashboard or web interface
- real telemetry ingestion instead of synthetic data