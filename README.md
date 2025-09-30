# 🌏 qm-phivolcs

Fetch and monitor the latest earthquake data from **PHIVOLCS** (Philippine Institute of Volcanology and Seismology) using Selenium and Pandas.

---

## ⚡ Features

* Scrapes the official PHIVOLCS Earthquake site
* Parses earthquake events into a clean Pandas DataFrame
* Pretty console output with `tabulate`
* Shows current timestamp in **Asia/Manila (GMT+8)**
* Runs in **headless** mode

---

## 🛠️ Setup

### 1) Clone

```bash
git clone <your-repo-url>
cd qm-phivolcs
```

### 2) Create & activate venv

```bash
python3 -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3) Install deps

```bash
pip3 install -r requirements.txt
```

---

## ▶️ Usage

```bash
python3 main.py
```

This will:

1. Open PHIVOLCS in a headless browser
2. Wait for the quake table to load
3. Scrape, clean, and print the latest events with a PH timestamp

---

## 📊 Example Output (clean & compact)

**CLI header line**

```text
📡 Latest PHIVOLCS Quake Data (as of 2025-10-01 14:23:45 PHST +0800)
```

**Table (Markdown, 3 rows only for brevity)**

| DateTime                 | Latitude | Longitude | Depth_km | Magnitude | Location                                      |
| ------------------------ | -------: | --------: | -------: | --------: | --------------------------------------------- |
| 01 October 2025 04:13 AM |    11.50 |    124.05 |       30 |       1.5 | 027 km S 02° E of Esperanza (Masbate)         |
| 01 October 2025 04:18 AM |    13.65 |    120.53 |       84 |       3.5 | 023 km S 29° W of Calatagan (Batangas)        |
| 01 October 2025 04:12 AM |     8.80 |    126.52 |       27 |       2.1 | 025 km N 89° E of Marihatag (Surigao del Sur) |





