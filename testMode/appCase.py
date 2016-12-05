__author__ = 'shikun'

from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType,MultiType


class GetAppCase(Model):
    element_info = StringType() # (查找类型：name/id/xpah)
    operate_type = StringType() #具体的详情,如xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id等
    msg = StringType() # 输入的内容
    find_type = StringType() # 操作类型。比如点击，下拉，拖动等等，对应common
    time = IntType() # 配合与滑动操作
    name = StringType()
    index = IntType()
    text = StringType()# 输入信息
    log = StringType() # 本地log信息路径，一般由手机名字_型号构成

# 用例的基本信息
class GetAppCaseInfo(Model):
    test_id = StringType() # 用例的id
    test_intr = StringType() # 用例的介绍
    test_name = StringType() # 用例的名字
    test_result =StringType() # 用例的结果
    test_reason = StringType() # 用例失败的理由
    test_module = StringType() # 测试的模板
    test_men_max = StringType() # 内存最大使用情况
    test_men_avg = StringType() # 内存平均使用情况
    test_cpu_max = StringType() #cpu最大使用峰值
    test_cpu_avg = StringType() #cpu 平均使用值
    test_fps_max = StringType() # fps最大峰值
    test_fps_avg = StringType() # fps平均值
    # test_devices = StringType()
    test_phone_name = StringType() #设备_手机_型号
    test_image = StringType() # 图片
    test_log = StringType() #闪退的日志
