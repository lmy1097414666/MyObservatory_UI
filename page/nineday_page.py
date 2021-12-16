import logging

from selenium.webdriver.common.by import By

from page.base_page import BasePage

logger=logging.getLogger()
class NineDayPage(BasePage):
    description_element=(By.ID,'hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit')
    def get_nine_day_des(self):
        desc=self.find_and_return(*self.description_element)       #获取九天预报中的描述信息
        logger.info(r"九天预报中的描述信息: %s",desc)
        return desc

    tomorrow_element=(By.XPATH,'//*[@resource-id="hko.MyObservatory_v1_0:id/mainAppSevenDayView"]/*[@class="android.widget.LinearLayout" and @index="0"]')
    def get_tomorrow_weather(self):                  #获取九天预报中的全部的天气预报
        context= self.driver.find_element(*self.tomorrow_element).get_attribute("content-desc")
        logger.info(r"一次性获取到的明天的天气： %s",context)
        return context

    temperature_elements=(By.XPATH,'//*[@class="android.widget.TextView" and @index="0"]')
    humidity_elements = (By.XPATH, '//*[@class="android.widget.TextView" and @index="1"]')
    def get_tomorrow_weather_desc(self):
        tomorrow_data=self.finds_and_return(*self.temperature_elements,4)   #获取日期
        tomorrow_weekday = self.finds_and_return(*self.humidity_elements, 1)  # 获取明天周几
        tomorrow_temperature=self.finds_and_return(*self.temperature_elements,5)   #获取温度
        tomorrow_humidity=self.finds_and_return(*self.humidity_elements,2)    #获取湿度
        tomorrow_rainfall=self.finds_and_return(*self.humidity_elements,3)    #获取降雨量概率
        tomorrow_wind = self.finds_and_return(*self.temperature_elements, 6)  # 获取风速
        tomorrow_describe = self.finds_and_return(*self.temperature_elements, 7)  # 天气描述
        logger.info(r"明天的日期： %s",tomorrow_data)
        logger.info(r"明天星期几： %s",tomorrow_weekday)
        logger.info(r"明天的温度： %s",tomorrow_temperature)
        logger.info(r"明天的湿度： %s",tomorrow_humidity)
        logger.info(r"明天的降雨量： %s",tomorrow_rainfall)
        logger.info(r"明天的风速： %s",tomorrow_wind)
        logger.info(r"明天的描述： %s",tomorrow_describe)
        return tomorrow_data,tomorrow_weekday,tomorrow_temperature,tomorrow_humidity,tomorrow_rainfall,tomorrow_wind,tomorrow_describe
