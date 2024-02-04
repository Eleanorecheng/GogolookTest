import pytest
from test_page import TestPage

def test_screenshot_2330(driver):
    testPage = TestPage(driver)
    testPage.click_day_price()
    testPage.select_date()
    testPage.input_stock()
    testPage.click_search()
    testPage.screen_shot()
