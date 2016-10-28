__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from testDAL import DBaseCaseList
class BexceCase():
    def __init__(self, test_module="", getTempCase="", BaseTestCase="",fps=[], cpu=[], men=[]):
        self.test_module = test_module
        self.getTempCase = getTempCase
        self.BaseTestCase = BaseTestCase
        self.fps = fps
        self.cpu = cpu
        self.men = men
        self.be = DBaseCaseList.BexceCase(self.test_module, self.getTempCase, self.BaseTestCase,self.fps, self.cpu, self.men)
    def execCase(self, f, **kwargs):
        self.be.execCase(f, **kwargs)

