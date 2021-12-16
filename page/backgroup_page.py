from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.location_page import LocationPage


class BackgroupPage(BasePage):
    agree_btm_backgroup= (By.ID,'android:id/button1')
    def agree_backgroup(self):
        self.find_and_clik(*self.agree_btm_backgroup)  #点击背景存取位置资讯的确定按钮
        return LocationPage(self.driver)        #进入到获取设备的定位信息

