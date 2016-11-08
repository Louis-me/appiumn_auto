__author__ = 'Administrator'

from testDAL import apkBase

class apkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath
        self.appinfo = apkBase.ApkInfo(self.apkpath)
    def get_app_msg(self):
        return self.appinfo.get_app_msg()

