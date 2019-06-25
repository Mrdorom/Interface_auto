# coding:utf-8
import requests,json
from unit.base_path import Config
from unit.common import get_yaml_data
from unit.error_exception import GetTokenError


class GetSignature(object):
	# 如果登录还有需要别的参数，请自行添加
	def __init__(self):
		self.token = None
		signature_data = get_yaml_data(Config)["token"]
		self.headers = signature_data["headers"]
		self.login_data = signature_data["login_ata"]
		self.url = signature_data["url"]


	def get_token(self):
		self.login_data = json.dumps(self.login_data)
		try:
			re = requests.post(url=self.url,headers=self.headers,data=self.login_data)
			token = json.loads(re.text)["data"]["token"]
			return token
		except:
			raise GetTokenError("Token 获取错误")
