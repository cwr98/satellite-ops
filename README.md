# Satellite Telemetry Monitoring & Anomaly Detection System

## Overview
This project simulates satellite telemetry data and detects anomalies in spacecraft health metrics such as temperature, battery level, and signal strength.

It represents a simplified satellite operations monitoring pipeline.

## Features
- Synthetic telemetry generation for multiple satellites
- Detection of anomalies:
  - temperature spikes
  - battery drops
  - signal loss
- Automated anomaly reporting (CSV)
- Metrics summary (JSON)
- Time-series visualization with anomaly highlighting

## Tech Stack
- Python
- NumPy
- Pandas
- Matplotlib

## Project Structure
satellite-ops/
├── src/
├── data/
├── outputs/

## Example Output
- `data/processed/telemetry.csv`
- `outputs/reports/anomalies.csv`
- `outputs/reports/metrics.json`
- `outputs/figures/*.png`

## Run
```bash
python -m src.main