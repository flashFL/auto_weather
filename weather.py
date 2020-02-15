#!/bin/sh
# encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver


def get_weather(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    aim = re.findall('<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日20时 (.*?)  (.*?)  (.*?)" />', req.text, re.S)

    fout = open('result.html', 'w')
    fout.write('<html>') #设置输出的HTML文件的格式
    fout.write('<body>')
    fout.write('<table>')
    fout.write("<tr>")
    fout.write("<td>%s月%s日 %s %s</td>" % aim[0][:4])  # 将爬取的信息写入到html文件中
    fout.write("</tr>")
    fout.write("<tr>")
    fout.write("<td>今日气温：%s</td>" % aim[0][4])
    fout.write("</tr>")
    fout.write("</table>")
    fout.write("</body>")
    fout.write("</html>")



# 使用requests.get()方式有些内容不可获得,实时气温功能暂不可用。ps:中国天气网使用的是shtml
# def real_time_weather(url):
#     req = requests.get(url)
#     req.encoding = 'utf-8'
#     soup = BeautifulSoup(req.text, 'html.parser')
#     tem = soup.find_all('div', class_='tem')
#     print(tem)


if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather1d/101260401.shtml'
    get_weather(url)
    # real_time_weather(url)
