__author__ = 'shikun'
# -*- coding: utf-8 -*-
import subprocess
cpu = []
men = []
# flow = [[],[]]
def top_cpu(pkg_name):
    cmd = "adb shell dumpsys cpuinfo | grep " + pkg_name
    temp = []
    # cmd = "adb shell top -n %s -s cpu | grep %s$" %(str(times), pkg_name)
    top_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    # print(top_info)
    for info in top_info:
        temp.append(info.split()[2].decode()) # bytes转换为string
        # print("cpu占用:%s" %cpu)
    for i in temp:
         if i != "0%":
            cpu.append(i.split("%")[0])
    return cpu

def get_men(pkg_name):
    cmd = "adb shell  dumpsys  meminfo %s"  %(pkg_name)
    temp = []
    m = []
    men_s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for info in men_s:
        temp.append(info.split())
        # print("内存占用:%s" %men[19][1].decode()+"K")
    m.append(temp)
    for t in m:
        men.append(t[19][1].decode())
    return men

# 取到流量后可以用步骤后的流量减去步骤前的流量得到步骤消耗流量！也可以用时间差来计算！
# def getFlow(pid="31586"):
#     flow_info = os.popen("adb shell cat /proc/"+pid+"/net/dev").readlines()
#     t = []
#     for info in flow_info:
#         temp_list = info.split()
#         t.append(temp_list)
#     flow[0].append(ceil(int(t[6][1])/1024)) # 下载
#     flow[1].append(ceil(int(t[6][9])/1024)) # 发送
#     return flow
