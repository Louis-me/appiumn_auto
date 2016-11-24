# -*- coding: utf-8 -*-
import os
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
from common.variable import GetVariable as common
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
import threading
# readConfigLocal = readConfig.ReadConfig()
class AppiumServer:

    def __init__(self, l_devices):
        # openAppium = "node D:\\app\Appium\\node_modules\\appium\\bin\\appium.js"
        # baseUrl = "http://127.0.0.1:4723/wd/hub"
        # openAppium = "java -jar " + PATH("../img/selenium-server-standalone-3.0.1.jar")
        # baseUrl = "http://127.0.0.1:4444/wd/hub"
        self.l_devices = l_devices
        # self.baseUrl = baseUrl
        # self.selenium_appium = selenium_appium
    def start_server(self):
        """start the appium server
        :return:
        """
        for i in range(0, len(self.l_devices["appium"])):
            t1 = RunServer(self.l_devices["appium"][i]["config"])
            p = Process(target=t1.start())
            p.start()
        # t2 = RunServer(self.l_devices["selenium_jar"])
        # p2 = Process(target=t2.start())
        # p2.start()
    def stop_server(self):
        """stop the appium server
        selenium_appium: appium selenium
        :return:
        """
        # kill myServer
        res = ""
        # if self.selenium_appium == common.APPIUM:
        #     res = "node.exe"
        # else:
        #     res = "java.exe"
        os.system('taskkill /f /im  node.exe')
        # os.system('taskkill /f /im  java.exe')
    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        for i in range(0, len(self.l_devices["appium"])):
            url = " http://127.0.0.1:"+str(self.l_devices["appium"][i]["port"])+"/wd/hub"+"/status"
            try:
                response = urllib.request.urlopen(url, timeout=5)

                if str(response.getcode()).startswith("2"):
                    return True
                else:
                    return False
            except URLError:
                return False
            finally:
                if response:
                    response.close()
class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)


# if __name__ == "__main__":
#
#     oo = AppiumServer()
#     oo.start_server()
#     print("strart server")
#     print("running server")
#     oo.stop_server()
#     print("stop server")