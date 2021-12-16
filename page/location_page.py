from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.versionlog_page import versionLogPage


class LocationPage(BasePage):
    allow_use_element=(By.ID,'com.lbe.security.miui:id/permission_allow_foreground_only_button')
    def click_allow_use(self):
        self.find_and_clik(*self.allow_use_element)   #点击允许使用
        return versionLogPage(self.driver)
    def click_refuse(self):   #点击拒绝
        pass
    def click_this_operation(self):  #点击本次允许使用
        pass
