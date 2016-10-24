__author__ = 'shikun'

import logging
import time
import os
from time import sleep
import threading

class Log:

    def __init__(self):

        global logger, resultPath, logPath
        resultPath ="d:\\appium"
        logPath = os.path.join(resultPath, (time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if os.path.exists(logPath) == False:
            os.makedirs(logPath)
        self.checkNo = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        #create handler,write log
        fh = logging.FileHandler(os.path.join(logPath, "outPut.log" ))
        #Define the output format of formatter handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def getMyLogger(self):
        """get the logger
        :return:logger
        """
        return self.logger

    def buildStartLine(self, caseNo):
        """build the start log
        :param caseNo:
        :return:
        """

        startLine = "----  " + caseNo + "   " + "START" + "   " +\
        "  ----"
        self.logger.info(startLine)

    def buildEndLine(self, caseNo):
        """build the end log
        :param caseNo:
        :return:
        """
        endLine = "----  " + caseNo + "   " + "END" + "   " +\
        "  ----"
        self.logger.info(endLine)
        self.checkNo = 0

    def writeResult(self, result):
        """write the case result(OK or NG)
        :param result:
        :return:
        """
        reportPath = os.path.join(logPath, "report.txt")
        flogging = open(reportPath, "a")
        try:
            flogging.write(result+"\n")
        finally:
            flogging.close()
        pass

    def resultOK(self, caseNo):
        self.writeResult(caseNo+": OK")

    def resultNG(self, caseNo, reason):
        self.writeResult(caseNo+": NG--" + reason)

    def checkPointOK(self, driver,caseName, checkPoint):
        """write the case's checkPoint(OK)
        :param driver:
        :param caseName:
        :param checkPoint:
        :return:
        """
        self.checkNo += 1

        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+checkPoint+": OK")

        # take shot
        self.screenshotOK(driver, caseName)

    def checkPointNG(self, driver,caseName, checkPoint):
        """write the case's checkPoint(NG)
        :param driver:
        :param caseName:
        :param checkPoint:
        :return:
        """
        self.checkNo += 1

        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+checkPoint+": NG")

        # take shot
        self.screenshotNG(driver, caseName)

    def screenshotOK(self, driver, caseName):
        """screen shot
        :param driver:
        :param caseName:
        :return:
        """
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_"+str(self.checkNo)+"_OK.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        # driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))
        driver.get_screenshot_as_file(os.path.join(screenshotPath+screenshotName))

    def screenshotNG(self, driver, caseName):
        """screen shot
        :param driver:
        :param caseName:
        :return:
        """
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_"+str(self.checkNo)+"_NG.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath+screenshotName))

    def screenshotERROR(self, driver, caseName):
        """screen shot
        :param driver:
        :param caseName:
        :return:
        """
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "ERROR.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))


class myLog:
    """
    This class is used to get log
    """

    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def getLog():

        if myLog.log == None:

            myLog.mutex.acquire()
            myLog.log = Log()
            myLog.mutex.release()

        return myLog.log

# if __name__ == "__main__":
#     logTest = myLog.getLog()
#     logger = logTest.getMyLogger()
#     logger.debug("1111")
#     logTest.buildStartLine("test")





