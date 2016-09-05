__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType

class operateElement(Model):
    type = StringType()
    elemt_by = StringType()
    element_info = StringType()
    msg = StringType()
    operate = StringType()
    xy = ListType(IntType)