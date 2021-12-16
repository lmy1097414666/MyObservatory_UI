from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main_page import MainPage


class versionLogPage(BasePage):
    off_element= (By.ID,'hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip')
    def click_off(self):   #版本日志页面点击关闭按钮
        self.find_and_clik(*self.off_element)
        return MainPage(self.driver)