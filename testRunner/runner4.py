__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import datetime
import xlsxwriter
import time
import unittest
from Common import reportPhone
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
from testBLL import Breport
from testMode import Mreport
from Common.CoGlobal import *
import math
from Common import dataToString

def get_email():
    email = BgetEmail.read_email("D:\\app\\appium_study\\email.ini", Memail.email())
    return email

def get_app_basemsg(f=r"D:\app\appium_study\t1.apk"):
    return BAppBaseMsg.apkInfo(f).get_app_basemsg()

def get_phone(log=r"d:\phone.txt"):
    return BappKernel.get_phone_kernel(log)

def phone_avg_use_cpus(cpu):
    return reportPhone.phone_avg_use_cpu(cpu)

def phone_avg_use_raws(men):
    return reportPhone.phone_avg_use_raw(men)

def phone_max_use_raws(men):
   return reportPhone.phone_max_use_raw(men)

def phone_avg_max_use_cpus(cpu):
    return reportPhone.phone_avg_max_use_cpu(cpu)

def phone_raws(raw):
    return reportPhone.phone_raw(raw)

def getDateStr(t_time, fromat):
    return dataToString.getStrTime(t_time, fromat)

def get_common_report(start_test_time, endtime, starttime):
    mreport = Mreport.report()
    g_phone = get_phone()
    raw = g_phone[1]/1024
    appbase = get_app_basemsg()
    mreport.test_sum = common.test_sum
    mreport.test_failed = common.test_failed
    mreport.test_success = common.test_success
    mreport.test_sum_date = str((endtime - starttime).seconds)
    mreport.app_name = appbase[0]
    mreport.app_size = appbase[1]
    mreport.phone_name = g_phone[0]["phone_name"] +" " +g_phone[0]["phone_model"]
    mreport.phone_rel = g_phone[0]["release"]
    mreport.phone_pix = g_phone[3]
    mreport.phone_raw = phone_raws(raw)
    print(common.MEN)
    # max_men = [math.ceil((common.MEN[i])) for i in range(len(common.MEN))]  # 获取每次占用内存多少
    avg_men = [math.ceil((common.MEN[i])/raw) for i in range(len(common.MEN))]  # 获取每次占用内存多少
    mreport.phone_avg_use_raw = phone_avg_use_raws(avg_men)
    mreport.phone_max_use_raw = phone_max_use_raws(common.MEN)
    mreport.phone_cpu = g_phone[2]
    mreport.phone_avg_use_cpu = phone_avg_use_cpus(common.CPU)
    mreport.phone_avg_max_use_cpu = phone_avg_max_use_cpus(common.CPU)
    mreport.app_version = appbase[2]
    mreport.test_date = start_test_time
    Breport.set_report(mreport)

def runnerCaseApp():
    start_test_time = getDateStr(time.localtime(), "%Y-%m-%d %H:%M %p")
    suite = unittest.TestSuite()
    starttime = datetime.datetime.now()
    suite.addTest(TestInterfaceCase.parametrize(testHome))
    # suite.addTest(TestInterfaceCase.parametrize(testHome1))
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
    # BsendEmail.send_mail(get_email())
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
