__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from testDAL import appCase
class GetAppCase():
    def __init__(self, test_module="", AppCaseInfo="", AppCase="",fps=[], cpu=[], men=[]):
        self.test_module = test_module
        self.AppCaseInfo = AppCaseInfo
        self.AppCase = AppCase
        self.fps = fps
        self.cpu = cpu
        self.men = men
        self.be = appCase.AppCase(self.test_module, self.AppCaseInfo, self.AppCase, self.fps, self.cpu, self.men)
    def execCase(self, f, **kwargs):
        self.be.execCase(f, **kwargs)

