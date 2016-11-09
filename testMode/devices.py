__author__ = 'shikun'
#获取app的信息。设备名，测试的app的包名，appium 服务器的信息
# -*- coding:utf-8 -*-

from schematics.models import Model
from schematics.types import StringType,BooleanType
class getDriver(Model):

    selenium_appium = StringType()
   # appium
    deviceName = StringType() #不能为空
    platformName = StringType()
    platformVersion = StringType()
    appPackage = StringType()
    appActivity = StringType()
    Remote = StringType()
    appiumJs = StringType()
    port = StringType()

    # selenium
    sel_remote = StringType()
    phantomjs = StringType()
    open_url = StringType()
    selenium_jar = StringType()