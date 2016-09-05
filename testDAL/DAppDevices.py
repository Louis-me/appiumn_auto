__author__ = 'shikun'
# -*- coding:utf-8 -*-
import configparser

def appDevices(MAppDevices, f="D:\app\appium_study\AppDevices.ini"):
    config = configparser.ConfigParser()
    config.read(f)
    MAppDevices.deviceName = config['DEFAULT']['devices']
    MAppDevices.platformName = config["DEFAULT"]['platformName']
    MAppDevices.platformVersion = config['DEFAULT']['platformVersion']
    MAppDevices.appPackage = config['DEFAULT']['appPackage']
    # common.PACKAGE = appPackage
    MAppDevices.appActivity = config['DEFAULT']['appActivity']
    MAppDevices.Remote = config['DEFAULT']['Remote']
    MAppDevices.appiumJs = config['DEFAULT']['appiumjs']
    return MAppDevices
    # return gd
