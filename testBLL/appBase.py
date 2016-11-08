__author__ = 'Administrator'
from testDAL import appBase
import math
# def get_phone_kernel(log):
#     return DappKernel.get_phone_Kernel(log)
#     pix = get_app_pix()
#     men_total = get_men_total(log)
#     phone_msg = GetPhoheInfo(log)
#     cpu_sum = get_cpu_kel(log)
def get_avg_raw(l_men):
    return appBase.get_avg_raw(l_men)

def get_men_total(log=r"d:\men.log"):
    return appBase.get_men_total(log)

def get_app_pix():
    return appBase.get_app_pix()

def get_phone_info(log=r"d:\msg.log"):
    return appBase.get_phone_info(log)

def get_cpu_kel(log=r"d:\cpu.log"):
    return appBase.get_cpu_kel(log)
