from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_browser():
    opts = Options()

    # Use Chrome installed by GitHub Actions (setup-chrome) if present
    chrome_bin = (
        os.getenv("CHROME_BIN")
        or os.getenv("CHROME_PATH")
        or "/usr/bin/google-chrome"
    )
    if os.path.exists(chrome_bin):
        opts.binary_location = chrome_bin

    # Headless + CI stability flags
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")

    # If GitHub Actions provides CHROMEDRIVER_PATH, use it; otherwise use webdriver-manager
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
    if chromedriver_path and os.path.exists(chromedriver_path):
        service = Service(chromedriver_path)
    else:
        service = Service(ChromeDriverManager().install())

    return webdriver.Chrome(service=service, options=opts)
