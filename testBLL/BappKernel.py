__author__ = 'Administrator'
from testDAL import DappKernel
import math
# def get_phone_kernel(log):
#     return DappKernel.get_phone_Kernel(log)
#     pix = get_app_pix()
#     men_total = get_men_total(log)
#     phone_msg = getPhoneMsg(log)
#     cpu_sum = get_cpu_kel(log)
def get_avg_raw(l_men):
    return DappKernel.get_avg_raw(l_men)

def get_men_total(log=r"d:\men.log"):
    return DappKernel.get_men_total(log)

def get_app_pix():
    return DappKernel.get_app_pix()

def getPhoneMsg(log=r"d:\msg.log"):
    return DappKernel.getPhoneMsg(log)

def get_cpu_kel(log=r"d:\cpu.log"):
    return DappKernel.get_cpu_kel(log)
