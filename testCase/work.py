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
    @staticmethod
    def tearDownClass():
        common.DRIVER.close_app()
        common.DRIVER.quit()
    def work_report(self):
        self.bc.execCase(PATH("yaml/contact/work.yaml"), test_name="test_work_report", isLast="1")
    def test_work_report(self):
        self.work_report()

