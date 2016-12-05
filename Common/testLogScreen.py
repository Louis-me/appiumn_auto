import os
import time
def screenshotNG(caseName, driver, resultPath):
    # resultPath = "d:\\appium"
    logPath = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # screenshotPath = os.path.join(logPath, caseName)
    screenshotName = "CheckPoint_NG.png"
    screen_img = resultPath+caseName+"_"+logPath +"_"+screenshotName
    # screen_img = os.path.join(screenshotPath, screenshotName)
    driver.get_screenshot_as_file(screen_img)
    return screen_img
