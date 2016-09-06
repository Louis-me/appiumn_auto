__author__ = 'Administrator'
from Common.CoGlobal import *

def set_report(mreport):
    common.RRPORT["test_sum"] = mreport.test_sum
    common.RRPORT["test_failed"] = mreport.test_failed
    common.RRPORT["test_success"] = mreport.test_success
    common.RRPORT["test_sum_date"] = mreport.test_sum_date
    common.RRPORT["app_name"] = mreport.app_name
    common.RRPORT["app_size"] = mreport.app_size
    common.RRPORT["phone_name"] = mreport.phone_name
    common.RRPORT["phone_rel"] = mreport.phone_rel
    common.RRPORT["phone_pix"] = mreport.phone_pix
    common.RRPORT["phone_raw"] = mreport.phone_raw
    common.RRPORT["phone_avg_use_raw"] = mreport.phone_avg_use_raw
    common.RRPORT["phone_max_use_raw"] = mreport.phone_max_use_raw
    common.RRPORT["phone_cpu"] = mreport.phone_cpu
    common.RRPORT["phone_avg_use_cpu"] = mreport.phone_avg_use_cpu
    common.RRPORT["phone_avg_max_use_cpu"] = mreport.phone_avg_max_use_cpu
    common.RRPORT["app_version"] = mreport.app_version
    common.RRPORT["test_date"] = mreport.test_date