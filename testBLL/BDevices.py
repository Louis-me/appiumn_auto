__author__ = 'Administrator'
from testDAL import DDevices

def BgetDevices(MAppDevices, f):
    return DDevices.appDevices(MAppDevices, f)
