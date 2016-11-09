__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from common.variable import GetVariable as common
from testMode import devices as mdevices
from testBLL import devices
import os
from selenium import webdriver as web
from seleniumrequests import Chrome

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



def get_evices():
    return devices.get_devices(mdevices, PATH("../devices.ini"), PATH("../img/t.apk"))

def appium_testcase(ga):
    desired_caps = {}
    desired_caps['platformName'] = ga.platformName
    desired_caps['platformVersion'] = ga.platformVersion
    desired_caps['deviceName'] = ga.deviceName
    desired_caps['appPackage'] = "cn.ibona.t1_beta"
    desired_caps['appActivity'] = ga.appActivity
    desired_caps['app'] = PATH( '../img/t.apk')
    #     desired_caps["unicodeKeyboard"] = "True"
    #     desired_caps["resetKeyboard"] = "True"
    common.PACKAGE = ga.appPackage
    driver = webdriver.Remote(ga.Remote, desired_caps)
    common.DRIVER = driver
    common.FLAG = False

def selenium_testcase(ga):
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = web.Chrome(chromedriver)
    # driver = web.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
    common.DRIVER = driver
    common.FLAG = False
    driver.maximize_window()  #将浏览器最大化
    driver.get(ga.open_url)
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestInterfaceCase, self).__init__(methodName)
    @staticmethod
    def setUpClass():
        global driver
        ga = get_evices()
        common.SELENIUM_APPIUM = ga.selenium_appium
        if common.SELENIUM_APPIUM == common.APPIUM: # appium入口
            if ga.platformName == common.ANDROID and common.FLAG:
                appium_testcase(ga)
        if common.SELENIUM_APPIUM == common.SELENIUM and common.FLAG: # selenium入口
            selenium_testcase(ga)
            # driver.get("http://www.baidu.com")
            # data = driver.title
            pass
    def setUp(self):
        print("setUp")
    @staticmethod
    def tearDownClass():
        # driver.close_app()
        # driver.quit()
        print('tearDownClass')
    @staticmethod
    def parametrize(testcase_klass):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name))
        return suite

