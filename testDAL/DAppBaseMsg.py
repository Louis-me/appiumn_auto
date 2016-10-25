__author__ = 'Administrator'
from math import  floor
import subprocess
import os

class apkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath

# 得到app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkpath)/(1024*1000))
        return str(size) + "M"
    # 得到版本
    def get_apk_version(self, pag):
        cmd = "aapt dump badging " + self.apkpath + " | grep " + pag
        return self.get_apk_info(cmd, 62, -30)

    #得到应用名字
    def get_apk_name(self):
        cmd = "aapt dump badging " + self.apkpath + " | grep application-label:"
        return self.get_apk_info(cmd, 19, -2)

    # 得到app的详细信息
    def get_apk_info(self, commond,start, end):
        result = ""
        p = subprocess.Popen(commond, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE,shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output[start:end]
        return result.decode()

    def get_app_basemsg(self):
        apk_name = self.get_apk_name() # app名字
        apk_siz = self.get_apk_size() # app大小
        apk_version = self.get_apk_version("versionName") # app版本
        # print(apk_version)
        return apk_name, apk_siz, apk_version

# COMMOND1 = "aapt dump badging "
# COMMOND2 = " | grep application-label:"
# COMMOND3 = " | grep package"
# apk_path = "zhishang.apk"
# commond1 = COMMOND1+apk_path+COMMOND3
# commond2 = COMMOND1+apk_path+COMMOND2
#
# apkInfo(r"D:\app\appium_study\img\t.apk").get_app_basemsg() # 版本
# # get_apk_info(commond, 62, -30) 大小
# # get_apk_info(commond2, 19, -2) #项目名称

