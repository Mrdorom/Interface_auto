# coding:utf-8

import os

BASE_PATH = os.path.abspath('.')   # 项目根目录
Db_Config = os.path.join(BASE_PATH,"config/db.yaml")   # 数据库配置
Test_Case_Dir = os.path.join(BASE_PATH,"testcase")    # 用例存放文件
LOGDIR = os.path.join(BASE_PATH,"log")                # 日志目录
Result_Dir = os.path.join(BASE_PATH,"result")         #  结果目录


if __name__ == "__main__":
	print(BASE_PATH)