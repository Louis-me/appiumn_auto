__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import datetime
import xlsxwriter
import time
import unittest
from common import reportPhone
from testRunner.runnerBase import TestInterfaceCase
from testCase.login import testLogin
from testCase.work import testContact
from testCase.web.comment import testComment
from testBLL import email as b_email
from testBLL import server
from testBLL import adbCommon
from testMode import email as memail
from testBLL import report as b_report
from testBLL import phoneBase
from common.variable import GetVariable as common
from common import dataToString
import os
from testBLL import apkBase
from multiprocessing import Pool
from common import operateFile
from common import operateYaml
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
data = {"init":[], "info":[]}
def get_devices():
    return operateYaml.getYam(PATH("../devices.yaml"))
ga = get_devices()

def get_email():
    m_email = memail.GetEmail()
    m_email.file = PATH( '../email.ini' )
    email = b_email.read_email(m_email)
    return email
def read_report(f=""):
    op = operateFile.OperateFile(f, "r")
    return op.read_txt_row()
# 得到总统计的case
def get_report_collect(start_test_time, endtime, starttime):
    _read_collect_json = eval(read_report(common.REPORT_COLLECT_PATH))
    for key in _read_collect_json:
        data[key] = _read_collect_json[key]
    apk_msg = apkBase.apkInfo(PATH('../img/t.apk'))
    data["app_name"] = apk_msg.get_apk_name()
    data["app_size"] = apk_msg.get_apk_size()
    data["app_version"] = apk_msg.get_apk_version()
    data["test_sum_date"] = str((endtime - starttime).seconds) + "秒"
    data["test_date"] = start_test_time
# 得到每个设备的的case 运行情况
def get_report_init():
    data["init"] = eval(read_report(common.REPORT_INIT))["init"]
# 得到每个case的运行情况
def get_report_info():
    data["info"] = eval(read_report(common.REPORT_INFO_PATH))["info"]

def get_common_report(start_test_time, endtime, starttime):
    get_report_collect(start_test_time, endtime, starttime)
    get_report_init()
    get_report_info()

# def get_app_msg(f=r"D:\app\appium_study\img\t.apk"):
#     return apkBase.apkInfo(f).get_app_msg()
def get_common_web_report(start_test_time, endtime, starttime):
    pass

def runnerCaseWeb():
    suite = unittest.TestSuite()
    starttime = datetime.datetime.now()
    suite.addTest(TestInterfaceCase.parametrize(testComment))
    unittest.TextTestRunner(verbosity=2).run(suite)

def runnerPool():
    devices_Pool = []
    for i in range(0, len(ga["appium"])):
        l_pool = []
        t = {}
        t["deviceName"] = ga["appium"][i]["devices"]
        t["platformVersion"] = phoneBase.get_phone_info(devices=ga["appium"][i]["devices"])["release"]
        t["platformName"] = ga["appium"][i]["platformName"]
        t["port"] = ga["appium"][i]["port"]
        l_pool.append(t)
        devices_Pool.append(l_pool)
    pool = Pool(len(devices_Pool))
    # for i in range(2):
    #     pool.apply_async(sample_request, args=(t[i],)) # 异步
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()

def runnerCaseApp(l_devices):

    start_test_time = dataToString.getStrTime(time.localtime(), "%Y-%m-%d %H:%M %p")
    starttime = datetime.datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(testLogin, l_devices=l_devices))
    # suite.addTest(TestInterfaceCase.parametrize(testContact))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.datetime.now()
    get_common_report(start_test_time, endtime, starttime)
    report()
def report():
    workbook = xlsxwriter.Workbook('GetReport.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    print(data)
    b_OperateReport = b_report.OperateReport(wd=workbook, data=data)
    b_OperateReport.init(worksheet)
    b_OperateReport.detail(worksheet2)
    b_OperateReport.close()
    # b_email.send_mail(get_email())

if __name__ == '__main__':
        ga = get_devices()
        if adbCommon.attached_devices():
            appium_server = server.AppiumServer(ga)
            appium_server.start_server()
            while not appium_server.is_runnnig():
                time.sleep(2)
            runnerPool()
            appium_server.stop_server()
            operateFile.OperateFile(common.REPORT_COLLECT_PATH).remove_file()
            operateFile.OperateFile(common.REPORT_INIT).remove_file()
            operateFile.OperateFile(common.REPORT_INFO_PATH).remove_file()
        else:
            print(u"设备不存在")
