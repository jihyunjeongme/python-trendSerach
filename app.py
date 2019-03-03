# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
import pprint

client_id = "Ax_loNWh6muXFz9nVi9B***wsd"
client_secret = "r0zIdpxwud***wsd"
url = "https://openapi.naver.com/v1/datalab/search"
body = '{"startDate":"2016-01-01","endDate":"2019-02-28","timeUnit":"month","keywordGroups":[{"groupName":"북미정상회담","keywords":["북미정상회담"]}],"device":"","ages":["1","2","3","4","5","6","7","8","9","10","11"],"gender":""}'

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
request.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode("utf-8"))
else:
    print("Error Code:" + rescode)
