__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType,MultiType


class getReport(object):
    # test_failed = IntType()
    # test_sum = IntType()
    # test_error = IntType()
    # test_module = StringType()
    # test_success = IntType()
    # info = ListType(MultiType)
    def __init__(self):
        self.test_failed = 0
        self.test_sum = 0
        self.test_error = 0
        self.test_module = "模块"
        self.test_success = 0
        self.info = []
    def set_test_failed(self, test_failed):
        self.test_failed = test_failed
    def get_test_failed(self):
        return self.test_failed
    def set_test_sum(self, test_sum):
        self.test_sum = test_sum
    def get_test_sum(self):
        return self.test_sum
    def set_test_error(self, test_error):
        self.test_error = test_error
    def get_test_error(self):
        return self.test_error
    def set_test_module(self, test_module):
        self.test_module = test_module
    def get_test_module(self):
        return self.test_module
    def set_test_success(self, test_success):
        self.test_success = test_success
    def get_test_success(self):
        return self.test_success
    def set_info(self, info):
        self.info.append(info)
    def get_info(self):
        return self.info