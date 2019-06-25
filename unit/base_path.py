# coding:utf-8

import os

BASE_PATH = lambda p: os.path.join(
	os.path.abspath('.'),p
)   # 项目根目录

Db_Config = BASE_PATH("config/db.yaml")   # 数据库配置
Config = BASE_PATH("config/config.yaml")
Test_Case_Dir = BASE_PATH("testcase")    # 用例存放文件
LOGDIR = BASE_PATH("log")                # 日志目录
Result_Dir = BASE_PATH("result")         #  结果目录
Non_Execution = BASE_PATH("config/non_execution.yaml")


if __name__ == "__main__":
	print(Db_Config)