# coding:utf-8

from unit.abs_api import CreateCase
from unit.base_path import Test_Case_Dir,Non_Execution
from unit.common import get_yaml_data
import multiprocessing
import os


class Runner(object):
    def __init__(self):
        self.case_file_list = []

    def __get_case_file(self,dest_file=Test_Case_Dir):
        """获取所有的用例文件"""
        file_list = os.listdir(dest_file)
        non_execution_data = get_yaml_data(Non_Execution)
        for execution in non_execution_data:
            if execution in file_list:
                file_list.pop(file_list.index(execution))
        try:
            file_list.pop(file_list.index("__pycache__"))
            file_list.pop(file_list.index(".DS_Store"))
        except:
            pass

        for file in file_list:
            full_path = os.path.join(Test_Case_Dir,file)
            flag = os.path.isdir(full_path)
            if flag:
                self.__get_case_file(full_path)
            else:
                arr = os.path.splitext(file)
                if arr[1] == ".yaml":
                    case_file = os.path.join(dest_file,file)
                    self.case_file_list.append(case_file)

    def runner_case(self,file):
        craeate = CreateCase()
        craeate.main(file)

    def mult_runner_case(self):
        """多进程调用"""
        self.__get_case_file()
        mult_pool = []
        for i in range(len(self.case_file_list)):
            print(self.case_file_list[i])
            pool = multiprocessing.Process(target=self.runner_case,args=(self.case_file_list[i],))
            mult_pool.append(pool)
        for pool in mult_pool:
            pool.start()
        for pool in mult_pool:
            pool.join()

if __name__ == '__main__':
    R = Runner()
    R.mult_runner_case()
