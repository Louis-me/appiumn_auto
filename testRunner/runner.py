__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from Common.CoGlobal import *
from testMode import MAppDevices
from testBLL import BAppDevices
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def appDevices():
    mapp = MAppDevices.getDriver()
    return BAppDevices.appDevices(mapp, PATH("../AppDevices.ini"))
ga = appDevices()
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestInterfaceCase, self).__init__(methodName)
    @staticmethod
    def setUpClass():
        desired_caps = {}
        global driver
        if ga.platformName == common.ANDROID or ga.platformName == common.IOS:
            if common.FLAG:
                desired_caps['platformName'] = ga.platformName
                desired_caps['platformVersion'] = ga.platformVersion
                desired_caps['deviceName'] = ga.deviceName
                desired_caps['appPackage'] = ga.appPackage
                desired_caps['appActivity'] = ga.appActivity
                desired_caps['app'] = PATH(
                '../img/t.apk'
            )
            #     desired_caps["unicodeKeyboard"] = "True"
            #     desired_caps["resetKeyboard"] = "True"
                common.PACKAGE = ga.appPackage
                driver = webdriver.Remote(ga.Remote, desired_caps)
                print("FLAG_setUpClass")
                print(common.FLAG)
                common.DRIVER = driver
                common.FLAG = False
    def setUp(self):
        print("FLAG_setUp")
        print(common.FLAG)

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

