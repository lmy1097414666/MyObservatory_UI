from appium import webdriver

from page.base_page import BasePage



class App(BasePage):
    def start(self):
        if self.driver == None:
            caps={
                "platformName": "android",
                "deviceName": "25d55a0e",
                "appPackage": "hko.MyObservatory_v1_0",
                "appActivity": "hko.MyObservatory_v1_0.AgreementPage",
                "noReset": True
            }
            self.driver=webdriver.Remote('127.0.0.1:4723/wd/hub',caps)    #初始化driver
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(8)
        return self
    def stop(self):
        self.driver.quit()
    def goto_main(self):
        from page.main_page import MainPage
        return MainPage(self.driver)


