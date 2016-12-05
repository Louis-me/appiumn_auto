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


class testLogin(te):
    # def __init__(self, methodName=''):
    #     super(testHome, self).__init__(methodName)
    def setUp(self):
        super(testLogin, self).setUp()
        self.bc = b_app_case.GetAppCase(test_module="我的", GetAppCaseInfo=m_app_case.GetAppCaseInfo, GetAppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[],
                                        driver=self.driver, package=self.get_apk_pkg(), devices=self.l_devices["deviceName"])
    def home_feed(self):
        self.bc.execCase(PATH("yaml/myinfo/home_feed.yaml"), test_name="test_home_feed", isLast="1")

    # 单点登陆这里特殊处理,不同的设备调用不同的case
    def home_login(self):
        home_logon_yaml = ""
        if self.l_devices["deviceName"] == "JTJ4C16331013562":
            home_logon_yaml = PATH("yaml/myinfo/home_login.yaml")
        if self.l_devices["deviceName"] == "MSM8926":
            home_logon_yaml = PATH("yaml/myinfo/home_login1.yaml")
        self.bc.execCase(home_logon_yaml, test_name="test_home_login", isLast="0")

    def get_apk_pkg(self):
        return apkBase.apkInfo(PATH("../img/t.apk")).get_apk_pkg()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass
    @staticmethod
    def tearDownClass():
        pass
    def test_home(self):
        # self.home_fist_open()
        self.home_login()
        self.home_feed()

