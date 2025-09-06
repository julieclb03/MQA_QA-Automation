
import os, time

class BasePage:
  def __init__(self, browser):
    self.browser = browser
    self.base_url = os.getenv("BASE_URL","https://demowebshop.tricentis.com/")
  def open(self, rel=""):
    self.browser.get(self.base_url + rel)
    time.sleep(1.5)
