
from .base_page import BasePage
from ..locators.selectors import LOGIN_LINK

class LoginPage(BasePage):
  def open_login(self):
    self.open("")
    self.browser.find_element(*LOGIN_LINK).click()
