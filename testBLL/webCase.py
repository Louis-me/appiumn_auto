__author__ = 'shikun'
# -*- coding: utf-8 -*-
from testDAL import webCase
class BexceCase():
    def __init__(self, test_module="", getTempCase="", BaseTestCase=""):
        self.test_module = test_module
        self.getTempCase = getTempCase
        self.BaseTestCase = BaseTestCase
        self.be = webCase.WebCase(self.test_module, self.getTempCase, self.BaseTestCase)
    def execCase(self, f, **kwargs):
        self.be.execCase(f, **kwargs)

