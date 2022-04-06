import pytest
import time
def test_site_with_different_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")