__author__ = 'shikun'
# -*- coding:utf-8 -*-
import configparser
from common.variable import GetVariable as common
from testDAL import phoneBase
from testDAL import apkBase


def get_devices(MAppDevices, devices_ini="D:\\app\\appium_study\\devices.ini", app_path=""):
    config = configparser.ConfigParser()
    config.read(devices_ini)

    MAppDevices.selenium_appium = config['DEFAULT']["selenium_appium"]
    if config['DEFAULT']["selenium_appium"] == common.APPIUM: # appium
        ab = apkBase.ApkInfo(app_path)
        phone_msg = phoneBase.get_phone_info("d:\\log.txt", config[common.APPIUM]['devices'])

        MAppDevices.deviceName = config[common.APPIUM]['devices']
        MAppDevices.platformName = common.ANDROID
        MAppDevices.platformVersion = phone_msg["release"]
        MAppDevices.appPackage = ab.get_apk_pkg()
        MAppDevices.appActivity = ab.get_apk_activity().strip()
        MAppDevices.Remote = "http://"+config[common.APPIUM]['Remote'] + ":" + config[common.APPIUM]['port'] + "/wd/hub"
        MAppDevices.appiumJs = config[common.APPIUM]['appiumjs']

    if config['DEFAULT']["selenium_appium"] == common.SELENIUM:# selenium
        MAppDevices.selenium_appium = config[common.SELENIUM]['selenium_appium']
        MAppDevices.sel_remote = config[common.SELENIUM]['sel_remote']
        MAppDevices.selenium_jar = config[common.SELENIUM]['selenium_jar']
        MAppDevices.open_url = config[common.SELENIUM]['open_url']
    return MAppDevices
