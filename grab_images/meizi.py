# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
} ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mzitu.com/all'  ##开始的URL地址
start_html = requests.get(all_url, headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
# print(start_html.text) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
Soup = BeautifulSoup(start_html.text, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
all_a = Soup.find('div', class_='all').find_all('a') ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签
for a in all_a: ##这个不解释了。看不懂的小哥儿回去瞅瞅基础教程
    # print(a) ##同上
    title = a.get_text()
    href = a['href']
    if ('old' not in href):
        # print(title, href)
        headers['Referer'] = href
        # print(headers, href)
        html = requests.get(href, headers=headers)
        html_soup = BeautifulSoup(html.text, 'lxml')
        max_span = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text() ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
        for page in range(1, int(max_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
            page_url = href + '/' + str(page) ##同上
            headers['Referer'] = page_url
            print(page_url) ##这个page_url就是每张图片的页面地址啦！但还不是实际地址！
            single_html = requests.get(page_url, headers=headers)
            single_soup = BeautifulSoup(single_html.text, 'lxml')
            img = single_soup.find('div', class_='main-image').find('img')
            print(img['src'], img['alt'])
