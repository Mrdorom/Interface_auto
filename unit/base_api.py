# coding:utf-8

import requests
from unit.logger import Logger


class SendRequest(object):

	def __init__(self):
		self.method = {}
		self.url = ''

		self.params = {}
		self.data = {}
		self.header = {}
		self.file = ""
		self.mylogger = Logger("SendRequest").get_log()

	def set_mothod(self,method):
		self.method = method

	def set_url(self,url):
		self.url =  url

	def set_headers(self,headers):
		self.header = headers

	def set_data(self,data):
		self.data = data

	def set_params(self,params):
		self.params = params
		# self.mylogger.info(str(self.params))

	def set_file(self,file_name):
		if file_name != "":
			self.file = {"file":open(file_name,'rb')}

	def send_request(self):
		if self.method =="get" or self.method == "GET":
			try:
				# self.mylogger.info(str(self.url))
				# self.mylogger.info(str(self.params))

				res = requests.get(url=self.url,params=self.params,headers=self.header,verify=False)

				return res.text
			except Exception as msg:
				self.mylogger.info("错误请求信息：---------------------------------GET错误请求信息--------------------------------------"+'\n'
								   +"{0}".format(msg)+"\n"+
								   "-----------------------------------------------------------------------------------------"+"\n")
		elif self.method == "post" or self.method =="POST":
			try:
				res = requests.post(url=self.url,headers= self.header,data=self.data,verify=False)
				return res.text
			except Exception as msg:
				self.mylogger.info(
					"错误请求信息：---------------------------------POST错误请求信息--------------------------------------" + '\n'
					+ "{0}".format(msg) + "\n" +
					"-----------------------------------------------------------------------------------------"+"\n")
		elif self.method == "delete" or self.method =="DELETE":
			try:
				res = requests.delete(self.url,headers=self.header,data=self.data,verify=False)
				return res.text
			except Exception as msg:
				self.mylogger.info(
					"错误请求信息：---------------------------------DELETE错误请求信息--------------------------------------" + '\n'
					+ "{0}".format(msg) + "\n" +
					"-----------------------------------------------------------------------------------------"+"\n")
		elif self.method == "patch" or self.method == "PATCH":
			try:
				res = requests.patch(url=self.url,headers= self.header,data=self.data,verify=False)
				return res.text
			except Exception as msg:
				self.mylogger.info(
					"错误请求信息：---------------------------------PATCH错误请求信息--------------------------------------" + '\n'
					+ "{0}".format(msg) + "\n" +
					"-----------------------------------------------------------------------------------------" + "\n")
		elif self.method == "put" or self.method == "PUT":
			try:
				self.mylogger.info(self.data)
				self.mylogger.info(self.header)
				res = requests.put(url = self.url,headers = self.header,data=self.data)
				return res.text
			except Exception as msg:
				self.mylogger.info(
				"错误请求信息：---------------------------------PUT错误请求信息--------------------------------------" + '\n'
				+ "{0}".format(msg) + "\n" +
				"-----------------------------------------------------------------------------------------" + "\n")
		else:
			self.mylogger.info("不支持的请求方式：{0} 请检查excel method".format(self.method))




