# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:39:47 2017

@author: tianmin
"""

import requests
from lxml import etree as etree
import urllib
'''
#西刺代理国内高匿免费Http代理
def xici():
    proxy=[]
    url='http://www.xicidaili.com/nn/'
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive'
        }
    html=requests.get(url,headers=header).text
    page=etree.HTML(html)
    proxy=page.xpath('//table[@id="ip_list"]/tr/td[2]/text()')
    return proxy


#快代理国内高匿代理
def kuaidaili():
    proxy=[]
    for i in range(1,3):
        url='http://www.kuaidaili.com/free/inha/'+str(i)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding':'gzip, deflate, br',
                'Connection':'keep-alive'
                }
        html=requests.get(url,headers=header).text
        page=etree.HTML(html)
        proxy=page.xpath('//td[@data-title="IP"]/text()')
    return proxy

all_proxies=[]
all_proxies+=xici()
all_proxies+=kuaidaili()

def check_proxy():
    
    for i in all_proxies:
        url_test='http://www.baidu.com/js/bdsug.js?v=1.0.3.0'
        proxy_handler=urllib.request.ProxyHandler({"http":"http://"+i})
        opener=urllib.request.build_opener(proxy_handler,urllib.request.HTTPHandler)
        try:
            response = opener.open(url_test, timeout=3)
            print ("这个可以用：",i)
            f=open('D:/12.txt','w')
            f.write(str(i))
            f.close()
        except Exception:
            print ("这个不行：",i)
            
check_proxy()   '''         

url='http://www.66ip.cn/mo.php?sxb=&tqsl=10&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=http%3A%2F%2Fwww.66ip.cn%2F%3Fsxb%3D%26tqsl%3D10%26ports%255B%255D2%3D%26ktip%3D%26sxa%3D%26radio%3Dradio%26submit%3D%25CC%25E1%2B%2B%25C8%25A1'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding':'gzip, deflate, br',
                'Connection':'keep-alive'
                }
html=requests.get(url,headers=header).text
page=etree.HTML(html)
proxy=page.xpath('//body/text()')
print(proxy)
