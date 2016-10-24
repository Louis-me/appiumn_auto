__author__ = 'Administrator'
import unittest

from testBLL import BaseCaseList
from testMode import MBaseTestCase
from testRunner.runner import TestInterfaceCase
class testHome1(TestInterfaceCase):
    def __init__(self, methodName=''):
        super(testHome1, self).__init__(methodName)
        self.bc = BaseCaseList.BexceCase(test_module="首页", getTempCase=MBaseTestCase.getTempCase, BaseTestCase=MBaseTestCase.BaseTestCase)
    def home_fist_open(self):
        self.bc.execCase(r'D:\appium\testcase\home\home_fist_open.yaml', test_name="test_home_fist_open", isLast="0")

    def home_login(self):
        self.bc.execCase(r'D:\appium\testcase\home\home_login.yaml', test_name="test_home_login", isLast="0")

    def home_feed(self):
        self.bc.execCase(r'D:\appium\testcase\home\home_feed.yaml', test_name="test_home_feed", isLast="1")
    def test_home(self):
        # self.home_fist_open()
        # self.home_login()
        self.home_feed()

    # def test_home_shopcart(self):
    #      self.bc.execCase(r'D:\appium\testcase\home\home_shopcart.yaml', test_name="test_home_shopcart", isLast="0")
    #
    # # def test_home_code(self):
    # #     self.bc.execCase(r'D:\appium\testcase\home\home_code.yaml', test_name="test_home_code", isLast="1")
    # def test_home_mycode(self):
    #      self.bc.execCase(r'D:\appium\testcase\home\home_mycode.yaml', test_name="test_home_mycode", isLast="1")

