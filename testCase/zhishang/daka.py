__author__ = 'Administrator'
import unittest

from testRunner.runner import TestInterfaceCase
from testBLL.BaseCaseList import *

result = {"info":[]}
result["test_module"] = "应用中心"
result["test_success"] = 0
result["test_sum"] = 0
result["test_failed"] = 0
result["test_error"] = 0
class testDaka(unittest.TestCase):
    def __init__(self,methodName=''):
        super(testDaka, self).__init__(methodName)
        self.bc = BexceCase(result)
    @staticmethod
    def setUpClass():
        TestInterfaceCase.setUpClass()
    @staticmethod
    def tearDownClass():
        TestInterfaceCase.tearDownClass()
    # @staticmethod
    # def test_login(self):
    #     self.bc.execCase(r'D:\appium\testcase\myinfo\login.yaml', test_id="2002", test_intr="登陆", test_case="test_login",isLast="0")
    # def test_loginOut(self):
    #     self.bc.execCase(r'D:\appium\testcase\myinfo\loginOut.yaml', test_id="2003", test_intr="登陆退出", test_case="test_loginOut", isLast="1")
    def test_daka(self):
        self.bc.execCase(r'D:\appium\testcase\zhishang\daka.yaml', test_id="2004", test_intr="打卡下班", test_case="test_daka", isLast="1", type=common.FIND_STR)


