#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib

class agent:
    def get_ip(self,fout):
        for num in range(1,10):
            url = 'http://www.kuaidaili.com/proxylist/%d' % num
            data = urllib.urlopen(url)
            soup = BeautifulSoup(data)
            div = soup('div')
            for d in div:
                try:
                    did = d['id']
                    #print did
                    if did == 'list':
                        source = str(d.table.tbody)
                        newdata = BeautifulSoup(source)('tr')
                        for d in newdata:
                            print d.td.string
                            fout.write(d.td.string+'\n')
                except:
                    continue
                        
                        
if __name__ == '__main__':
    fout = open('agent_ip.txt','w')
    ag = agent()
    ag.get_ip(fout)
