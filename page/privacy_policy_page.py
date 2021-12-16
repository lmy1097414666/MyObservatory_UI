from selenium.webdriver.common.by import By

from page.base_page import BasePage


class PrivacyPolicyPage(BasePage):
    privacy_element=(By.ID,'hko.MyObservatory_v1_0:id/btn_agree')
    def click_agree_privacy(self):
        self.find_and_clik(*self.privacy_element)    #点击隐私声明的确定按钮
        from page.backgroup_page import BackgroupPage
        return BackgroupPage(self.driver)