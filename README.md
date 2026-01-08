# Service Incident Manager

## Overview
Service Incident Manager is a Python-based command-line application for reporting, storing, and managing service incidents. The tool allows users to record incidents, track their status (open or resolved), and calculate downtime for resolved incidents using persistent JSON storage.

This project simulates a lightweight internal operations tool commonly used in IT and service monitoring environments.

---

## Features
- Report new service incidents through an interactive CLI menu
- Automatically generate unique incident IDs
- Persist incident data across program runs using JSON files
- View:
  - All incidents
  - Open incidents
  - Resolved incidents
- Calculate downtime for resolved incidents
- Automatically creates required data files at runtime if missing

---

## Technologies Used
- Python 3
- JSON file storage
- Command-line interface (CLI)

---

## How It Works
- Incident data is stored in `incidents.json`
- Unique IDs are generated and tracked using `id.json`
- Both files are created automatically when the program runs
- Open incidents are identified by a `None` end time
- Resolved incidents include an end time, allowing downtime calculation

---

## How to Run
1. Clone the repository
2. Ensure Python 3 is installed
3. Run the program:

```bash
python incident_manager.py
