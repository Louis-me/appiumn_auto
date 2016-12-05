__author__ = 'shikun'
from testDAL import adbCommon

def attached_devices():
   return adbCommon.AndroidDebugBridge().attached_devices()

def open_app(packagename, activity):
    return adbCommon.AndroidDebugBridge().open_app(packagename, activity)