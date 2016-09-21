__author__ = 'Administrator'
import unittest

from testRunner.runner import TestInterfaceCase
from testBLL import BaseCaseList
from testMode import MBaseTestCase

class testCrash(unittest.TestCase):
    def __init__(self,methodName=''):
        super(testCrash, self).__init__(methodName)
        self.bc = BaseCaseList.BexceCase(test_module="闪退测试", getTempCase=MBaseTestCase.getTempCase, BaseTestCase=MBaseTestCase.BaseTestCase)
    @staticmethod
    def setUpClass():
        TestInterfaceCase.setUpClass()
    @staticmethod
    def tearDownClass():
        TestInterfaceCase.tearDownClass()
    def test_crase1(self):
        self.bc.execCase(r'D:\appium\testcase\home\home_crash.yaml', test_name="test_crase1", isLast="0")
    def test_crase2(self):
        self.bc.execCase(r'D:\appium\testcase\home\home_info.yaml', test_name="test_crase1", isLast="1")
