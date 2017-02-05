# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:39:47 2017
@author: tianmin
"""

import requests
from lxml import etree as etree
import urllib
import re
import multiprocessing

'''
#西刺代理国内高匿免费Http代理
def get_xici():
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
def get_kuaidaili():
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
'''
#获取66ip免费Http代理
def get_66ip():
    proxy=[]
    url='http://www.66ip.cn/mo.php?sxb=&tqsl=10&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=http%3A%2F%2Fwww.66ip.cn%2F%3Fsxb%3D%26tqsl%3D10%26ports%255B%255D2%3D%26ktip%3D%26sxa%3D%26radio%3Dradio%26submit%3D%25CC%25E1%2B%2B%25C8%25A1'
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive'
                }
    html=requests.get(url,headers=header).text
    proxy=re.findall(r'(\d+.\d+.\d+.\d+:\d+)',html)
    
    return proxy
    


def check_proxy():
    
    for i in all_proxies:
        url_test='http://www.baidu.com/js/bdsug.js?v=1.0.3.0'
        proxy_handler=urllib.request.ProxyHandler({"http":"http://"+i})
        opener=urllib.request.build_opener(proxy_handler,urllib.request.HTTPHandler)
        try:
            response = opener.open(url_test, timeout=3)
            print ("这个可以用：",i)
            with open('D:/python/12.txt','a+') as f:
                f.write(' '+str(i)+'\n')
                f.close()
        except Exception:
            print ("这个不行：",i)

            
if __name__=="__main__":
    all_proxies=[]
    #all_proxies+=get_xici()
    #all_proxies+=get_kuaidaili()
    all_proxies+=get_66ip()
    print (all_proxies)
    print (type(all_proxies))
    list_ip=all_proxies
    pool=multiprocessing.Pool(processes=4)
    pool.apply_async(check_proxy(),list_ip)
    pool.close()
    pool.join()
    print('All subprocesses done.')
