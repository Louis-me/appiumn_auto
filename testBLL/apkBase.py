__author__ = 'shikun'

from testDAL import apkBase

class apkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath
        self.appinfo = apkBase.ApkInfo(self.apkpath)

    def get_apk_size(self):
        return self.appinfo.get_apk_size()

    def get_apk_version(self):
        return self.appinfo.get_apk_version()

    def get_apk_name(self):
        return self.appinfo.get_apk_name()

    def get_apk_pkg(self):
        return self.appinfo.get_apk_pkg()

    def get_apk_activity(self):
        return self.appinfo.get_apk_activity()
