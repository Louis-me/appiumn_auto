__author__ = 'Administrator'
from testDAL import phoneBase
def get_avg_raw(l_men, deviceName):
    return phoneBase.get_avg_raw(l_men, deviceName)

def get_men_total(log=r"d:\men.log", devices=""):
    return phoneBase.get_men_total(log, devices)

def get_app_pix(devices):
    return phoneBase.get_app_pix(devices)

def get_phone_info(log=r"d:\msg.log", devices=""):
    return phoneBase.get_phone_info(log, devices)

def get_cpu_kel(log=r"d:\cpu.log", devices=""):
    return phoneBase.get_cpu_kel(log, devices)
