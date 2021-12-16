from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from page.base_page import BasePage
from page.privacy_policy_page import PrivacyPolicyPage


class MainPage(BasePage):
    click_element=(MobileBy.ID,"hko.MyObservatory_v1_0:id/btn_agree")
    def agree_exemption(self):   #首次打开的免责
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(self.click_element))
        self.find_and_clik(*self.click_element)    #点击免责声明的确定按钮
        return PrivacyPolicyPage(self.driver)

    more_elemment=(By.XPATH,'//android.widget.ImageButton[@content-desc="转到上一层级"]')
    def click_more(self):
        self.find_and_clik(*self.more_elemment)     #点击更多图标
        from page.find_nine_day_page import FindNineDayPage
        return FindNineDayPage(self.driver)
    click_no_ask_element=(By.ID,"com.lbe.security.miui:id/permission_keep_foreground_button")
    def click_no_ask(self):   #再次打开的不再询问
        self.find_and_clik(*self.click_no_ask_element)  #点击使用时允许且不再询问
        return self


