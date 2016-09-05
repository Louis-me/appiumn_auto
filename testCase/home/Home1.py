__author__ = 'Administrator'
import unittest

from testRunner.runner import TestInterfaceCase
from testBLL import BaseCaseList
from testMode import MBaseTestCase

class testHome1(unittest.TestCase):
    def __init__(self,methodName=''):
        super(testHome1, self).__init__(methodName)
        self.bc = BaseCaseList.BexceCase(test_module="我的模块1", getTempCase=MBaseTestCase.getTempCase, BaseTestCase=MBaseTestCase.BaseTestCase)
    @staticmethod
    def setUpClass():
        TestInterfaceCase.setUpClass()
    @staticmethod
    def tearDownClass():
        TestInterfaceCase.tearDownClass()
    def test_home_info(self):
        self.bc.execCase(r'D:\appium\testcase\home\home_info.yaml', test_name="test_home_info", isLast="0")

    def test_home_shopcart(self):
         self.bc.execCase(r'D:\appium\testcase\home\home_shopcart.yaml', test_name="test_home_shopcart", isLast="0")

    # def test_home_code(self):
    #     self.bc.execCase(r'D:\appium\testcase\home\home_code.yaml', test_name="test_home_code", isLast="1")
    def test_home_mycode(self):
         self.bc.execCase(r'D:\appium\testcase\home\home_mycode.yaml', test_name="test_home_mycode", isLast="1")

