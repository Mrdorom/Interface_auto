# coding:utf-8

from unit.abs_api import CreateCase
from unit.base_path import Test_Case_Dir
import multiprocessing
import os


class Runner(object):
    def __init__(self):
        self.case_file_list = []

    def __get_case_file(self):
        """获取所有的用例文件"""
        file_list = os.listdir(Test_Case_Dir)
        for file in file_list:
            arr = os.path.splitext(file)
            if arr[1] == ".yaml":
                case_file = os.path.join(Test_Case_Dir,file)
                self.case_file_list.append(case_file)

    def runner_case(self,file):
        craeate = CreateCase()
        craeate.main(file)

    def mult_runner_case(self):
        """多进程调用"""
        self.__get_case_file()
        mult_pool = []
        for i in range(len(self.case_file_list)):
            pool = multiprocessing.Process(target=self.runner_case,args=(self.case_file_list[i],))
            mult_pool.append(pool)
        for pool in mult_pool:
            pool.start()
        for pool in mult_pool:
            pool.join()

if __name__ == '__main__':
    R = Runner()
    R.mult_runner_case()


