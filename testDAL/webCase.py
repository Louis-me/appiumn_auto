__author__ = 'shikun'
# -*- coding: utf-8 -*-
import json

from common import operateYaml, operateElement as bo
from common.variable import GetVariable as common
from common import testLog
class WebCase():

    def __init__(self, test_module="", GetWebInfoCase="", GetWebCase=""):
        self.test_module = test_module
        self.GetWebInfoCase = GetWebInfoCase
        self.GetWebCase = GetWebCase
    def getModeList(self, f):
        bs = []
        gh = operateYaml.getYam(f)
        for i in range(len(gh)):
            if i == 0:
                  #用例id
                self.GetWebInfoCase.test_id = gh[i].get("test_id", "false")
                 # 用例介绍
                self.GetWebInfoCase.test_intr = gh[i].get("test_intr", "false")
            self.GetWebCase.element_info = gh[i].get("element_info", "false")
            self.GetWebCase.open_url = gh[i].get("get_url", "false")
          # 操作类型
            self.GetWebCase.operate_type = gh[i].get("operate_type", "false")
            self.GetWebCase.index = gh[i].get("index", "false")
            self.GetWebCase.text = gh[i].get("text", "false") # 输入的text
           # 验证类型
            self.GetWebCase.find_type = gh[i].get("find_type", "false")
            bs.append(json.loads(json.dumps(self.GetWebCase().to_primitive())))
        return bs

    def execCase(self, f, **kwargs):
        logTest = testLog.myLog().getLog()
        bc = self.getModeList(f)
        go = bo.OperateElement(driver=common.DRIVER)
        ch_check = bc[-1]
        for k in bc:
            if k["operate_type"] != "false":
                if go.operate_element(k)== False:
                     logTest.checkPointNG(common.DRIVER, kwargs["test_name"], kwargs["test_name"])
                     logTest.resultNG(kwargs["test_name"], "找不页面元素")
        if go.findElement(ch_check):
            common.test_success += 1
            self.GetWebInfoCase.test_result = "成功"
            logTest.resultOK(kwargs["test_name"])
        else:
            logTest.checkPointNG(common.DRIVER, kwargs["test_name"], kwargs["test_name"])
            common.test_failed += 1
            test_reason = "检查不到元素"
            self.GetWebInfoCase.test_result = "失败"
            self.GetWebInfoCase.test_reason = test_reason

        self.GetWebInfoCase.test_name =kwargs["test_name"]
        self.GetWebInfoCase.test_module = self.test_module
        common.test_sum += 1

        common.RESULT["info"].append(json.loads(json.dumps(self.GetWebInfoCase().to_primitive())))
        if kwargs["isLast"] == "1":
        # 最后case要写最下面的统计步骤
            common.RRPORT["info"].append(common.RESULT["info"])
