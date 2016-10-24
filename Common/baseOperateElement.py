__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from Common.CoGlobal import *
import time
from Common import errorLog

# 此脚本主要用于查找元素是否存在，操作页面元素
class getOperateElement():
    def __init__(self, driver=""):
        self.cts = driver
    def findElement(self, mOperate):
        '''
        查找元素
        :param elemt_by:   查找类型,id,xpath等
        :param element_info: 具体元素参数，如xpath的值，id的值
        :return:
        '''


        try:
            WebDriverWait(self.cts, common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.cts))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("找不到数据")
            return False

        # if mOperate["type"] == common.FIND_NAME_INDEX:
        #     find_str(mOperate["elemt_by"], self.cts, mOperate["element_info"], mOperate["text"])


    def operate_element(self,  mOperate):
        '''
        所有的操作入口
        :param operate: 操作对应common中的click,tap等
        :param elemen_by: 对应common中的id,xpath,name等
        :param element_info: 详细的元素，如xpath的格式，如id,name的名字
        :param arg: 扩展字段传list
        :param kwargs: 主要传dict
        :return:
        '''
        if self.findElement(mOperate):
            elements = {
                common.CLICK: lambda: operate_click(mOperate, self.cts),
                # common.TAP: lambda: operate_tap(mOperate["find_type"], self.cts,  mOperate["element_info"], arg),
                common.SEND_KEYS: lambda: send_keys(mOperate, self.cts),
                common.SWIPELEFT: lambda : opreate_swipe_left(mOperate, self.cts)

            }
            return elements[mOperate["operate_type"]]()
        return False

# 点击事件
def operate_click(mOperate,cts):
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_name or mOperate["find_type"] == common.find_element_by_xpath:
        elements_by(mOperate, cts).click()
    if mOperate["find_type"] == common.find_elements_by_id or mOperate["find_type"] == common.find_elements_by_name:
        elements_by(mOperate, cts)[mOperate["index"]].click()

    # errorLog.get_error(log=r"d:\operate_log.txt")

def opreate_swipe_left(mOperate, cts):
    time.sleep(2)
    width = cts.get_window_size()["width"]
    height = cts.get_window_size()["height"]
    for i in range(mOperate["time"]):
        cts.swipe(width/4*3, height / 2, width / 4 *1, height / 2, 500)
        time.sleep(2)
# start_x,start_y,end_x,end_y

# 轻打x轴向右移动x单位，y轴向下移动y单位
# def operate_tap(elemen_by,cts,element_info, xy=[]):
#     elements_by(elemen_by, cts, element_info).tap(x=xy[0], y=xy[1])

def send_keys(mOperate,cts):
    elements_by(mOperate, cts).send_keys(mOperate["text"])

# # common.FIND_STR: lambda: find_str(elements_by, kwargs["msg"])
# def find_str(elements_by,cts,element_info, msg):
#    # return ex_str.find(msg)
#    result = elements_by(elements_by, cts, element_info).text().find(msg)
#    return result



# 封装常用的标签
def elements_by(mOperate, cts):
    elements = {

        common.find_element_by_id : lambda :cts.find_element_by_id(mOperate["element_info"]),
        common.find_elements_by_id : lambda :cts.find_elements_by_id(mOperate["element_info"]),
        common.find_element_by_xpath: lambda :cts.find_element_by_xpath(mOperate["element_info"]),
        common.find_element_by_name: lambda :cts.find_element_by_name(mOperate['name']),
        common.find_elements_by_name: lambda :cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        common.find_element_by_class_name: lambda :cts.find_element_by_class_name(mOperate['element_info']),
        common.find_elements_by_class_name: lambda :cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    }
    return elements[mOperate["find_type"]]()
