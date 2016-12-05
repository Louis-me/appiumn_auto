__author__ = 'shikun'
import os,time
import subprocess

def get_error(log="d:\log.txt", devices=""):
    handle = subprocess.Popen("adb -s "+devices+ "-d  logcat >" +log, shell=True)
    time.sleep(1)
    os.system("adb logcat -s "+devices+" -c")
    subprocess.Popen("taskkill /F /T /PID " + str(handle.pid) , shell=True)
    # with open(log, encoding="utf-8", mode="r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         if re.findall(GetVariable.ANR, line):
    #             print('\033[1;31;42m')
    #             print("存在anr错误:", line)
    #             GetVariable.I_ANR += 1
    #         if re.findall(GetVariable.CRASH, line):
    #             print('\033[1;31;42m')
    #             print("存在crash错误:", line)
    #             GetVariable.I_CRASH += 1
    #         if re.findall(GetVariable.EXCEPTION, line):
    #             print('\033[1;31;42m')
    #             print("存在EXCEPTION错误:", line)
    #             GetVariable.I_EXCEPTION += 1

#
# def save_log(log="d:\log.txt", pack=""):
#     os.system("adb logcat | grep " + pack + ">" +log)
