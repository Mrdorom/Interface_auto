# coding:utf-8
from unit.base_api import SendRequest
from unit.base_path import Result_Dir
from unit.common import get_yaml_data
from unit.dbConnect import DbOption
from unit.report import SetStyle
from queue import Queue
import re
import xlsxwriter
import time
import json
import os


class CreateCase(object):

    def __init__(self):
        self.data = None
        self.queue_labels = Queue()
        self.case_name = None
        self.base_url = None
        self.full_url = None
        self.method = None
        self.header = None
        self.case_params = None
        self.check = None
        self.set_up = None
        self.tear_down = None
        self.send_result = None
        self.result = None

        self.db = DbOption()
        self.result_name = None

    def __get_file_data(self,file):
        self.result_name = os.path.splitext(os.path.split(file)[1])[0]
        data = get_yaml_data(file)
        self.data = data

    def __get_case_queue(self):
        for datum in self.data:
            if datum !="base_url":
                self.queue_labels.put(datum)

    def __get_base_url(self):
        self.base_url = self.data["base_url"]

    def __component_case(self):
        """构建用例"""
        _request_list = []
        self.__get_base_url()
        if  not self.queue_labels.empty():
            for test_label in range(self.queue_labels.qsize()):
                label = self.queue_labels.get()
                label_data = self.data[label]
                path = label_data["url_path"]
                self.method = label_data["method"]
                self.header = label_data["headers"]
                case_list = label_data["case"]
                pattern = re.compile(r"{(.*?)}")
                patten_result = pattern.findall(path)
                for case_data in case_list:
                    if len(patten_result) ==0:
                        # print("url 不需要拼接")
                        self.full_url = self.base_url+ path
                        self.case_params = case_data
                    else:
                        # 需要拼接的url特殊处理
                        for re_str in patten_result:
                            # 如果正则匹配不到，重新获取path
                            if not pattern.findall(path):
                                path = label_data["url_path"]
                            path = pattern.sub(str(case_data[re_str]),path,1)
                            del case_data[re_str]
                            self.full_url = self.base_url + path
                            # params 特殊处理
                            self.case_params = case_data
                    self.case_name = self.case_params["test_type"]
                    self.set_up = self.case_params["set_up"]
                    self.tear_down = self.case_params["tear_down"]
                    self.check = self.case_params["check"]
                    # print(self.check)
                    del self.case_params["set_up"]
                    del self.case_params["tear_down"]

                    _request = {}
                    _request["TestName"] = self.case_name
                    _request["url"] = self.full_url
                    _request["method"] = self.method
                    _request["headers"] = self.header
                    _request["set_up"] = self.set_up
                    _request["tear_down"] = self.tear_down
                    _request["case_params"] = self.case_params
                    self.__send_request()
                    _request["send_result"] = self.send_result
                    _request["result"] = self.result
                    _request_list.append(_request)
                    # print(self.result)
            self.write_report(_request_list)
            print(_request_list)

    def __send_request(self):
        """执行接口"""
        sr = SendRequest()
        sr.set_url(self.full_url)
        sr.set_headers(self.header)
        sr.set_mothod(self.method)
        if self.method not in ("get", "GET"):
            self.case_params = json.dumps(self.case_params)
            sr.set_data(self.case_params)
        else:
            sr.set_params(self.case_params)
        try:
            if self.set_up is not None:
                self.judge_sql(self.set_up)
        except:
            print("接口初始化失败")
        finally:
            try:
                res = sr.send_request()
                self.send_result = res
                # print(res)
                # res = json.dumps(res)
                self.result = self.check_point(res)
            except Exception as e:
                print("出错了")
                self.result = "Error"
            finally:
                if self.tear_down is not None:
                    self.judge_sql(self.tear_down)
                print("数据清理")

    def judge_sql(self,sql_data):
        """判断sql语句的操作类型"""
        for sql_datum in sql_data:
            sql_type = list(sql_datum.keys())
            for datum in sql_type:
                if datum == "select":
                    self.db.select(sql_datum[datum])
                else:
                    self.db.operation(sql_datum[datum])

    def check_point(self,res):
        res= json.loads(res)
        res_code = res["code"]
        # print(res_code)
        for datum in self.check:
            if isinstance(datum,str):
                if datum in res:
                    return True
                else:
                    return False
            elif isinstance(datum,list):
                pass

            elif isinstance(datum,dict):
                check_code = datum[list(datum.keys())[0]]
                # print(check_code)
                try:
                    assert str(check_code) == str(res_code)
                    return True
                except AssertionError:
                    return False
            else:
                print("不存在的检查点类型")

    def write_report(self,data):
        tr = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        report_dir = os.path.join(Result_Dir,tr)
        if not os.path.exists(report_dir):
            os.mkdir(report_dir)
        workbook = xlsxwriter.Workbook(os.path.join(report_dir,self.result_name+".xlsx"))
        worksheet = workbook.add_worksheet("测试详情")
        bc = SetStyle(wd=workbook, data=data)
        bc.test_detail(worksheet)
        bc.close()

    def main(self,file):
        self.__get_file_data(file)
        self.__get_case_queue()
        self.__component_case()

if __name__ == "__main__":
    pass