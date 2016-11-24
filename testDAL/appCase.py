__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import json

from common import operateYaml, appPerformance as ap, operateElement as bo
from common.variable import GetVariable as common
from common import testLog
from common import reportPhone as rp
from testBLL import phoneBase as ba
import os
from common import  operateFile
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class AppCase():

    # def __init__(self, test_module="", GetAppCaseInfo="", GetAppCase="",fps=[], cpu=[], men=[]):
    def __init__(self, **kwargs):
        '''

        :param kwargs:
        test_module:'模块名'
        GetAppCaseInfo: '用例介绍'
        GetAppCase: 'app case'
        fps: []
        cpu: []
        men: []
        driver:
        package： 包名
        devices: 设备名
        '''
        self.test_module = kwargs["test_module"]
        self.GetAppCaseInfo = kwargs["GetAppCaseInfo"]
        self.GetAppCase = kwargs["GetAppCase"]
        self.fps = kwargs["fps"]
        self.cpu = kwargs["cpu"]
        self.men = kwargs["men"]
        self.driver = kwargs["driver"]
        self.package = kwargs["package"]
        self.devices = kwargs["devices"]
    def get_phone_name(self):
        get_phone = ba.get_phone_info(devices=self.devices)
        phone_name = get_phone["brand"] + "_" +get_phone["model"] + "_"+"android" +"_"+ get_phone["release"]
        return phone_name

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

            self.GetAppCase.log = r"d:/" + self.get_phone_name()

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
        '''

        :param f: 用例文件
        :param kwargs:
        test_name: 用例名
        is_last: 最后一个用例 1, 0
        :return:
        '''
        logTest = testLog.myLog().getLog()
        bc = self.getModeList(f)
        go = bo.OperateElement(driver=self.driver)
        ch_check = bc[-1]
        # l_report = {"info": [], "init": []}  # case的init,info信息
        # _init = []
        # _info = []
        _d_report_common = {"test_success": 0, "test_failed": 0, "test_sum": 0} #case的运行次数和性能
        for k in bc:
            if k["operate_type"] != "false":
                k["devices"] = self.devices
                if go.operate_element(k)== False:
                     logTest.checkPointNG(driver=self.driver,caseName=kwargs["test_name"], checkPoint=kwargs["test_name"])
                     logTest.resultNG(kwargs["test_name"], "找不页面元素")

                get_men = ap.get_men(devices=self.devices, pkg_name=self.package)
                get_cpu = ap.top_cpu(devices=self.devices, pkg_name=self.package)
                get_fps = ap.get_fps(devices=self.devices, pkg_name=self.package)

                # 单个case
                self.GetAppCaseInfo.test_devices = self.get_phone_name()
                self.cpu.append(get_cpu)
                self.men.append(get_men)
                self.fps.append(get_fps)

        _d_report_common["test_sum"] += 1
        if go.findElement(ch_check):
            _d_report_common["test_success"] += 1
            self.GetAppCaseInfo.test_result = "成功"
            logTest.resultOK(kwargs["test_name"])
            self.write_report_collect(_d_report_common, f=common.REPORT_COLLECT_PATH)  # 写入case运行的总个数

        else:
            # logTest.screenshotNG(GetVariable.DRIVER, kwargs["test_name"])
            logTest.checkPointNG(driver=self.driver, caseName=kwargs["test_name"], checkPoint=kwargs["test_name"])
            _d_report_common["test_failed"] += 1
            test_reason = "检查不到元素"
            self.write_report_collect(_d_report_common, f=common.REPORT_COLLECT_PATH)  # 写入case运行的总个数

            self.GetAppCaseInfo.test_result = "失败"
            self.GetAppCaseInfo.test_reason = test_reason

        self.GetAppCaseInfo.test_name =kwargs["test_name"]
        self.GetAppCaseInfo.test_module = self.test_module


        self.GetAppCaseInfo.test_men_max = rp.phone_max_use_raw(self.men) #内存最大使用情况
        avg_men = ba.get_avg_raw(self.men, self.devices)  # 获取每次占用内存平均值
        self.GetAppCaseInfo.test_men_avg = avg_men
        self.GetAppCaseInfo.test_cpu_max = rp.phone_avg_max_use_cpu(self.cpu) #cpu最大使用
        self.GetAppCaseInfo.test_cpu_avg = rp.phone_avg_use_cpu(self.cpu)  #cpu平均使用
        self.GetAppCaseInfo.test_fps_max = rp.fps_max(self.fps)
        self.GetAppCaseInfo.test_fps_avg = rp.fps_avg(self.fps)
        self.GetAppCaseInfo.test_phone_name = self.get_phone_name()


        info_case = json.loads(json.dumps(self.GetAppCaseInfo().to_primitive()))
        # _info.append(info_case)
        self.write_detail(info_case, f=common.REPORT_INFO_PATH, key="info")  # 写入所有的case包括，init,info中的excel中的case情况
        if kwargs["isLast"] == "1":
            d_report = {}
            raw = ba.get_men_total(devices=self.devices)
            d_report["phone_name"] = self.get_phone_name()
            d_report["phone_pix"] = ba.get_app_pix(self.devices)
            d_report["phone_cpu"] = ba.get_cpu_kel(self.devices)
            d_report["phone_raw"] = rp.phone_raw(raw / 1024)
            # 记录每个设备的case运行情况
            d_report["phone_avg_use_cpu"] = self.GetAppCaseInfo.test_cpu_avg
            d_report["phone_avg_max_use_cpu"] = self.GetAppCaseInfo.test_cpu_max
            d_report["phone_avg_use_raw"] = self.GetAppCaseInfo.test_men_avg
            d_report["phone_max_use_raw"] = self.GetAppCaseInfo.test_men_max
            d_report["fps_avg"] = self.GetAppCaseInfo.test_fps_avg
            d_report["fps_max"] = self.GetAppCaseInfo.test_fps_max
            # _init.append(d_report)
        #最后case要写最下面的统计步骤
            self.write_detail(d_report, f=common.REPORT_INIT, key="init") #写入所有的case包括，init,info中的excel中的case情况
            # self.write_report(d_report, f=common.REPORT_PAHT) # 写入统计case成功，失败等个数
    def read_detail_report(self, f=""):
       op = operateFile.OperateFile(f, "r")
       return op.read_txt_row()

    # 写入统计case的info,init情况
    def write_detail(self, json, f="", key="info"):
        '''

        :param json: 存储的json
        :param f: 存储的文件文字，一般是info,和init的位置
        :param key:  info和init两个值,要和f的路径匹配;REPORT_INFO_PATH对应info,REPORT_INIT对应init
        这里的key就是init,当f的值为REPORT_INFO_PATH,这里
        :return:
        '''
        _read_json_temp = self.read_detail_report(f)
        _result = {}
        if len(_read_json_temp) > 0:
            _read_json = eval(_read_json_temp)
            _read_json[key].append(json)
            _result = _read_json
        else:
            _result[key] = []
            _result[key].append(json)
        op = operateFile.OperateFile(f, "w")
        op.write_txt(str(_result))
        print(_result)
    # def write_detail_init(self, json, f=""):
    #     _read_json_temp = self.read_detail_report(f)
    #     _result = {}
    #     op = operateFile.OperateFile(f, "w")
    #     if len(_read_json_temp) > 0:
    #         _read_json = eval(_read_json_temp)
    #         _read_json["init"].append(json)
    #         _result = _read_json
    #     else:
    #         _result["init"] = []
    #         _result["init"].append(json)
    #     op.write_txt(str(_result))
    #
    # 写入统计总的case的运行次数
    def write_report_collect(self, json, f=""):
        _read_json_temp = self.read_detail_report(f)
        op = operateFile.OperateFile(f, "w")
        _result = {}
        if len(_read_json_temp) > 0:
            _read_json = eval(_read_json_temp)
            for i in _read_json:
                if i == "test_success" or i == "test_failed" or i == "test_sum":  # 统计总的case的运行次数
                    _result[i] = int(_read_json[i]) + int(json[i])
                else:
                    _result[i] = _read_json[i]
        if len(_result) > 0:
            op.write_txt(str(_result))
        else:
            op.write_txt(str(json))




