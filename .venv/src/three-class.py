from itertools import count
import json
from operator import truediv
from pyexpat import features

from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
# 下面是11.2的测试
# 你将阅读并解析一个包含文本和数字的文件。
# 你将提取文件中的所有数字并计算数字的总和。
'''
import re
def num_sum(file_location):
    sun_arr = list()
    file_data = open(file_location, 'r')
    for line in file_data:
        find_data = re.findall(r'\d+', line)
        sun_arr = sun_arr + find_data
    sun_arr = [int(i) for i in sun_arr]
    print(sum(sun_arr))
num_sum('../data/sql/regex_sum_42.txt')
num_sum('../data/sql/regex_sum_2075511.txt')
'''
# 下面是12.2的测试
# 您可以通过三种方式检索此网页并查看响应标头：
# 首选：修改socket1.py 程序以检索上述 URL 并打印出标头和数据。确保更改代码以检索上述 URL - 每个 URL 的值都不同。
# 使用开发人员控制台或 FireBug 在 Web 浏览器中打开 URL，然后手动检查返回的标头。
# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('127.0.0.1', 9999))

# 下面是12.7的测试
'''
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# requests方法
sun = 0
url = 'http://py4e-data.dr-chuck.net/comments_2075513.html'
get_web_content_re = requests.get(url)
web_content_re = get_web_content_re.text
soup = BeautifulSoup(web_content_re, 'html.parser')
span = soup.find_all('span')
for i in span:
    i = int(i.text)
    sun += i
print(sun)

# urillb方法
sun = 0
get_web_content_ur = urlopen(url)
web_content_ur = get_web_content_ur.read()
soup = BeautifulSoup(web_content_ur, 'html.parser')
span = soup.find_all('span')
for i in span:
    i = int(i.text)
    sun += i
print(sun)
'''
# 下面是12.8的测试
'''



# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# url = 'http://py4e-data.dr-chuck.net/known_by_Fares.html '
# url = input('Enter URL: ')
# count_i = '7'
# option_i = '18'
url = input('Enter url: ')
count_i = input('Enter count: ')
option_i = input('Enter option: ')

count_i = int(count_i)
option_i = int(option_i)
option_i = option_i - 1

def get_web_content(url,count_i,option_i):
    print('Retrieving:',url)
    href_line = list()
    get_web_content_ur = urlopen(url)
    web_content_ur = get_web_content_ur.read().decode('utf-8')
    if count_i > 0:
        soup = BeautifulSoup(web_content_ur, 'html.parser')
        a = soup.find_all('a')
        for i in a:
            href = i.get('href')
            href_line.append(href)
        url = href_line[option_i]

        get_web_content(url,count_i - 1,option_i)
    else:
        print('****************')
        h1_arr = list()
        soup = BeautifulSoup(web_content_ur, 'html.parser')
        h1 = soup.find_all('h1')
        for i in h1:
            h1_arr.append(i.text)
        h1_arr = h1_arr[0]
        h1_arr = h1_arr.split(' ')
        print(h1_arr[2])
get_web_content(url,count_i,option_i)
'''
# 下面是13.5的测试
'''
sun = list()
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
get_web_content_ur = urlopen(url)
web_content_ur = get_web_content_ur.read().decode('utf-8')
soup = BeautifulSoup(web_content_ur, 'html.parser')
count_f = soup.find_all('count')
for i in count_f:
    i = int(i.text)
    sun.append(i)
print(sum(sun))

################################################


# url = 'http://py4e-data.dr-chuck.net/comments_2075515.xml'
# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count: 50
# Sum: 2...
sunn = list()
url = input('Enter location: ')
if len(url) < 1:
    print('Retrieved:',url)

get_web_content_ur = urlopen(url)
web_content_ur = get_web_content_ur.read().decode('utf-8')
print('Retrieved',len(web_content_ur),'characters')
root = ET.fromstring(web_content_ur)
elements = root.findall('.//count')
print('Count:',len(elements))
for i in elements:
    i = int(i.text)
    sunn.append(i)
print('Sum:',sum(sunn))
'''

# 下面是13.8的测试
'''
# 定义网站地址
url_one = 'http://py4e-data.dr-chuck.net/comments_42.json'
url_two = 'http://py4e-data.dr-chuck.net/comments_2075516.json'

# or输入网站地址
url_text = input('Enter location: ')
print('Retrieving http:',url_text)


def get_json_count_sum(url):
    sun_num = list()
    # 打开网站
    get_web_content_ur_open = urllib.request.urlopen(url)
    # 将网站内容从字节流转换为str
    web_content_ur_open = get_web_content_ur_open.read().decode('utf-8')
    print('Retrieved',len(web_content_ur_open),'characters')
    # 将json字符串转换为py对象
    web_content_str_open = json.loads(web_content_ur_open)
    # 循环遍历对象并添加到数组当中
    print('Count:',len(web_content_str_open['comments']))
    for i in web_content_str_open['comments']:
        i['count'] = int(i['count'])
        sun_num.append(i['count'])
    sun_num = sum(sun_num)
    print('Sum:',sun_num)

get_json_count_sum(url_text)
get_json_count_sum(url_one)
get_json_count_sum(url_two)
'''

# 下面是13.9的测试
while True:
    get_api_url = 'http://py4e-data.dr-chuck.net/opengeo?'
    get_api_url_input = input('Enter location: ')

    url_end_dict = dict()
    if len(get_api_url_input) < 1:
        print('Retrieved:',url)
        break
    # 去处url后缀空格
    get_api_url_input = get_api_url_input.strip()
    # 输入API要求值为dict
    url_end_dict['q'] = get_api_url_input
    # 将dict转换为url
    url_end = urllib.parse.urlencode(url_end_dict)
    url = get_api_url + url_end
    url.rstrip('/')
    print('Retrieving:',url)
    # 接取返回值
    get_web_content = urllib.request.urlopen(url)
    # 接取状态码
    status = get_web_content.getcode()
    # 字节流转换为str
    get_web_content = get_web_content.read().decode('utf-8')
    print('Retrieved',len(get_web_content),'characters')
    # str转换为dict
    get_web_content_str = json.loads(get_web_content)
    get_web_content_str = get_web_content_str['features'][0]['properties']['plus_code']
    print('Plus code',get_web_content_str)
