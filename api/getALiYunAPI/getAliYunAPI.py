# encoding=utf8
import urllib, sys
import urllib.request as urllib2
import json
from time import sleep
from urllib import parse
import sys

print(sys.getdefaultencoding())


def UCaseChar(ch):
    if ord(ch) in range(97, 122):
        return chr(ord(ch) - 32)
    return ch


def LCaseChar(ch):
    if ord(ch) in range(65, 91):
        return chr(ord(ch) + 32)
    return ch


def Ucase(str):
    return "".join(map(UCaseChar,str))


def Lcase(str):
    return "".join(map(LCaseChar,str))

def getNumberCity(phone):
    host = 'http://jshmgsdmfb.market.alicloudapi.com'
    path = '/shouji/query'
    method = 'GET'
    appcode = '2f1e16cbdaeb4cd788d92109bb67c0d0'
    querys = 'shouji={0}'.format(phone)
    bodys = {}
    url = host + path + '?' + querys

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        numInfo = json.loads(content.decode('utf-8'))
        print(numInfo.get("result").get("province"))
        return numInfo
    return


def getWeather(city):
    host = 'http://freecityid.market.alicloudapi.com'
    path = '/whapi/json/alicityweather/briefforecast3days'
    method = 'POST'
    appcode = '2f1e16cbdaeb4cd788d92109bb67c0d0'
    querys = '安庆'
    bodys = {}
    url = host + path

    bodys['cityId'] = '''45'''
    bodys['token'] = '''677282c2f1b3d718152c4e25ed434bc4'''
    post_data = urllib.parse.urlencode(bodys).encode(encoding='UTF8')
    request = urllib2.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        weaInfo = json.loads(content.decode('utf-8'))
        return weaInfo
    return


def getNews():
    host = 'http://toutiao-ali.juheapi.com'
    path = '/toutiao/index'
    method = 'GET'
    appcode = '2f1e16cbdaeb4cd788d92109bb67c0d0'
    querys = 'type=type'
    bodys = {}
    url = host + path + '?' + querys

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        newsInfo = json.loads(content.decode('utf-8'))
        print(newsInfo.get("result"))
        return newsInfo
    return


def getRebotChat(strMsg):
    host = 'http://jisuznwd.market.alicloudapi.com'
    path = '/iqa/query'
    method = 'GET'
    appcode = '2f1e16cbdaeb4cd788d92109bb67c0d0'
    querys = 'question=%s' % urllib.parse.quote(strMsg.encode('utf-8'))

    bodys = {}
    url = host + path + '?' + querys
    print(url)

    print(urllib.parse.quote(url.encode('ascii')))

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        newsInfo = json.loads(content.decode('utf-8'))
        print(newsInfo.get("result"))
        return newsInfo
    return

if "__main__" ==__name__:
    #print(getNumberCity("17602112408"))
    getWeather("")
    #getNews()
    #getRebotChat("查询上海天气")
