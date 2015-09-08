#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re 
from selenium import webdriver


browser = webdriver.PhantomJS()
response = browser.get('http://product.dangdang.com/23269384.html')
#response = urllib.urlopen('http://product.dangdang.com/23269384.html')
print type(response)
soup=BeautifulSoup(response)
data = soup('div')
'''for d in data:
    try:
        did = d['id']
        if did == "alsoview":
            #print d
            source = d.div.ul.li
            print source
            sdata = BeautifulSoup(source)
            dsoup = sdata('p')
            for p in dsoup:
                print p.string
            
    except:
        continue'''
        
        
for d in data:
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
                print s.a['title'].strip(),da
            
    

