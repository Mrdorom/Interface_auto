# coding:utf-8

import xlrd
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
