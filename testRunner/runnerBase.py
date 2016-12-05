__author__ = 'shikun'
# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from common.variable import GetVariable as common
import os
from selenium import webdriver as web
from seleniumrequests import Chrome
from testBLL import  apkBase


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_testcase(l_devices):
    apk_base = apkBase.apkInfo(PATH("../img/monkneyTest.apk"))
    desired_caps = {}
    desired_caps['platformName'] = l_devices["platformName"]
    desired_caps['platformVersion'] = l_devices["platformVersion"]
    desired_caps['deviceName'] = l_devices["deviceName"]
    desired_caps['appPackage'] = apk_base.get_apk_pkg()
    desired_caps['appActivity'] = apk_base.get_apk_activity()
    desired_caps['udid'] = l_devices["deviceName"]
    # desired_caps['app'] = PATH( '../img/t.apk')
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    common.PACKAGE = apk_base.get_apk_pkg()
    remote = "http://127.0.0.1:" + str(l_devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    # common.DRIVER = driver
    # common.FLAG = False
    return driver
def selenium_testcase(get_devices):
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = web.Chrome(chromedriver)
    # driver = web.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
    common.DRIVER = driver
    common.FLAG = False
    driver.maximize_window()  #将浏览器最大化
    driver.get(get_devices.open_url)
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest', l_devices=None):
        super(TestInterfaceCase, self).__init__(methodName)
        self.l_devices = l_devices
        # self.driver = ""

    @staticmethod
    def setUpClass():
        # global driver
        # ga = get_evices()
        # common.SELENIUM_APPIUM = ga.selenium_appium
        # if common.SELENIUM_APPIUM == common.APPIUM: # appium入口
        #     if ga.platformName == common.ANDROID and common.FLAG:
        #         appium_testcase(ga)
        # if common.SELENIUM_APPIUM == common.SELENIUM and common.FLAG: # selenium入口
        #     selenium_testcase(ga)
        #     # driver.get("http://www.baidu.com")
        #     # data = driver.title
            pass
    def setUp(self):
        if self.l_devices["platformName"] == common.ANDROID:
            self.driver = appium_testcase(self.l_devices)
    def tearDown(self):
        # self.driver.close_app()
        # self.driver.quit()
        pass
    @staticmethod
    def tearDownClass():
        # driver.close_app()
        # driver.quit()
        print('tearDownClass')
    @staticmethod
    def parametrize(testcase_klass, l_devices=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, l_devices=l_devices[0]))
        return suite

