__author__ = 'shikun'
import unittest
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase as te
from testBLL import apkBase



class testHome(te):
    # def __init__(self, methodName=''):
    #     super(testHome, self).__init__(methodName)
    def setUp(self):
        super(testHome, self).setUp()
        self.bc = b_app_case.GetAppCase(test_module="个人中心", GetAppCaseInfo=m_app_case.GetAppCaseInfo, GetAppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[],
                                        driver=self.driver, package=self.get_apk_pkg(), devices=self.l_devices["deviceName"])
    def home_fist_open(self):
        self.bc.execCase(PATH("yaml/myinfo/home_fist_open.yaml"), test_name="test_home_fist_open", isLast="0")

    def home_login(self):
        self.bc.execCase(PATH("yaml/myinfo/home_login.yaml"), test_name="test_home_login", isLast="0")

    def home_feed(self):
        self.bc.execCase((PATH("yaml/myinfo/home_feed.yaml")), test_name="test_home_feed", isLast="1")

    def get_apk_pkg(self):
        return apkBase.apkInfo(PATH("../img/t.apk")).get_apk_pkg()
    @staticmethod
    def tearDownClass():
        pass
    def test_home(self):
        # self.home_fist_open()
        # self.home_login()
        self.home_login()

