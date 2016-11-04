__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import datetime
import xlsxwriter
import time
import unittest
from Common import reportPhone
from testRunner.runner import TestInterfaceCase,ga
from testCase.Home import testHome
from testCase.work import testContact
from testCase.web.comment import testComment
from testBLL import BgetEmail
from testBLL import BtestServer
from testBLL import BAdbCommon
from testMode import Memail
from testBLL import BExcelReport
from testBLL import BappKernel
from testBLL import BAppBaseMsg
from testBLL import Breport
from testMode import Mreport
from Common.CoGlobal import *
from Common import dataToString
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_email():
    g_email = Memail.email()
    g_email.file = PATH( '../email.ini' )
    email = BgetEmail.read_email(g_email)
    return email

def get_app_basemsg(f=r"D:\app\appium_study\img\t.apk"):
    return BAppBaseMsg.apkInfo(f).get_app_basemsg()
def get_common_report(start_test_time, endtime, starttime):
    mreport = Mreport.report()

    BappK = BappKernel.getPhoneMsg()
    raw = BappKernel.get_men_total(r"d:\men.log")
    appbase = get_app_basemsg(PATH( '../img/t.apk'))
    mreport.test_sum = common.test_sum
    mreport.test_failed = common.test_failed
    mreport.test_success = common.test_success
    mreport.test_sum_date = str((endtime - starttime).seconds-6) +"秒"
    mreport.app_name = appbase[0]
    mreport.app_size = appbase[1]
    mreport.phone_name = BappK["phone_name"] +" " + BappK["phone_model"]
    mreport.phone_rel =BappK["release"]
    mreport.phone_pix = BappKernel.get_app_pix()
    mreport.phone_raw = reportPhone.phone_raw(raw/1024)

    print(common.MEN)
    avg_men = BappKernel.get_avg_raw(common.MEN)  # 获取每次占用内存多少
    mreport.phone_avg_use_raw = avg_men
    mreport.phone_max_use_raw = reportPhone.phone_max_use_raw(common.MEN)
    mreport.phone_cpu = BappKernel.get_cpu_kel()
    mreport.phone_avg_use_cpu = reportPhone.phone_avg_use_cpu(common.CPU)
    mreport.phone_avg_max_use_cpu = reportPhone.phone_avg_max_use_cpu(common.CPU)
    mreport.app_version = appbase[2]
    mreport.test_date = start_test_time
    mreport.fps_max = reportPhone.fps_max(common.FPS)
    mreport.fps_avg = reportPhone.fps_avg(common.FPS)
    Breport.set_report(mreport)

def get_common_web_report(start_test_time, endtime, starttime):
    pass

def runnerCaseWeb():
    suite = unittest.TestSuite()
    starttime = datetime.datetime.now()
    suite.addTest(TestInterfaceCase.parametrize(testComment))
    unittest.TextTestRunner(verbosity=2).run(suite)

def runnerCaseApp():

    start_test_time = dataToString.getStrTime(time.localtime(), "%Y-%m-%d %H:%M %p")
    suite = unittest.TestSuite()
    starttime = datetime.datetime.now()
    suite.addTest(TestInterfaceCase.parametrize(testHome))
    suite.addTest(TestInterfaceCase.parametrize(testContact))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.datetime.now()
    get_common_report(start_test_time, endtime, starttime)
    report()
def report():
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    print(common.RRPORT)
    bc = BExcelReport.sendReport(wd=workbook, data=common.RRPORT)
    bc.init(worksheet)
    bc.detail(worksheet2)
    bc.close()
    # BsendEmail.send_mail(get_email())

if __name__ == '__main__':
        if ga.platformName == common.ANDROID and ga.selenium_appium == common.APPIUM:
            if BAdbCommon.attached_devices():
                appium_server = BtestServer.AppiumServer(ga.appiumJs, ga.Remote,ga.selenium_appium)
                appium_server.start_server()
                while not appium_server.is_runnnig():
                    time.sleep(2)
                runnerCaseApp()
                appium_server.stop_server()
            else:
                print(u"设备不存在")
        if ga.selenium_appium == common.SELENIUM:
            appium_server = BtestServer.AppiumServer(ga.selenium_jar, ga.sel_remote, ga.selenium_appium)
            appium_server.start_server()
            while not appium_server.is_runnnig():
                time.sleep(2)
            runnerCaseWeb()
            appium_server.stop_server()
