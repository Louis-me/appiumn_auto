__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import datetime
import xlsxwriter
import time
import unittest
from testRunner.runner import ga, TestInterfaceCase
from testCase.home.Home import testHome
from testCase.home.Home1 import testHome1
from testBLL import BgetEmail
from testBLL import BtestServer
from testBLL import BAdbCommon
from testMode import Memail
from testBLL import BsendEmail
from testBLL import BExcelReport
from testBLL import BappKernel
from testBLL import BAppBaseMsg
from Common.CoGlobal import *
import math
def get_email():
    email = BgetEmail.read_email("D:\\app\\appium_study\\email.ini")
    me = Memail.email()
    me.report = "report.xlsx"
    me.to_addr = email[0]
    me.mail_host = email[1]
    me.mail_user = email[2]
    me.mail_pass = email[3]
    me.port = email[4]
    me.headerMsg = email[5]
    me.attach = email[6]
    return me
def get_app_basemsg():
    ab = BAppBaseMsg.apkInfo(r"D:\app\appium_study\t1.apk")
    apk_name = ab.get_apk_name() # app名字
    apk_siz = ab.get_apk_size() # app大小
    apk_version = ab.get_apk_version() # app版本
    return apk_name, apk_siz, apk_version

def get_phone():
    pix = BappKernel.get_app_pix()
    men_total = BappKernel.get_men_total("d:\men_total.txt")
    phone_msg = BappKernel.getPhoneMsg("d:\phone.txt")
    cpu_sum = BappKernel.get_cpu_kel("d:\cpu.txt")
    return phone_msg, men_total, cpu_sum, pix

def get_common_report(start_test_time, endtime, starttime):
    appbase = get_app_basemsg()
    g_phone = get_phone()
    common.RRPORT["test_sum"] = common.test_sum
    common.RRPORT["test_failed"] = common.test_failed
    common.RRPORT["test_success"] = common.test_success
    common.RRPORT["test_sum_date"] = (endtime - starttime).seconds
    common.RRPORT["app_name"] = appbase[0]
    common.RRPORT["app_size"] = appbase[1]
    common.RRPORT["phone_name"] = g_phone[0]["phone_name"] +" " +g_phone[0]["phone_model"]
    common.RRPORT["phone_rel"] = g_phone[0]["release"]
    common.RRPORT["phone_pix"] = g_phone[3]
    raw = g_phone[1]/1024
    common.RRPORT["phone_raw"] = str(math.ceil(raw)) + "M"

    # str(ceil(int(men_total)/1000)) + "M"
    men = [math.ceil((int(common.MEN[i])/1024)/raw) for i in range(len(common.MEN))]  # 获取每次占用内存多少

    common.RRPORT["phone_avg_use_raw"] = str(math.ceil(sum(men)/len(men))) + "%" # 平均占用内存率
    common.RRPORT["phone_max_use_raw"] = str(math.ceil(max(common.MEN)/1024)) + "KB" # 最大运行内存
    common.RRPORT["phone_cpu"] = g_phone[2]
    common.RRPORT["phone_avg_use_cpu"] = str(math.ceil(sum(common.CPU)/len(common.CPU))) + "%" # cpu平均占用情况
    common.RRPORT["phone_avg_max_use_cpu"] = str(max(common.CPU)) + "%" # cpu最大峰值
    common.RRPORT["app_version"] = appbase[2]
    common.RRPORT["test_date"] = start_test_time


def runnerCaseApp():
    start_test_time = time.strftime("%Y-%m-%d %H:%M %p", time.localtime())
    suite = unittest.TestSuite()
    starttime = datetime.datetime.now()
    suite.addTest(TestInterfaceCase.parametrize(testHome))
    suite.addTest(TestInterfaceCase.parametrize(testHome1))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.datetime.now()
    get_common_report(start_test_time, endtime, starttime)

def report(appium_server):
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    print(common.RRPORT)
    bc = BExcelReport.sendReport(wd=workbook, data=common.RRPORT)
    bc.init(worksheet)
    bc.detail(worksheet2)
    bc.close()
    BsendEmail.send_mail(get_email())
    appium_server.stop_server()

if __name__ == '__main__':
    if BAdbCommon.attached_devices():
        if ga.platformName == common.ANDROID or ga.platformName == common.IOS:
            appium_server = BtestServer.AppiumServer(ga.appiumJs, ga.Remote)
            appium_server.start_server()
            while not appium_server.is_runnnig():
                time.sleep(1)
            runnerCaseApp()
            appium_server.stop_server()
            report(appium_server)
    else:
        print(u"设备不存在")
