from page.base_page import BasePage
from page.nineday_page import NineDayPage


class FindNineDayPage(BasePage):
    def find_nine_day(self,name):    #滚动查找到九天预报
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{name}").'
                                                        'instance(0));').click()
        return NineDayPage(self.driver)   #进入到九天预报页面
