from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO
import pandas as pd
from tabulate import tabulate
from time import sleep
from datetime import datetime
from zoneinfo import ZoneInfo  # requires Python 3.9+

def fetch_phivolcs_quakes():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1400,1000")
    options.add_experimental_option("detach", False)
    options.page_load_strategy = "eager"

    service = Service()
    browser = webdriver.Chrome(service=service, options=options)

    try:
        browser.get("https://earthquake.phivolcs.dost.gov.ph")
        sleep(5)

        WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
        )

        tables = browser.find_elements(By.TAG_NAME, "table")
        target_html = None
        for tbl in tables:
            html = tbl.get_attribute("outerHTML")
            if "Mag" in html:
                target_html = html
                break

        if target_html is None and tables:
            target_html = tables[0].get_attribute("outerHTML")

        if not target_html:
            return None

        html_io = StringIO(target_html)
        df = pd.read_html(html_io, header=0)[0]

        df = df.dropna(how="all").dropna(axis=1, how="all").reset_index(drop=True)
        df.columns = ["DateTime", "Latitude", "Longitude", "Depth_km", "Magnitude", "Location"]
        for col in ["Latitude", "Longitude", "Depth_km", "Magnitude"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        return df

    finally:
        browser.quit()

def main():
    df = fetch_phivolcs_quakes()
    if df is None or df.empty:
        print("No earthquake data found.")
        return

    # get current time in PH / GMT+8
    now_ph = datetime.now(ZoneInfo("Asia/Manila"))
    timestamp_str = now_ph.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    print(f"📡 Latest PHIVOLCS Quake Data (as of {timestamp_str}):")
    print(tabulate(df.head(20), headers="keys", tablefmt="psql", showindex=False))

if __name__ == "__main__":
    main()
