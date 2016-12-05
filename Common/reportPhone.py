__author__ = 'shikun'
import math
from common.variable import GetVariable as common
def phone_avg_use_cpu(cpu):
    print("phone_avg_use_cpu1")
    print(cpu)
    result = ""
    try:
        if len(cpu) > 0:
           result = str(math.ceil(sum(cpu)/len(cpu))) + "%"
        return result
    except:
        return result
def phone_avg_use_raw(men):
    print("phone_avg_use_raw1")
    print(men)
    try:
        if len(men) > 0 :
            return str(math.ceil(sum(men)/len(men))) + "%"
        return 0
    except:
        return  0
def phone_max_use_raw(l_men):
    print("phone_max_use_raw1")
    print(l_men)
    if len(l_men) > 0:
        return str(math.ceil((max(l_men))/1024)) + "M"
    return "0"


def phone_avg_max_use_cpu(cpu):
    print("phone_avg_max_use_cpu1")
    print(cpu)
    try:
        if len(cpu):
            return str(max(cpu)) + "%"
        return "0"
    except :
        return "0"
def phone_raw(raw):
    if raw > 0:
        return str(math.ceil(raw)) + "M"
    return "0"

def fps_max(d_fps):
    print("fps_max1")
    print(d_fps)
    if len(d_fps) > 0:
        return str(max(d_fps))
    return "0"
def fps_avg(d_fps):
    print("fps_avg1")
    print(d_fps)
    result = 0
    if len(d_fps) > 0:
        result = float(str(math.ceil(sum(d_fps)/len(d_fps))))
        return '%.2f' % result
    return result


