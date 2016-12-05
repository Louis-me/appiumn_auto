__author__ = 'shikun'
import xlsxwriter
from common.variable import GetVariable as gv
class OperateReport:
    def __init__(self, wd, data):
        self.wd = wd
        self.data = data
    def init(self, worksheet):
         # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)


        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        worksheet.merge_range('A1:E1', '测试报告总概况', define_format_H1)
        worksheet.merge_range('A2:E2', '测试概括', define_format_H2)

        _write_center(worksheet, "A3", 'APP名称', self.wd)
        _write_center(worksheet, "A4", 'APP大小', self.wd)
        _write_center(worksheet, "A5", 'APP版本', self.wd)
        _write_center(worksheet, "A6", '测试日期', self.wd)



        _write_center(worksheet, "B3", self.data['app_name'], self.wd)
        _write_center(worksheet, "B4", self.data['app_size'], self.wd)
        _write_center(worksheet, "B5", self.data['app_version'], self.wd)
        _write_center(worksheet, "B6", self.data['test_date'], self.wd)

        _write_center(worksheet, "C3", "用例总数", self.wd)
        _write_center(worksheet, "C4", "通过总数", self.wd)
        _write_center(worksheet, "C5", "失败总数", self.wd)
        _write_center(worksheet, "C6", "测试耗时", self.wd)



        # data1 = {"test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"}
        _write_center(worksheet, "D3", self.data['test_sum'], self.wd)
        _write_center(worksheet, "D4", self.data['test_success'], self.wd)
        _write_center(worksheet, "D5", self.data['test_failed'], self.wd)
        _write_center(worksheet, "D6", self.data['test_sum_date'], self.wd)

        _write_center(worksheet, "E3", "脚本语言", self.wd)


        worksheet.merge_range('E4:E6', 'appium+python3', get_format_center(self.wd))

        # 测试手机详情
        worksheet.merge_range('A9:J9', '测试手机详情', define_format_H2)
        worksheet.set_row(9, 30)
        worksheet.set_row(10, 30)

        _write_center(worksheet, "A10", "手机名字", self.wd)
        _write_center(worksheet, "B10", "运行内存", self.wd)
        _write_center(worksheet, "C10", "CPU", self.wd)
        _write_center(worksheet, "D10", "手机分辨率", self.wd)
        _write_center(worksheet, "E10", "内存占用均值", self.wd)
        _write_center(worksheet, "F10", "内存占用峰值", self.wd)
        _write_center(worksheet, "G10", "CPU占用均值", self.wd)
        _write_center(worksheet, "H10", "CPU占用峰值", self.wd)
        _write_center(worksheet, "I10", "FPS均值", self.wd)
        _write_center(worksheet, "J10", "FPS峰值", self.wd)
        temp = 0
        for item in self.data["init"]:
            worksheet.set_row(11+temp, 30)
            _write_center(worksheet, "A"+str(11+temp), item["phone_name"], self.wd)
            _write_center(worksheet, "B"+str(11+temp), item["phone_raw"], self.wd)
            _write_center(worksheet, "C"+str(11+temp), item["phone_cpu"], self.wd)
            _write_center(worksheet, "D"+str(11+temp), item["phone_pix"], self.wd)
            _write_center(worksheet, "E"+str(11+temp), item["phone_avg_use_raw"], self.wd)
            _write_center(worksheet, "F"+str(11+temp), item["phone_max_use_raw"], self.wd)
            _write_center(worksheet, "G"+str(11+temp), item["phone_avg_use_cpu"], self.wd)
            _write_center(worksheet, "H"+str(11+temp), item["phone_avg_max_use_cpu"], self.wd)
            _write_center(worksheet, "I"+str(11+temp), item["fps_avg"], self.wd)
            _write_center(worksheet, "J"+str(11+temp), item["fps_max"], self.wd)
            temp += 1
        # pie(self.wd, worksheet)
    def test_detail(self, worksheet):
        # 设置列行的宽高
        # worksheet.set_column("A:A", 30)
        # worksheet.set_column("B:B", 20)
        # worksheet.set_column("C:C", 20)
        # worksheet.set_column("D:D", 20)
        # worksheet.set_column("E:E", 20)
        # worksheet.set_column("F:F", 20)
        # worksheet.set_column("G:G", 20)
        # worksheet.set_column("H:H", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        # worksheet.set_row(3, 30)
        # worksheet.set_row(4, 30)
        # worksheet.set_row(5, 30)
        # worksheet.set_row(6, 30)
        # worksheet.set_row(7, 30)



        worksheet.merge_range('A1:O1', '测试详情', get_format(self.wd, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#ffffff'}))
        _write_center(worksheet, "A2", '机型', self.wd)
        _write_center(worksheet, "B2", '用例ID', self.wd)
        _write_center(worksheet, "C2", '模块', self.wd)
        _write_center(worksheet, "D2", '用例介绍', self.wd)
        _write_center(worksheet, "E2", '用例名字', self.wd)
        _write_center(worksheet, "F2", '内存峰值(M)', self.wd)
        _write_center(worksheet, "G2", '内存均值(M)', self.wd)
        _write_center(worksheet, "H2", 'CPU峰值', self.wd)
        _write_center(worksheet, "I2", 'CPU均值', self.wd)
        _write_center(worksheet, "J2", 'FPS峰值', self.wd)
        _write_center(worksheet, "K2", 'FPS均值', self.wd)
        _write_center(worksheet, "L2", '测试结果 ', self.wd)
        _write_center(worksheet, "M2", '失败原因', self.wd)
        _write_center(worksheet, "N2", '截图', self.wd)
        _write_center(worksheet, "O2", '日志', self.wd)


        # data = {"info": [{"test_id": "1001", "test_name": "登陆", "t_method": "post", "t_url": "http://XXX?login", "t_param": "{user_name:test,pwd:111111}",
        #                   "t_hope": "{code:1,msg:登陆成功}", "t_actual": "{code:0,msg:密码错误}", "test_result": "失败"}, {"test_id": "1002", "test_name": "商品列表", "t_method": "get", "t_url": "http://XXX?getFoodList", "t_param": "{}",
        #                   "t_hope": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "t_actual": "{code:1,msg:成功,info:[{name:123,detal:dfadfa,img:product/1.png},{name:456,detal:dfadfa,img:product/1.png}]}", "test_result": "成功"}],
        #         "test_sum" 100,"test_success": 20, "test_failed": 80}
        temp = 3
        for item in self.data["info"]:
            _write_center(worksheet, "A"+str(temp), item["test_phone_name"], self.wd)
            _write_center(worksheet, "B"+str(temp), item["test_id"], self.wd)
            _write_center(worksheet, "C"+str(temp), item["test_module"], self.wd)
            _write_center(worksheet, "D"+str(temp), item["test_intr"], self.wd)
            _write_center(worksheet, "E"+str(temp), item["test_name"], self.wd)
            _write_center(worksheet, "F"+str(temp), item["test_men_max"], self.wd)
            _write_center(worksheet, "G"+str(temp), item["test_men_avg"], self.wd)
            _write_center(worksheet, "H"+str(temp), item["test_cpu_max"], self.wd)
            _write_center(worksheet, "I"+str(temp), item["test_cpu_avg"], self.wd)
            _write_center(worksheet, "J"+str(temp), item["test_fps_max"], self.wd)
            _write_center(worksheet, "K"+str(temp), item["test_fps_avg"], self.wd)
            _write_center(worksheet, "L"+str(temp), item["test_result"], self.wd)
            _write_center(worksheet, "M"+str(temp), item["test_reason"], self.wd)
            if item["test_image"]== None:
                _write_center(worksheet, "N" + str(temp), "", self.wd)
            else:
                worksheet.insert_image('N' + str(temp), item["test_image"], {'x_scale': 0.1, 'y_scale': 0.1,'border':1})
                worksheet.set_row(temp-1, 110)
            if item["test_log"]!= None:
                worksheet.write_url('O'+str(temp),item["test_log"], get_format(self.wd, {'bold': True,'underline':  1,'valign': 'vcenter', 'border':1}), "下载日志")
            else:
                _write_center(worksheet, "O" + str(temp), "", self.wd)
            if item["test_image"] != None:
                worksheet.set_row(temp, 30)
            temp = temp + 1

    def close(self):
        self.wd.close()
def get_format(wd, option={}):
    return wd.add_format(option)
# def link_format(wd):
#     red_format = wd.add_format({
#         'font_color': 'red',
#         'bold': 1,
#         'underline': 1,
#         'font_size': 12,
#     })
def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))
def set_row(worksheet, num, height):
    worksheet.set_row(num, height)

 # 生成饼形图
# def pie(workbook, worksheet):
#     chart1 = workbook.add_chart({'type': 'pie'})
#     chart1.add_series({
#     'name':       '接口测试统计',
#     'categories':'=测试总况!$D$4:$D$5',
#    'values':    '=测试总况!$E$4:$E$5',
#     })
#     chart1.set_title({'name': '接口测试统计'})
#     chart1.set_style(10)
#     worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

if __name__ == '__main__':
    data ={'test_date': '2016-12-01 15:58 PM', 'test_failed': 1,
 'info': [{'test_men_avg': '8%', 'test_cpu_avg': '0%', 'test_fps_avg': '0.00', 'test_name': 'test_home_feed', 'test_cpu_max': '0.0%', 'test_intr': '闪退测试', 'test_reason': None, 'test_phone_name': 'Huawei_H60-L02_android_4.4.2', 'test_men_max': '23M', 'test_image': None, 'test_module': '闪退测试', 'test_log': None, 'test_fps_max': '0.0', 'test_id': 1001, 'test_result': '成功'}, {'test_men_avg': '4%', 'test_cpu_avg': '23%', 'test_fps_avg': '0.00', 'test_name': 'test_home_feed', 'test_cpu_max': '46.0%', 'test_intr': '闪退测试', 'test_reason': '崩溃了', 'test_phone_name': 'Huawei_H60-L02_android_4.4.2', 'test_men_max': '23M', 'test_image': None, 'test_module': '闪退测试', 'test_log': 'd://storage/emulated/0/crash/2016-12-01-15-58-48.log', 'test_fps_max': '0.0', 'test_id': 1001, 'test_result': '失败'}],
 'test_sum_date': '24秒', 'app_name': "'monkneyTest'", 'test_success': 2, 'app_size': '0M',
 'init': [{'phone_avg_use_raw': '8%', 'phone_pix': ' 1080x1920\n', 'phone_avg_use_cpu': '0%', 'fps_avg': '0.00', 'fps_max': '0.0', 'phone_raw': '3014M', 'phone_name': 'Huawei_H60-L02_android_4.4.2', 'phone_avg_max_use_cpu': '0.0%', 'phone_max_use_raw': '23M', 'phone_cpu': '8核'}, {'phone_name': 'Huawei_H60-L02_android_4.4.2', 'phone_pix': ' 1080x1920\n', 'phone_avg_use_cpu': '0', 'fps_avg': '0', 'fps_max': '0', 'phone_raw': '3014M', 'phone_avg_use_raw': '0', 'phone_cpu': '8核', 'phone_max_use_raw': '0', 'phone_avg_max_use_cpu': '0'}],
'test_sum': 3, 'app_version': "'1.0'"}
    workbook = xlsxwriter.Workbook('GetReport.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    bc = OperateReport(wd=workbook, data=data)
    bc.init(worksheet)
    bc.test_detail(worksheet2)
    bc.close()
    #







