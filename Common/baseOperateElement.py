__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from Common.CoGlobal import *
from Common import errorLog

# 此脚本主要用于查找元素是否存在，操作页面元素
class getOperateElement():
    def __init__(self, driver=""):
        self.cts = driver
    # def findElement(self, elemt_by, element_info,msg=None):
    def findElement(self, **kwargs):
        '''
        查找元素
        :param elemt_by:   查找类型,id,xpath等
        :param element_info: 具体元素参数，如xpath的值，id的值
        :return:
        '''
        if kwargs["type"] == common.FIND:
            errorLog.get_error(log="d:\log.txt")
            try:
                WebDriverWait(self.cts, 10).until(lambda x: elements_by(kwargs["elemt_by"], self.cts, kwargs["element_info"]))
                return True
            except selenium.common.exceptions.TimeoutException:
                return False
            except selenium.common.exceptions.NoSuchElementException:
                print("找不到数据")
                return False
        if kwargs["type"] == common.FIND_STR:
            find_str(kwargs["elemt_by"], self.cts, kwargs["element_info"], kwargs["msg"])


    def operate_element(self, operate, elemen_by, element_info, *arg, **kwargs):
        '''
        所有的操作入口
        :param operate: 操作对应common中的click,tap等
        :param elemen_by: 对应common中的id,xpath,name等
        :param element_info: 详细的元素，如xpath的格式，如id,name的名字
        :param arg: 扩展字段传list
        :param kwargs: 主要传dict
        :return:
        '''
        elements = {
            common.CLICK: lambda: operate_click(elemen_by, self.cts, element_info),
            common.TAP: lambda: operate_tap(elemen_by, self.cts, element_info, arg),
            common.SEND_KEYS: lambda: send_keys(elemen_by, self.cts, element_info, kwargs)
        }
        # 监控性能信息

        return elements[operate]()

# 点击事件
def operate_click(elemen_by,cts,element_info):
    elements_by(elemen_by, cts, element_info).click()
    errorLog.get_error(log="d:\log.txt")

# 轻打x轴向右移动x单位，y轴向下移动y单位
def operate_tap(elemen_by,cts,element_info, xy=[]):
    elements_by(elemen_by, cts, element_info).tap(x=xy[0], y=xy[1])

def send_keys(elemen_by,cts,element_info, kwargs):

    elements_by(elemen_by, cts, element_info).send_keys(kwargs["msg"])

# common.FIND_STR: lambda: find_str(elements_by, kwargs["msg"])
def find_str(elements_by,cts,element_info, msg):
   # return ex_str.find(msg)
   result = elements_by(elements_by, cts, element_info).text().find(msg)
   return result

# 封装常用的find标签
def elements_by(types, cts, element_info, msg=None):
    elements = {
        common.ID : lambda :cts.find_element_by_id(element_info),
        common.XPATH: lambda :cts.find_element_by_xpath(element_info),
        common.NAME: lambda :cts.find_element_by_name(msg)
    }
    return elements[types]()
