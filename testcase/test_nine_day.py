import allure
import pytest

from page.app import App

@allure.feature("测试进入九天预报")
class TestNineDay:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.app.start()
    def teardown(self):
        self.app.back()
    def teardown_class(self):
        self.app.stop()
    @allure.title("首次进入到九天预报")
    @pytest.mark.parametrize("name",["九天預報"])
    def test_first_nine_day(self,name):
        #首次安装同意免责声明，同意隐私政策，背景获取位置资讯，获取定位，关闭版本日志，进入到首页,点击更多，进入到九天预报
        desc=self.app.goto_main().agree_exemption().click_agree_privacy().agree_backgroup().click_allow_use().click_off().click_more().find_nine_day(name).get_tomorrow_weather_desc()
        assert desc !=""
    @allure.title("第二次进入到九天预报")
    def test_second_nine_day(self):
        #再次打开app，仅在使用时运行且不再询问,进入到首页，点击更多图标，进入到九天预报
        desc=self.app.goto_main().click_no_ask().click_more().find_nine_day("九天預報").get_tomorrow_weather_desc()
        assert desc !=""
    @allure.title("之后进入到九天预报")
    def test_nine_day(self):
        # 再次打开app，进入到首页，点击更多图标，进入到九天预报
        desc = self.app.goto_main().click_more().find_nine_day("九天預報").get_tomorrow_weather_desc()
        assert desc != ""
        #一次拿到的明天的天气
    @allure.title("一次性拿到的明天的天气")
    def test_get_tomorrow(self):
        context=self.app.goto_main().click_more().find_nine_day("九天預報").get_tomorrow_weather()
        print(context)
        assert context !=" "
    @allure.title("分开拿到的明天的天气")
    def test_get_tomorrow_temperature(self):
        context=self.app.goto_main().click_more().find_nine_day("九天預報").get_tomorrow_weather_desc()
        print(context)
        assert context !=" "
