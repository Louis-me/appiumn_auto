__author__ = 'shikun'
import yaml
import os
import sys

from testBLL import phoneBase


# -*- coding:utf-8 -*-
def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            print(x)
            return x
    except FileNotFoundError:
        print(u"找不到文件")


