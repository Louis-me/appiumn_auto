__author__ = 'Administrator'
import os
import re
import math
from math import ceil
from common.variable import GetVariable as common
# 得到手机信息
def get_phone_info(cmd_log):
    os.system('adb shell cat /system/build.prop >'+cmd_log)
    l_list = {}
    with open(cmd_log, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split('=')
            #Android 系统，如anroid 4.0
            if (line[0] == 'ro.build.version.release'):
                l_list["release"] = line[1]
                #手机名字
            if (line[0]=='ro.product.model'):
                l_list["phone_name"] = line[1]
                #手机品牌
            if (line[0]=='ro.product.brand'):
                 l_list["phone_model"] =  line[1]

    # 删除本地存储的手机信息文件
    if os.path.exists(cmd_log):
        os.remove(cmd_log)
    return l_list

def get_men_total(cmd_log):
    os.system("adb shell cat /proc/meminfo >" + cmd_log)
    men_total = ""
    with open(cmd_log, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split('=')
                if line[0]:
                    men_total = re.findall(r"\d+", line[0])[0]
                    break
    if os.path.exists(cmd_log):
        os.remove(cmd_log)
    return int(men_total)
# 得到几核cpu
def get_cpu_kel(log):
    os.system("adb shell cat /proc/cpuinfo >" + log)
    cpu_kel = 0
    with open(log, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(':')
                if line[0].find("processor") >= 0:
                   cpu_kel += 1
    if os.path.exists(log):
        os.remove(log)
    return str(cpu_kel) + "核"
# print(get_cpu_kel("d:\\men.txt"))

# 得到手机分辨率
def get_app_pix():
    result = os.popen("adb shell wm size", "r")
    return result.readline().split("Physical size:")[1]

# def get_phone_raw(log):
#     return get_phone_kernel(log)[1]
def get_avg_raw(l_men):
    if common.RAW == 0:
        common.RAW = get_men_total(r"d:\men.txt")
    # print("shikun")
    # print(l_men)
    # print(GetVariable.RAW)
    l_men = [math.ceil(((l_men[i])/common.RAW)*1024) for i in range(len(l_men))]  # 获取每次占用内存多少
    # print("l_men")
    # print(l_men)
    if len(l_men) > 0 :
            return str(math.ceil(sum(l_men)/len(l_men))) + "%"
    return 0

# def get_phone_Kernel(log):
#     pix = get_app_pix()
#     men_total = get_men_total(log)
#     phone_msg = get_phone_info(log)
#     cpu_sum = get_cpu_kel(log)
#     return phone_msg, men_total, cpu_sum, pix
