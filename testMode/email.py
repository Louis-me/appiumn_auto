__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType, IntType
from schematics.types.compound import ListType

class GetEmail(Model):
    to_addr = ListType(StringType)
    mail_host = StringType()
    mail_user = StringType()
    mail_pass = StringType()
    port = IntType()
    headerMsg = StringType()
    attach = StringType()
    report = StringType()
    file = StringType()