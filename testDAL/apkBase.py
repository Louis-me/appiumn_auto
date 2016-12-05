__author__ = 'shikun'
import math
from math import  floor
import subprocess
import os

class ApkInfo():
    def __init__(self, apkpath):
        self.apkpath = apkpath

# 得到app的文件大小
    def get_apk_size(self):
        size = floor(os.path.getsize(self.apkpath)/(1024*1000))
        return str(size) + "M"
    # 得到版本
    def get_apk_version(self):
        cmd = "aapt dump badging " + self.apkpath + " | grep versionName"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[3].decode()[12:]
        return result

    #得到应用名字
    def get_apk_name(self):
        cmd = "aapt dump badging " + self.apkpath + " | grep application-label: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[0].decode()[18:]
        return result

    #得到包名
    def get_apk_pkg(self):
        cmd = "aapt dump badging " + self.apkpath + " | grep package:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result

    #得到启动类
    def get_apk_activity(self):
        cmd = "aapt dump badging " + self.apkpath + " | grep launchable-activity:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result
if __name__ == '__main__':
    ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_pkg()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_version()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_name()
    ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()


