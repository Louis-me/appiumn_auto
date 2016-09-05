__author__ = 'Administrator'
from testDAL import DExcelReport
class sendReport:
    def __init__(self, wd, data):
        self.wd = wd
        self.data = data
        self.sr = DExcelReport.sendReport(self.wd, self.data)
    def init(self, worksheet):
        self.sr.init(worksheet)
    def detail(self, worksheet):
        self.sr.test_detail(worksheet)
    def close(self):
        self.sr.close()
