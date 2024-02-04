from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from page import Page
class TestPage(Page):
    # 個股日收盤價及月平均價
    tradeInfo = (By.XPATH, "//*[@id='mega']/ul/li[2]/a")
    dayPrice = (By.XPATH, "//*[@id='mega']/ul/li[2]/div/div/ul[1]/li[10]/a")
    # 選 112/01
    selectDate = (By.XPATH, "//select[@id='label0']")
    # 輸入股票代碼 2330
    inputStock = (By.XPATH, "//input[@class='stock-code-autocomplete']")
    # 點選查詢按鈕
    searchBtn = (By.XPATH, "//button[@class='search']")

    # 將台積電 112 年 01 月份的每日收盤價 print 出來 //button[@class='html']
    # 截圖
    screenshot = (By.XPATH, "//*[@class='hints']")

    def click_day_price(self):
        self.find_element(self.tradeInfo).click()
        self.find_element(self.dayPrice).click()

    def select_date(self):
        select = Select(self.find_element(self.selectDate))
        select.select_by_value('2023')

    def input_stock(self):
        self.find_element(self.inputStock).send_keys('2330')

    def click_search(self):
        self.find_element(self.searchBtn).click()

    def screen_shot(self):
        charts = self.find_element(self.screenshot)
        action = ActionChains(self.driver)
        action.move_to_element(charts).perform()
        self.driver.get_screenshot_as_file("2330.png")