__author__ = 'Administrator'
# 查找元素的方式
class common(object):
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    SELENIUM = "selenium"
    APPIUM = "appium"
    ANDROID = "android"
    IOS = "ios"
    IE = "ie"
    FOXFIRE = "foxfire"
    CHROME = "chrome"

    CLICK = "click"
    DRIVER = ""
    TAP = "tap"
    SWIPELEFT = "swipeLeft"
    FLAG = True


    SELENIUM_APPIUM = "appium"

    RRPORT = {"info":[]}
    RESULT = {"info":[]}
    RESULT["test_module"] = "登陆模块1"
    SEND_KEYS = "send_keys"
    FIND_STR = "find_str"

    test_sum = 0
    test_success = 0
    test_failed = 0
    test_error_title = 0
    time_took = ""
    MEN = []
    CPU = []
    PACKAGE = ""
    FPS = []
    RAW = 0
   # 错误日志
    ANR = "ANR"
    I_ANR = 0
    CRASH = "CRASH"
    I_CRASH = 0
    EXCEPTION = "Exception"
    I_EXCEPTION = 0

    WAIT_TIME = 5

    #selenium
    SEND_CODE = "send_code" # 输入验证码

