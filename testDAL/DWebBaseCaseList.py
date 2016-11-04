__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import json

from Common import getXMl, baseOperateElement as bo
from Common.CoGlobal import *
from Common import testLog
class BWebexceCase():

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
            self.BaseTestCase.element_info = gh[i].get("element_info", "false")
            self.BaseTestCase.open_url = gh[i].get("get_url", "false")
          # 操作类型
            self.BaseTestCase.operate_type = gh[i].get("operate_type", "false")
            self.BaseTestCase.index = gh[i].get("index", "false")
            self.BaseTestCase.text = gh[i].get("text", "false") # 输入的text
           # 验证类型
            self.BaseTestCase.find_type = gh[i].get("find_type", "false")
            bs.append(json.loads(json.dumps(self.BaseTestCase().to_primitive())))
        return bs

    def execCase(self, f, **kwargs):
        logTest = testLog.myLog().getLog()
        bc = self.getModeList(f)
        go = bo.getOperateElement(driver=common.DRIVER)
        ch_check = bc[-1]
        for k in bc:
            if k["operate_type"] != "false":
                if go.operate_element(k)== False:
                     logTest.checkPointNG(common.DRIVER, kwargs["test_name"], kwargs["test_name"])
                     logTest.resultNG(kwargs["test_name"], "找不页面元素")
        if go.findElement(ch_check):
            common.test_success += 1
            self.getTempCase.test_result = "成功"
            logTest.resultOK(kwargs["test_name"])
        else:
            logTest.checkPointNG(common.DRIVER, kwargs["test_name"], kwargs["test_name"])
            common.test_failed += 1
            test_reason = "检查不到元素"
            self.getTempCase.test_result = "失败"
            self.getTempCase.test_reason = test_reason

        self.getTempCase.test_name =kwargs["test_name"]
        self.getTempCase.test_module = self.test_module
        common.test_sum += 1

        common.RESULT["info"].append(json.loads(json.dumps(self.getTempCase().to_primitive())))
        if kwargs["isLast"] == "1":
        # 最后case要写最下面的统计步骤
            common.RRPORT["info"].append(common.RESULT["info"])
