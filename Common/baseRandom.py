__author__ = "shikun"
import datetime
import random
#用时间生成一个唯一随机数
def get_ran_dom():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")#生成当前时间
    randomNum = random.randint(0, 100) #生成的随机整数n，其中0<=n<=100
    if randomNum <= 10:
        randomNum = str(0)+str(randomNum)
    uniqueNum = str(nowTime)+str(randomNum)
    return  uniqueNum