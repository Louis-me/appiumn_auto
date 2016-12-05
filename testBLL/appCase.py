__author__ = 'shikun'
# -*- coding: utf-8 -*-
from testDAL import appCase
class GetAppCase():
    # def __init__(self, test_module="", AppCaseInfo="", AppCase="",fps=[], cpu=[], men=[]):
    def __init__(self, **kwargs):
        '''
        :param kwargs:
        test_module:'模块名'
        GetAppCaseInfo: '用例详情' model层
        GetAppCase: 'app case' model层
        fps: []
        cpu: []
        men: []
        driver:
        package： 包名
        devices: 设备名
        '''
        self.kwargs= kwargs
        self.be = appCase.AppCase(**self.kwargs)
    def execCase(self, f, **kwargs):
        '''

        :param f: 用例文件
        :param kwargs:
        test_name: 用例名
        is_last: 最后一个用例 1, 0
        :return:
        '''
        self.be.execCase(f, **kwargs)

