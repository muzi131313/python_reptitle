# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import bs4


#获取数据
def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""


#填充列表
def fillUnivList(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[4].string])

#打印列表
def printUnivList(ulist,num):

	# 由于不清楚制表符\t 为什么导致编排难看的情况 仅仅是强行加了一个笨笨的编排 tpld
	# 原来的		tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'   
	tplt = '{0:<10}\t{1:{3}<10}\t{2:<10}' 
	tpld = '{0:<14}{1:<22}{2:<10}'
	print(tpld.format("排名","学校名称","总分"))
	for i in range(num):
		u=ulist[i]
		print(tplt.format(u[0],u[1],u[2],chr(12288)))

#主函数
def main():
	uinfo = []
	url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
	html = getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,10)

main()
