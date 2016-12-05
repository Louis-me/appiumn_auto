__author__ = 'shikun'
import time
def getStrTime(t_time, format):
    # time.strftime("%Y-%m-%d %I%p %M:%S 今天是当年第%j天  当年第%U周  星期%w",time.localtime())
    # time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return time.strftime(format, t_time)