__author__ = 'Administrator'
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import datetime
import xlsxwriter
import time
import unittest
from common import reportPhone
from testRunner.runnerBase import TestInterfaceCase, ga
from testCase.Home import testHome
from testCase.work import testContact
from testCase.web.comment import testComment
from testBLL import email as b_email
from testBLL import server
from testBLL import adbCommon
from testMode import email as memail
from testBLL import report as b_report
from testBLL import appBase
from testBLL import apkBase
from testMode import report as m_report
from common.variable import GetVariable as common
from common import dataToString
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_email():
    m_email = memail.GetEmail()
    m_email.file = PATH( '../email.ini' )
    email = b_email.read_email(m_email)
    return email

def get_app_msg(f=r"D:\app\appium_study\img\t.apk"):
    return apkBase.apkInfo(f).get_app_msg()
def get_common_report(start_test_time, endtime, starttime):
    mreport = m_report.GetReport()

    b_get_hp_info = appBase.get_phone_info()
    raw = appBase.get_men_total(r"d:\men.log")
    app_msg = get_app_msg(PATH( '../img/t.apk'))
    mreport.test_sum = common.test_sum
    mreport.test_failed = common.test_failed
    mreport.test_success = common.test_success
    mreport.test_sum_date = str((endtime - starttime).seconds-6) +"秒"
    mreport.app_name = app_msg[0]
    mreport.app_size = app_msg[1]
    mreport.phone_name = b_get_hp_info["phone_name"] +" " + b_get_hp_info["phone_model"]
    mreport.phone_rel =b_get_hp_info["release"]
    mreport.phone_pix = appBase.get_app_pix()
    mreport.phone_raw = reportPhone.phone_raw(raw/1024)

    print(common.MEN)
    avg_men = appBase.get_avg_raw(common.MEN)  # 获取每次占用内存多少
    mreport.phone_avg_use_raw = avg_men
    mreport.phone_max_use_raw = reportPhone.phone_max_use_raw(common.MEN)
    mreport.phone_cpu = appBase.get_cpu_kel()
    mreport.phone_avg_use_cpu = reportPhone.phone_avg_use_cpu(common.CPU)
    mreport.phone_avg_max_use_cpu = reportPhone.phone_avg_max_use_cpu(common.CPU)
    mreport.app_version = app_msg[2]
    mreport.test_date = start_test_time
    mreport.fps_max = reportPhone.fps_max(common.FPS)
    mreport.fps_avg = reportPhone.fps_avg(common.FPS)
    b_report.OperateReport().set_report(mreport)

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
    workbook = xlsxwriter.Workbook('GetReport.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    print(common.RRPORT)
    b_OperateReport = b_report.OperateReport(wd=workbook, data=common.RRPORT)
    b_OperateReport.init(worksheet)
    b_OperateReport.detail(worksheet2)
    b_OperateReport.close()
    b_email.send_mail(get_email())

if __name__ == '__main__':
        if ga.selenium_appium == common.APPIUM and ga.platformName == common.ANDROID :
            if adbCommon.attached_devices():
                appium_server = server.AppiumServer(ga.appiumJs, ga.Remote,ga.selenium_appium)
                appium_server.start_server()
                while not appium_server.is_runnnig():
                    time.sleep(2)
                runnerCaseApp()
                appium_server.stop_server()
            else:
                print(u"设备不存在")
        if ga.selenium_appium == common.SELENIUM:
            appium_server = server.AppiumServer(ga.selenium_jar, ga.sel_remote, ga.selenium_appium)
            appium_server.start_server()
            while not appium_server.is_runnnig():
                time.sleep(2)
            runnerCaseWeb()
            appium_server.stop_server()
