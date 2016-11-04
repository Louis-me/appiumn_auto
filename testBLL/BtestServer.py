__author__ = 'Administrator'
from testDAL import DtestServer

# 控制appium的服务
class AppiumServer():
    def __init__(self, openAppium, baseUrl, selenium_appium):
        self.openAppium = openAppium
        self.baseUrl = baseUrl
        self.selenium_appium = selenium_appium
        self.server = DtestServer.AppiumServer(self.openAppium, self.baseUrl, self.selenium_appium)
    def start_server(self):
        self.server.start_server()
    def stop_server(self):
        self.server.stop_server()
    def is_runnnig(self):
        return self.server.is_runnnig()