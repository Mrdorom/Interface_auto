# coding:utf-8

import logging
import os
import time
from unit.base_path import LOGDIR


class Logger(object):

	def __init__(self,funcname):
		self.log = logging.getLogger(funcname)
		self.log.setLevel(logging.INFO)

		dirname = os.path.join(LOGDIR,time.strftime('%Y-%m-%d',time.localtime(time.time())))
		name = "test_log.log"
		logname = os.path.join(dirname,name)
		if not os.path.exists(dirname):
			os.mkdir(dirname)

		# flag = True
		# num = 0
		# while flag:
		# 	if os.path.exists(logname):
		# 		name = "test_log_{0}.log".format(num)
		# 		logname = os.path.join (dirname, name)
		# 		num+=1
		# 	else:
		# 		flag =False

		# 创建handler
		fh = logging.FileHandler(logname)
		fh.setLevel(logging.INFO)

		ch = logging.StreamHandler()
		ch.setLevel(logging.INFO)


		# 设置输出格式

		formatter = logging.Formatter("%(asctime)s -%(name)s- %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
		ch.setFormatter(formatter)
		fh.setFormatter(formatter)

		# 添加handler
		self.log.addHandler (fh)
		self.log.addHandler (ch)


	def get_log(self):

		return self.log

if __name__ == "__main__":
	l = Logger('func')
	logger = l.get_log()
	logger.info('aaa')

