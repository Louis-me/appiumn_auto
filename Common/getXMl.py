__author__ = 'Administrator'
import yaml
# -*- coding:utf-8 -*-
def getYam(homeyaml):
    print(homeyaml)
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            print(x)
            return x
    except FileNotFoundError:
        print(u"找不到测试用例文件")
