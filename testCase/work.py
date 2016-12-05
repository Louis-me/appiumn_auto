__author__ = 'shikun'
import unittest
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase
from common.variable import GetVariable as common
class testContact(TestInterfaceCase):
    def __init__(self, methodName=''):
        super(testContact, self).__init__(methodName)
        self.bc = b_app_case.GetAppCase(test_module="应用中心", AppCaseInfo=m_app_case.GetAppCaseInfo, AppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[])
    @staticmethod
    def tearDownClass():
        common.DRIVER.close_app()
        common.DRIVER.quit()
    def work_report(self):
        self.bc.execCase(PATH("yaml/contact/work.yaml"), test_name="test_work_report", isLast="1")
    def test_work_report(self):
        self.work_report()

