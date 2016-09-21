__author__ = 'Administrator'

from testDAL import DAppBaseMsg

class apkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath
        self.appinfo = DAppBaseMsg.apkInfo(self.apkpath)
    def get_app_basemsg(self, apg):
        return self.appinfo.get_app_basemsg(apg)

