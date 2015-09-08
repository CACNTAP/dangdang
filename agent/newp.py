#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import random
import cookielib


fin = open('agent_ip.txt')
proxy_list = []
for line in fin:
    proxy_list.append(line.strip())
    
    
def print_data():
    url = 'http://product.dangdang.com/23269382.html'
    proxy = {'http':random.choice(proxy_list)}
    cj = cookielib.CookieJar()
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support,urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    try:
        response = opener.open(url,timeout=2)
    except Exception,e:
        print str(e)
        print_data()
        return
    soup=BeautifulSoup(response)
    data = soup('div')
    for d in data:
        #print d
        if 'id' in d.attrs:
            did = d['id']
            if did=="alsoview":
                source = str(d.div.ul)
                sdata = BeautifulSoup(source)('li')
                for s in sdata:
                    num = s.a.img['src'].split('/')
                    for n in num:
                        if "-" in n:
                            da = n.split('-')[0]
                            #fout.write(da+'\t'+s.a['title'].strip().encode('utf-8')+'\t'+'\n')
                            print s.a['title'].strip(),da
                            
print_data()
