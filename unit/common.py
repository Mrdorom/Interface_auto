# coding:utf-8

from unit.base_path import CONFIG_PATH
import xlrd
import configparser
import yaml


"""-------------------------ReadExcel--------------------------------"""

def get_excel(case_data_file,sheetname):
	test_data = []
	wb = xlrd.open_workbook(case_data_file)
	sheet = wb.sheet_by_name(sheetname)
	keys = sheet.row_values(0)
	max_row = sheet.nrows
	max_nclos = sheet.ncols
	if max_row<=1:
		print('没有测试数据')
	else:
		for i in range(1,max_row):
			app = {}
			for j in range(max_nclos):
				app['rownum'] = i+1
				ctype = sheet.cell(i,j).ctype   # 获取Excel 表格数据类型
				value = sheet.cell (i, j).value
				if ctype ==2:
					value = int(value)
				app[keys[j]] =  value
			test_data.append(app)
	return test_data

"""---------------------------------ReadConfig-----------------------------------------"""


class ReadConfig(object):

	def __init__(self):
		self.cf = configparser.ConfigParser()
		self.cf.read(CONFIG_PATH)    # CONFIG_PATH 配置文件地址

	def get_http_data(self,option):
		"""
		读取Http数据
		:param option:
		:return:
		"""
		data = self.cf.get("Http",option)
		return data


	def get_database_data (self, option):
		"""
		读取数据库配置数据
		:param option:
		:return:
		"""

		data = self.cf.get ("Database", option)
		# data = self.cf.get ("Database", "/Users/workspace/btclass/code/config/config.ini")
		return data

	def get_email_data(self,option):
		"""
		读取Email数据
		:param option:
		:return:
		"""
		data = self.cf.get("Email",option)
		return data


"""----------------------------------ReadYaml---------------------------------------------------"""

def get_yaml_data(file):
	with open(file,encoding='utf-8') as f:
		data = yaml.full_load((f.read()))
		return data

if __name__ =="__main__":

	file = r"/Users/workspace/btclass/code/data/interface/ms_classgrooup.yaml"
	data = get_yaml_data(file)
	for i in data:
		print(i,)
