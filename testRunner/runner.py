__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from Common.CoGlobal import *
from testMode import MAppDevices
from testBLL import BAppDevices

def appDevices():
    mapp = MAppDevices.getDriver()
    return BAppDevices.appDevices(mapp, r"D:\app\appium_study\AppDevices.ini")
ga = appDevices()
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestInterfaceCase, self).__init__(methodName)
    @staticmethod
    def setUpClass():
        desired_caps = {}
        global driver
        if ga.platformName == common.ANDROID or ga.platformName == common.IOS and common.FLAG:
            desired_caps['platformName'] = ga.platformName
            desired_caps['platformVersion'] = ga.platformVersion
            desired_caps['deviceName'] = ga.deviceName
            desired_caps['appPackage'] = ga.appPackage
            desired_caps['appActivity'] = ga.appActivity
            # desired_caps["unicodeKeyboard"] = "True"
            # desired_caps["resetKeyboard"] = "True"

            driver = webdriver.Remote(ga.Remote, desired_caps)

            common.DRIVER = driver
            common.FLAG = False
    @staticmethod
    def tearDownClass():
        driver.close_app()
        driver.quit()
        print('tearDownClass')

    def parametrize(testcase_klass):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name))
        return suite

