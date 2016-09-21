__author__ = 'Administrator'
import re
from Common.CoGlobal import *
import os, sys, time
import subprocess
def get_error(log="d:\log.txt"):
    # if os.path.exists(log):
    #     os.remove(log)
    subprocess.Popen("adb -d  logcat >" +log, shell=True)
    time.sleep(1)
    # with open(log, encoding="utf-8", mode="r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         if re.findall(common.ANR, line):
    #             print('\033[1;31;42m')
    #             print("存在anr错误:", line)
    #             common.I_ANR += 1
    #         if re.findall(common.CRASH, line):
    #             print('\033[1;31;42m')
    #             print("存在crash错误:", line)
    #             common.I_CRASH += 1
    #         if re.findall(common.EXCEPTION, line):
    #             print('\033[1;31;42m')
    #             print("存在EXCEPTION错误:", line)
    #             common.I_EXCEPTION += 1
    sys.exit()
def save_log(log="d:\log.txt", pack=""):
    os.system("adb logcat | grep " + pack + ">" +log)
