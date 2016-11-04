__author__ = 'shikun'
# -*- coding:utf-8 -*-
import configparser
from Common.CoGlobal import *
def appDevices(MAppDevices, f="D:\\app\\appium_study\\Devices.ini"):
    config = configparser.ConfigParser()
    config.read(f)
    MAppDevices.selenium_appium = config['DEFAULT']["selenium_appium"]
    if config['DEFAULT']["selenium_appium"] == common.APPIUM: # appium
        MAppDevices.deviceName = config[common.APPIUM]['devices']
        MAppDevices.platformName = config[common.APPIUM]['platformName']
        MAppDevices.platformVersion = config[common.APPIUM]['platformVersion']
        MAppDevices.appPackage = config[common.APPIUM]['appPackage']
        MAppDevices.appActivity = config[common.APPIUM]['appActivity']
        MAppDevices.Remote = config[common.APPIUM]['Remote']
        MAppDevices.appiumJs = config[common.APPIUM]['appiumjs']
    if config['DEFAULT']["selenium_appium"] == common.SELENIUM:# selenium
        MAppDevices.selenium_appium = config[common.SELENIUM]['selenium_appium']
        MAppDevices.sel_remote = config[common.SELENIUM]['sel_remote']
        MAppDevices.selenium_jar = config[common.SELENIUM]['selenium_jar']
        MAppDevices.open_url = config[common.SELENIUM]['open_url']
    return MAppDevices
