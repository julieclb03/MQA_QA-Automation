
from .base_page import BasePage
from ..locators.selectors import SEARCH_INPUT, PRODUCT_CARD

class SearchPage(BasePage):
  def search(self, term):
    self.open("")
    box = self.browser.find_element(*SEARCH_INPUT)
    box.clear(); box.send_keys(term + "\n")
  def results(self):
    return self.browser.find_elements(*PRODUCT_CARD)
