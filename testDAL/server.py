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
class AppiumServer:
    def __init__(self, l_devices):
        self.l_devices = l_devices
    def start_server(self):
        """start the appium server
        :return:
        """
        for i in range(0, len(self.l_devices["appium"])):
            t1 = RunServer(self.l_devices["appium"][i]["config"])
            p = Process(target=t1.start())
            p.start()
    def stop_server(self):
        """stop the appium server
        selenium_appium: appium selenium
        :return:
        """
        os.system('taskkill /f /im  node.exe')
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