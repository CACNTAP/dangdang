#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re 
from random import random,randint,choice
from time import sleep
from copy import deepcopy
from agent import agent

fout = open('info_log-%s.txt'%str(datetime.now())[:10],'w')



def browser(numss,ip):
    nums=deepcopy(numss)
    for i in range(15):
        num = randint(23665001,23765381)
        nums.append(num)
    for i in range(10):
        index = randint(0,19)
        temp = nums[i]
        nums[i] = nums[index]
        nums[index]=temp
    cj = cookielib.CookieJar()
    headers=[]
    headers.append('Mozilla/5.0 (compatible; MSIE 10.0; WindowsNT 6.1; WOW64; Trident/6.0; QQBrowser/7.7.24962.400)')
    headers.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
    headers.append('Mozilla/5.0 (compatible; MSIE 10.0;Windows NT 6.1; WOW64; Trident/6.0)')
    headers.append('Mozilla/5.0 (compatible; MSIE 10.0;Windows NT 6.1; WOW64; Trident/6.0) LBBROWSER')
    try:
        proxy = {'http':ip}
        proxy_support = urllib2.ProxyHandler(proxy)
        opener=urllib2.build_opener(proxy_support,urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent',choice(headers))]
        urllib2.install_opener(opener)
    except:
        return
    for num in nums:
        url = "http://product.dangdang.com/%d.html" %num
        try:
            opener.open(url,timeout=5)
            print url
            #sleep(random())
        except Exception,e:
            print url
            print str(e)
            continue
    #print nums
        

def attack():
    response = urllib.urlopen('http://product.dangdang.com/23269384.html')
    soup=BeautifulSoup(response)
    data = soup('div')
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
                            fout.write(da+'\t'+s.a['title'].strip().encode('utf-8')+'\t'+'\n')
                            print s.a['title'].strip(),da
                            
def testip(ip):
    proxy = {'http':ip}
    proxy_support = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    try:
        url = 'http://product.dangdang.com/23269384.html'
        response = opener.open(url,timeout=2)
        return True
    except Exception,e:
        print str(e)
        return False
    
    
def agent_ip():
    agentout = open('agent_ip.txt','w')
    ag = agent()
    ag.get_ip(agentout)
    agentout.close()
            
def start():
    fin = open('agent_ip.txt')
    proxy_list = []
    for line in fin:
        #print line
        proxy_list.append(line.strip())
    begin = datetime.now()
    nums=[]
    count = 0
    while count<6:
        num = randint(23165001,23765381)
        try:
            url = "http://product.dangdang.com/%d.html" %num
            urllib.urlopen(url)
            nums.append(num)
            fout.write(str(num)+'\t')
            count+=1;
        except Exception,e:
            continue
    nums.append(23269384)
    fout.write('\n')
    for i in range(100):
        if i%10==0:
            agent_ip()
    
        info = str(datetime.now()-begin)
        fout.write("Acctack: "+str(i+1)+'\t')
        fout.write('\t'+info+'\n')
        attack()
        for j in range(50):
            ip = choice(proxy_list)
            if testip(ip):
                browser(nums,ip)
        print i+1
        
if __name__ =="__main__":
    start()
    fout.close()
