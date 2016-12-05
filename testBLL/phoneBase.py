__author__ = 'shikun'
from testDAL import phoneBase
def get_avg_raw(l_men, deviceName):
    return phoneBase.get_avg_raw(l_men, deviceName)

def get_men_total(devices=""):
    return phoneBase.get_men_total(devices)

def get_app_pix(devices):
    return phoneBase.get_app_pix(devices)

def get_phone_info(devices=""):
    return phoneBase.get_phone_info(devices)

def get_cpu_kel(devices=""):
    return phoneBase.get_cpu_kel(devices)
