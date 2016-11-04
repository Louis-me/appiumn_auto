__author__ = 'Administrator'
from Common.CoGlobal import *
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import WebBaseCaseList
from testMode import MWebBaseTestCase
from testRunner.runner import TestInterfaceCase
class testComment(TestInterfaceCase):
    def __init__(self, methodName=''):
        super(testComment, self).__init__(methodName)
        self.bc = WebBaseCaseList.BexceCase(test_module="个人中心", getTempCase=MWebBaseTestCase.getWebTempCase, BaseTestCase=MWebBaseTestCase.BaseWebTestCase)
    def my_comment(self):
        self.bc.execCase(PATH("../yaml/web/my_comment.yaml"), test_name="my_comment", isLast="1")

    @staticmethod
    def tearDownClass():
        common.DRIVER.quit()
    def test_home(self):
        self.my_comment()
    # def test_home_shopcart(self):
    #      self.bc.execCase(r'D:\appium\testcase\myinfo\home_shopcart.yaml', test_name="test_home_shopcart", isLast="0")
    #
    # # def test_home_code(self):
    # #     self.bc.execCase(r'D:\appium\testcase\myinfo\home_code.yaml', test_name="test_home_code", isLast="1")
    # def test_home_mycode(self):
    #      self.bc.execCase(r'D:\appium\testcase\myinfo\home_mycode.yaml', test_name="test_home_mycode", isLast="1")

