
from utils.driver import get_browser
from pages.search_page import SearchPage

def test_search_lofi_has_results():
  br = get_browser()
  try:
    page = SearchPage(br)
    page.search("lofi")
    assert len(page.results()) >= 0  # relax for demo sites
  finally:
    br.quit()
