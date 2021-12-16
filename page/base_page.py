import logging

from appium.webdriver.webdriver import WebDriver

logger=logging.getLogger()
class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def find(self,by,value=None):
        logger.info("定位方式：find")
        logger.info(r"元素： %s",value)
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by,value)
    def find_and_clik(self,by,value=None):
        logger.info("定位方式:find_and_clik")
        return self.find(by,value).click()

    def find_and_sendkeys(self,by,value,sendkeys):
        logger.info("定位方式：find_and_sendkeys")
        logger.info(r"输入内容： %s",sendkeys)
        return self.find(by,value).send_keys(sendkeys)
    def find_and_return(self,by,value=None):
        logger.info("定位方式：find_and_return")
        logger.info(r"返回的数据: %s")
        return self.find(by,value).get_attribute('text')

    def finds(self, by, value=None):
        logger.info("定位方式：finds")
        logger.info(r"元素： %s", value)
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, value)
    def finds_and_return(self,by,value,location):
        logger.info("定位方式：finds_and_return")
        logger.info(r"返回的数据: %s")
        elments=self.finds(by,value)
        # for ele in range(len(elments)):
        #     print(elments[ele].get_attribute('text'))
        return elments[location].get_attribute('text')


    def back(self,num=3):
        logger.info("back")
        for i in range(0,num):
            self.driver.back()