__author__ = 'shikun'
from testDAL import report
class OperateReport:
    def __init__(self, wd=None, data=None):
        self.wd = wd
        self.data = data
        self.sr = report.OperateReport(self.wd, self.data)
    def init(self, worksheet):
        self.sr.init(worksheet)
    def detail(self, worksheet):
        self.sr.test_detail(worksheet)
    def close(self):
        self.sr.close()
    # def set_report(self, mreport):
    #     self.sr.set_report(mreport)