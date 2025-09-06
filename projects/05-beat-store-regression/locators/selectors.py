
from selenium.webdriver.common.by import By

LOGIN_LINK = (By.LINK_TEXT, "Log in")
SEARCH_INPUT = (By.NAME, "q")
PRODUCT_CARD = (By.CSS_SELECTOR, ".product, .card, .track")
ADD_TO_CART = (By.XPATH, "//button[contains(.,'Add to cart') or contains(.,'Add') or contains(.,'Buy')]")
CART_COUNT = (By.CSS_SELECTOR, ".cart-count, .mini-cart-count, [data-test='cart-count']")
