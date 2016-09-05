__author__ = 'Administrator'

from testDAL import DAppBaseMsg

class apkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath
        self.appinfo = DAppBaseMsg.apkInfo(self.apkpath)
    def get_apk_size(self):
       return self.appinfo.get_apk_size()
    def get_apk_version(self):
        return self.appinfo.get_apk_version()
    def get_apk_name(self):
        return self.appinfo.get_apk_name()

