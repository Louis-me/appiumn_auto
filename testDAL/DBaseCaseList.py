__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import json

from Common import getXMl, appPerformance as ap, baseOperateElement as bo
from Common.CoGlobal import *
# temp = getTempCase()
class BexceCase():
    """
    :param f: 读取用例文件位置
    :param kwargs: test_id,test_intr,test_case,isLast
    :return:
    """
    def __init__(self, test_module="", getTempCase="", BaseTestCase=""):
        self.test_module = test_module
        self.getTempCase = getTempCase
        self.BaseTestCase = BaseTestCase

    def getModeList(self, f):
        bs = []
        gh = getXMl.getYam(f)
        for i in range(len(gh)):
            if i == 0:
                  #用例id
                self.getTempCase.test_id = gh[i].get("test_id", "false")
                 # 用例介绍
                self.getTempCase.test_intr = gh[i].get("test_intr", "false")
            # bt = self.BaseTestCase
            self.BaseTestCase.element_info = gh[i]["element_info"]

          # 操作类型
            self.BaseTestCase.operate_type = gh[i].get("operate_type", "false")
            self.BaseTestCase.element_type = gh[i]["findElemtType"]
            # 输入文字
            self.BaseTestCase.msg = gh[i].get("msg", "false")

           # 验证类型
            self.BaseTestCase.find_type =gh[i].get("find_type", "false")
            bs.append(json.loads(json.dumps(self.BaseTestCase().to_primitive())))
        return bs

    def execCase(self, f, **kwargs):

        bc = self.getModeList(f)
        go = bo.getOperateElement(driver=common.DRIVER)
        ch_check = bc[-1]
        print(bc)
        for k in bc:
            if k["operate_type"] != "false":
                go.operate_element(k["operate_type"], k["element_type"], k["element_info"])
                common.MEN.append(ap.get_men(common.PACKAGE))
                common.CPU.append(ap.top_cpu(common.PACKAGE))
        # logTest = myLog.getLog()
        if go.findElement(elemt_by=ch_check["element_type"], element_info=ch_check["element_info"], type=ch_check["find_type"]):
            # logTest.resultOK(self.result["test_module"])
            common.test_success += 1
            self.getTempCase.test_result = "成功"
        else:
            # logTest.resultNG(self.result["test_module"])
            common.test_failed += 1
            self.getTempCase.test_result = "失败"
            self.getTempCase.test_reason = "扩展"


        self.getTempCase.test_name =kwargs["test_name"]
        self.getTempCase.test_module = self.test_module
        common.test_sum += 1

        common.RESULT["info"].append(json.loads(json.dumps(self.getTempCase().to_primitive())))
        if kwargs["isLast"] == "1":
        # 最后case要写最下面的统计步骤
            common.RRPORT["info"].append(common.RESULT["info"])
# getModeList(r"D:\appium\testcase\myinfo\login.yaml")



