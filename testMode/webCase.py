__author__ = 'shikun'

from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType,MultiType


class GetWebCase(Model):
    element_info = StringType() # (查找类型：name/id/xpah)
    operate_type = StringType() #具体的详情,如xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id等
    find_type = StringType() # 操作类型。比如点击，下拉，拖动等等，对应common
    name = StringType()
    index = IntType()
    text = StringType()


# 用例的基本信息
class GetWebInfoCase(Model):
    test_id = StringType()
    test_intr = StringType()
    test_name = StringType()
    test_result =StringType()
    test_reason = StringType()
    test_module = StringType()
