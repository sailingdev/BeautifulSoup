# -*- coding: utf-8 -*-
import requests

import csv
import json
import os
import datetime
import time
# import re


from bs4 import BeautifulSoup



print('Loading-------')

currentDT = datetime.datetime.now()

print('current date:' + str(currentDT))


class checker(object):
	"""docstring for checker"""

	def get_token(self):

		data = requests.get("https://www.offroadeq.com/en/log-in")

		soup = BeautifulSoup(data.text, "lxml")

		__VIEWSTATE = soup.find("input", {"name":"__VIEWSTATE"})["value"]
		__VIEWSTATEGENERATOR = soup.find("input", {"name":"__VIEWSTATEGENERATOR"})["value"]

		return __VIEWSTATE, __VIEWSTATEGENERATOR


	def post(self):

		tokens = self.get_token()

		print (tokens[0])
		print (tokens[1])

		# contracts = self.get_token()[0]
		# redirect = self.get_token()[1]
		# csrf_token = self.get_token()[2]
		# submitted = self.get_token()[3]
		# print(csrf_token)
			
		api_sender = requests.session()

		param = {"__VIEWSTATE":tokens[0], "ctl05$ct0$ctl01$username":"sgituku1", "ctl05$ct0$ctl01$password":"Unikaskazini1", "ctl05$ct0$ctl01$tos":"on", "__VIEWSTATEGENERATOR":tokens[1]}

		source = api_sender.post("https://www.offroadeq.com/en/log-in", data = param)

		# print(source.text)

		time.sleep(1)


		search_request_data = {"part": "7N8022", "sort": "", "nc": False, "cartid": 1418717, "od_id": 0}

		headers = {
			'accept': 'application/json, text/javascript, */*; q=0.01'
		}

		search_response = api_sender.post("https://www.offroadeq.com/services/ecommerce/mobile.svc/GetPartSearch", json=search_request_data)

		# root = xml.etree.ElementTree.fromstring(resp.content)
		# print(search_response.content)
		search_response_data = json.loads(search_response.content)

		print(search_response_data)

		exit()

	def start(self):
		self.post()


if __name__ == '__main__':
	checker().start()



exit()


