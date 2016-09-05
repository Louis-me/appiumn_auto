__author__ = 'Administrator'
from testDAL import DAdbCommon

def attached_devices():
   return DAdbCommon.AndroidDebugBridge().attached_devices()

def open_app(packagename, activity):
    return DAdbCommon.AndroidDebugBridge().open_app(packagename, activity)