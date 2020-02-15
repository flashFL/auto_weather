import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver


def get_weather(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    aim = re.findall('<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日08时 (.*?)  (.*?)  (.*?)" />', req.text, re.S)
    print('%s月%s日 %s %s' % aim[0][:4])
    print('今日气温：' + aim[0][4])


def real_time_weather(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')
    tem = soup.find_all('div', class_='tem')
    print(tem)
    #从表象上看，大概是因为中国天气网使用的是shtml，造成有些内容使用requests或者urllib不可显


if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather1d/101260401.shtml'
    get_weather(url)
    # real_time_weather(url)
