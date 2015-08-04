#!/usr/bin/python 
#coding=utf-8
#code from web
import urllib 
import urllib2 
def post(url, data):
  req = urllib2.Request(url) 
  data = urllib.urlencode(data) 
  #enable cookie 
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
  response = opener.open(req, data) 
  return response.read() 
def main(): 
  posturl = "http://www.hello.com/login.html"
  data = {'Username':'Username', 'Password':'Password', 'SaveOneWeek':'false', 'input':'登录'} 
  print post(posturl, data) 
if __name__ == '__main__': 
  main() 
