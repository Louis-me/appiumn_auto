__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from testDAL import DWebBaseCaseList
class BexceCase():
    def __init__(self, test_module="", getTempCase="", BaseTestCase=""):
        self.test_module = test_module
        self.getTempCase = getTempCase
        self.BaseTestCase = BaseTestCase
        self.be = DWebBaseCaseList.BWebexceCase(self.test_module, self.getTempCase, self.BaseTestCase)
    def execCase(self, f, **kwargs):
        self.be.execCase(f, **kwargs)

