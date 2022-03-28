import datetime
from pathlib import Path
import os
import time

from selenium import webdriver
import pandas as pd

ENCODING = "utf-8"
START = "2022-03-01"
END = "2022-03-27"
REGION = "global"

def download_chart(year, month, day, region="global"):
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    url = f"https://spotifycharts.com/regional/{region}/daily/{year}-{month}-{day}"
    driver.implicitly_wait(5)
    driver.get(url)
    element = driver.find_element_by_css_selector("#content > div > header > div > a")
    element.click()

def download_chart_range(start, end, region="global"):
    start_datetime = datetime.datetime(int(start[:4]), int(start[5:7]), int(start[8:]))
    end_datetime = datetime.datetime(int(end[:4]), int(end[5:7]), int(end[8:]))
    
    current = start_datetime
    while True:
        if current == end_datetime:
            break
        year = current.year
        month = current.month
        day = current.day
        download_chart(year, month, day, region=region)
        current += datetime.timedelta(1)
    
def is_chart_file(filename):
    if filename.startswith("regional-") and filename.endswith(".csv"):
        return True
    return False

def combine_csv(start, end, region):
    downloads_path = str(Path.home() / "Downloads")
    files = os.listdir(downloads_path)
    files = list(filter(is_chart_file, files))
    charts = []
    for file in files:
        chart = pd.read_csv(f"{downloads_path}/{file}", header=1, encoding=ENCODING)
        chart["Date"] = "-".join(file.split("-")[3:])[:-4]
        columns = "Position#Track Name#Artist#Streams#Date#URL".split("#")
        chart = chart.loc[:, columns]
        charts.append(chart)
    charts = pd.concat(charts)
    charts.to_csv(f"spotifychart-{region}-{start}-to-{end}.csv", index=None, encoding=ENCODING)

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome('chromedriver.exe', options=options)
download_chart_range(START, END, REGION)
start_datetime = datetime.datetime(int(START[:4]), int(START[5:7]), int(START[8:]))
end_datetime = datetime.datetime(int(END[:4]), int(END[5:7]), int(END[8:]))
time.sleep(3)
time.sleep((end_datetime - start_datetime).days)
combine_csv(START, END, REGION)
