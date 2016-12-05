__author__ = 'shikun'
# 查找元素的方式
class GetVariable(object):
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

    SELENIUM_APPIUM = "appium"

    SEND_KEYS = "send_keys"
    FIND_STR = "find_str"
    WAIT_TIME = 5

    #selenium
    SEND_CODE = "send_code" # 输入验证码

    #本地存储记录所有的case情况的路径
    REPORT_INFO_PATH = "d:/info.txt"
    REPORT_INIT = "d:/init.txt"
    REPORT_COLLECT_PATH = "d:/collect.txt"
    CRASH_LOG_PATH = "d:/crash.txt" # 存放crash的json文件名
    #my server
    HOST = '192.168.1.38'
    PORT = 8088

    PROTOCOL = "http://" #协议
    APACHE_PATH = "D:/app/Apache2.2/htdocs/appium/log/" #apapche器的地址，开发可以在这个上面下载异常日志

    SCREEN_IMG_PATH = "D:/app/Apache2.2/htdocs/appium/img/" # 截图地址


