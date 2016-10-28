__author__ = 'Administrator'
import unittest
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import BaseCaseList
from testMode import MBaseTestCase
from testRunner.runner import TestInterfaceCase
from Common.CoGlobal import *
class testContact(TestInterfaceCase):
    def __init__(self, methodName=''):
        super(testContact, self).__init__(methodName)
        self.bc = BaseCaseList.BexceCase(test_module="应用中心", getTempCase=MBaseTestCase.getTempCase, BaseTestCase=MBaseTestCase.BaseTestCase, fps=[], cpu=[], men=[])
    # def home_fist_open(self):
    #     self.bc.execCase(r'D:\appium\testcase\myinfo\home_fist_open.yaml', test_name="test_home_fist_open", isLast="0")
    #
    # def home_login(self):
    #     self.bc.execCase(r'D:\appium\testcase\myinfo\home_login.yaml', test_name="test_home_login", isLast="0")
    @staticmethod
    def tearDownClass():
        common.DRIVER.close_app()
        common.DRIVER.quit()
    def work_report(self):
        self.bc.execCase(PATH("yaml/contact/work.yaml"), test_name="test_work_report", isLast="1")
    def test_home(self):
        self.work_report()

    # def test_home_shopcart(self):
    #      self.bc.execCase(r'D:\appium\testcase\myinfo\home_shopcart.yaml', test_name="test_home_shopcart", isLast="0")
    #
    # # def test_home_code(self):
    # #     self.bc.execCase(r'D:\appium\testcase\myinfo\home_code.yaml', test_name="test_home_code", isLast="1")
    # def test_home_mycode(self):
    #      self.bc.execCase(r'D:\appium\testcase\myinfo\home_mycode.yaml', test_name="test_home_mycode", isLast="1")

