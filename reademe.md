环境：
Appium Desktop
Python3
Appium python client
Android sdk
allure

依赖包
Appium-Python-Client
appium-UIAutomation
pytest
allure-pytest
pyyml


运行命令：pytest test_nine_day.py --alluredir=../result
收集测试结果：allure serve ../result


result
    存放报告文件
testcase
    test_fnd_uc.py  测试接口返回的状态码以及获取后台的湿度
    log.log   存放日志
conftest.py  设置log格式
pytest.ini  一些日志的配置
Page
    app.py  初始化driver,启动，关闭
    backgroup_page.py      #点击背景存取位置资讯的确定按钮
    base_page.py    #重写定位方法
    find_nine_day_page.py    #滚动查找九天预报
    location_page.py       #允许使用定位
    main_page.py      #进入到更多
    nineday_page.py   #进入到九天预报页面
    privacy_policy_page.py   #确认
    versionlog_page.py     #关闭版本日志
