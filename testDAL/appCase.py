__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import json

from common import operateYaml, appPerformance as ap, operateElement as bo
from common.variable import GetVariable as common
from common import testLog
from common import reportPhone as rp
from testBLL import appBase as ba
class AppCase():

    def __init__(self, test_module="", GetAppCaseInfo="", GetAppCase="",fps=[], cpu=[], men=[]):
        self.test_module = test_module
        self.GetAppCaseInfo = GetAppCaseInfo
        self.GetAppCase = GetAppCase
        self.fps = fps
        self.cpu = cpu
        self.men = men
    def getModeList(self, f):
        bs = []
        gh = operateYaml.getYam(f)
        for i in range(len(gh)):
            if i == 0:
                  #用例id
                self.GetAppCaseInfo.test_id = gh[i].get("test_id", "false")
                 # 用例介绍
                self.GetAppCaseInfo.test_intr = gh[i].get("test_intr", "false")
            # bt = self.GetAppCase
            self.GetAppCase.element_info = gh[i].get("element_info", "false")

          # 操作类型
            self.GetAppCase.operate_type = gh[i].get("operate_type", "false")
            # 输入文字
            self.GetAppCase.name = gh[i].get("name", "false")

            self.GetAppCase.index = gh[i].get("index", "false")

            self.GetAppCase.text = gh[i].get("text", "false") # 对应by_link_text

           # 验证类型
            self.GetAppCase.find_type = gh[i].get("find_type", "false")

            self.GetAppCase.time = gh[i].get("time", 0)

            bs.append(json.loads(json.dumps(self.GetAppCase().to_primitive())))
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

                get_men = ap.get_men(common.PACKAGE)
                get_cpu = ap.top_cpu(common.PACKAGE)
                get_fps = ap.get_fps(common.PACKAGE)


                self.cpu.append(get_cpu)
                self.men.append(get_men)
                self.fps.append(get_fps)

                common.MEN.append(get_men)
                common.CPU.append(get_cpu)
                common.FPS.append(get_fps)


        if go.findElement(ch_check):
            common.test_success += 1
            self.GetAppCaseInfo.test_result = "成功"
            logTest.resultOK(kwargs["test_name"])
        else:
            # logTest.screenshotNG(GetVariable.DRIVER, kwargs["test_name"])
            logTest.checkPointNG(common.DRIVER, kwargs["test_name"], kwargs["test_name"])
            common.test_failed += 1
            test_reason = "检查不到元素"
            # if GetVariable.I_ANR > 0:
            #     test_reason = "有ANR错误"
            # if GetVariable.I_CRASH > 0:
            #     test_reason = "有CRASH错误"
            # if GetVariable.I_EXCEPTION > 0:
            #     test_reason = "有EXCEPTION错误"
            self.GetAppCaseInfo.test_result = "失败"
            self.GetAppCaseInfo.test_reason = test_reason

        self.GetAppCaseInfo.test_name =kwargs["test_name"]
        self.GetAppCaseInfo.test_module = self.test_module
        common.test_sum += 1

        self.GetAppCaseInfo.test_men_max = rp.phone_max_use_raw(self.men)
        avg_men = ba.get_avg_raw(self.men)  # 获取每次占用内存多少
        self.GetAppCaseInfo.test_men_avg = avg_men
        self.GetAppCaseInfo.test_cpu_max = rp.phone_avg_max_use_cpu(self.cpu)
        self.GetAppCaseInfo.test_cpu_avg = rp.phone_avg_use_cpu(self.cpu)
        self.GetAppCaseInfo.test_fps_max = rp.fps_max(self.fps)
        self.GetAppCaseInfo.test_fps_avg = rp.fps_avg(self.fps)

        common.RESULT["info"].append(json.loads(json.dumps(self.GetAppCaseInfo().to_primitive())))
        if kwargs["isLast"] == "1":
        # 最后case要写最下面的统计步骤
            common.RRPORT["info"].append(common.RESULT["info"])
