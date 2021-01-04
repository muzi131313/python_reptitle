# -*- coding: utf-8 -*-

# url: http://zwfw.hubei.gov.cn:8503/xcms/shzzwebsite/jumpPage/shzz_xzxkgg.jhtml?currentPage=1&djType=1&flagname=XKGG

import json
import requests
import jsonpath
import time
# from bs4 import BeautifulSoup
# import bs4

#获取数据
def getJSONData(url, page = 1):
    try:
        d = {
            'currentPage': page,
            'shzzType': '',
            'djType': 1,
            'filename': 'XKGG',
            'shzzname': '',
            'shzzxydm': '',
        }
        r = requests.post(url, data = d, headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        response = r.text
        content = json.loads(response)
        return content
    except:
        return ""

#主函数
def main():
    codes = []
    url = "http://zwfw.hubei.gov.cn:8503/xcms/shzzwebsite/queryData.jspx"

    for index in range(14):
        jsonData = getJSONData(url, index + 1)
        # print("jsonData: ", jsonData)
        totalpages = jsonpath.jsonpath(jsonData, '$..totalpages')
        print('totalpages: ', totalpages)
        list = jsonpath.jsonpath(jsonData, '$..list')
        if (list != False):
            list = list[0]
        # print('list: ', list)
        for listItem in list:
            code = listItem['axxx0015']
            codes.append(code)
        time.sleep(10)
    print('codes: ', codes)

main()
