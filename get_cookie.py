import urllib2
import cookielib
#实例化cookie存储对象
cookie=cookielib.CookieJar()
#实例化cookie获取对象
handler=urllib2.HTTPCookieProcessor(cookie)
#实例化HTTP请求对象
opener=urllib2.build_opener(handler)
opener.open('http://www.google.com.hk'）