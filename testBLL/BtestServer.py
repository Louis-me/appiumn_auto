__author__ = 'Administrator'
from testDAL import DtestServer

# 控制appium的服务
class AppiumServer():
    def __init__(self, openAppium, baseUrl):
        self.openAppium = openAppium
        self.baseUrl = baseUrl
        self.appium = DtestServer.AppiumServer(self.openAppium, self.baseUrl)
    def start_server(self):
        self.appium.start_server()
    def stop_server(self):
        self.appium.stop_server()
    def is_runnnig(self):
        return self.appium.is_runnnig()