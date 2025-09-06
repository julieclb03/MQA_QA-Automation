
from utils.driver import get_browser
from pages.login_page import LoginPage

def test_login_link_opens_login():
  br = get_browser()
  try:
    page = LoginPage(br)
    page.open_login()
    assert "login" in br.current_url.lower() or "sign" in br.current_url.lower()
  finally:
    br.quit()
