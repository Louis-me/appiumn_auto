__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType, IntType

class report(Model):
    test_sum = IntType() # 总用例数
    test_failed = IntType() # 失败总数
    test_success = IntType() # 错误总数
    test_sum_date = StringType() # 测试总花费时间
    app_name = StringType() #app名字
    app_size = StringType() # app大小
    phone_name = StringType() # 手机名字
    phone_rel = StringType() # 手机型号
    phone_pix = StringType() # 手机分辨率
    phone_raw = IntType() #手机运行内存
    phone_model = StringType() # 手机型号
    phone_avg_use_raw = StringType() # 平均使用内存
    phone_max_use_raw = StringType() # 最大使用内存情况
    phone_cpu = StringType() # c几核pu信息
    phone_avg_use_cpu = StringType() #cpu平均使用情况
    phone_avg_max_use_cpu = StringType() # cpu最大使用情况
    app_version = StringType() # app的版本
    test_date = StringType() # 测试的日期
