__author__ = 'Administrator'
import math
from Common.CoGlobal import *
def phone_avg_use_cpu(cpu):
    result = ""
    if cpu:
       result = str(math.ceil(sum(cpu)/len(cpu))) + "%"
    return result
def phone_avg_use_raw(men):
    if men: return str(math.ceil(sum(men)/len(men))) + "%"
    return 0
def phone_max_use_raw(men):
    return "100KB"
    # return str(math.ceil(max(men))) + "KB"

def phone_avg_max_use_cpu(cpu):
    return  "19%"
    # return str(max(cpu)) + "%"

def phone_raw(raw):
    return str(math.ceil(raw)) + "M"

