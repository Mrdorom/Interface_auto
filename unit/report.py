# coding:utf-8


class SetStyle(object):
    def __init__(self, wd, data):
        self.wd = wd
        self.data = data

    def test_detail(self, worksheet):
        worksheet.set_row(1, height=30)
        worksheet.set_row(2, height=30)
        worksheet.set_column("B:B", 15)
        worksheet.set_column("C:C", 15)
        worksheet.set_column("D:D", 15)
        worksheet.set_column("E:E", 15)
        worksheet.set_column("F:F", 15)
        worksheet.set_column("G:G", 15)

        worksheet.merge_range('A1:J1', '接口测试详情', get_format(self.wd, {'bold': True, 'font_size': 18, 'align': 'center',
                                                                    'valign': 'vcenter', 'bg_color': 'blue',
                                                                    'font_color': '#ffffff'}))

        _write_center(worksheet, "A2", "用例名称", self.wd)
        _write_center(worksheet, "B2", "url", self.wd)
        _write_center(worksheet, "C2", "请求方式", self.wd)
        _write_center(worksheet, "D2", "header", self.wd)
        _write_center(worksheet, "E2", "SetUp", self.wd)
        _write_center(worksheet, "F2", "TearDown", self.wd)
        _write_center(worksheet, "G2", "请求参数", self.wd)
        _write_center(worksheet, "H2", "请求结果", self.wd)
        _write_center(worksheet, "I2", "检查点", self.wd)
        _write_center(worksheet, "J2", "执行结果", self.wd)

        temp = 3
        for item in self.data:
            worksheet.set_row(temp, height=30)
            _write_center(worksheet, "A" + str(temp), str(item["TestName"]), self.wd)
            _write_center(worksheet, "B" + str(temp), str(item["url"]), self.wd)
            _write_center(worksheet, "C" + str(temp), item["method"], self.wd)
            _write_center(worksheet, "D" + str(temp), str(item["headers"]), self.wd)
            _write_center(worksheet, "E" + str(temp), str(item["set_up"]), self.wd)
            _write_center(worksheet, "F" + str(temp), str(item["tear_down"]), self.wd)
            _write_center(worksheet, "G" + str(temp), str(item["case_params"]), self.wd)
            _write_center(worksheet, "H" + str(temp), str(item["send_result"]), self.wd)
            _write_center(worksheet, "I" + str(temp), str(item["send_result"]), self.wd)
            _write_center(worksheet, "J" + str(temp), item["result"], self.wd)
            temp += 1
            # if item["test_image"] == None:
            #     _write_center(worksheet, "N" + str(temp), "", self.wd)
            # else:
                # worksheet.insert_image('N' + str(temp), item["test_image"],
                #                        {'x_scale': 0.1, 'y_scale': 0.1, 'border': 1})
                # worksheet.set_row(temp - 1, 110)

    def close(self):
        self.wd.close()


def get_format(wd, option={}):
    return wd.add_format(option)


def _write_center(worksheel, cl, data, wd):
    return worksheel.write(cl, data, get_format_center(wd))


def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})

