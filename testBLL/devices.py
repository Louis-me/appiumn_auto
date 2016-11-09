__author__ = 'Administrator'
from testDAL import devices

def get_devices(MAppDevices, devices_ini="", app_path=""):
    return devices.get_devices(MAppDevices, devices_ini, app_path)
