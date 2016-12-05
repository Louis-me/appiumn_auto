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


class testMonkey(te):
    # def __init__(self, methodName=''):
    #     super(testHome, self).__init__(methodName)
    def setUp(self):
        super(testMonkey, self).setUp()
        self.bc = b_app_case.GetAppCase(test_module="闪退测试", GetAppCaseInfo=m_app_case.GetAppCaseInfo, GetAppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[],
                                        driver=self.driver, package=self.get_apk_pkg(), devices=self.l_devices["deviceName"])
    def monkey_crash(self):
        _yaml = ""
        if self.l_devices["deviceName"] == "JTJ4C16331013562":
            _yaml = PATH("yaml/monkey/crash.yaml")
        if self.l_devices["deviceName"] == "DU2TAN15AJ049163":
            _yaml = PATH("yaml/monkey/crash1.yaml")
        self.bc.execCase(_yaml, test_name="test_home_feed", isLast="1")

    def get_apk_pkg(self):
        return apkBase.apkInfo(PATH("../img/monkneyTest.apk")).get_apk_pkg()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass
    @staticmethod
    def tearDownClass():
        pass
    def test_monkey(self):
        # self.home_fist_open()
        self.monkey_crash()

