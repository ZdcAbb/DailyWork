import urllib
import json

print "hello world"
#coding=utf-8

#  
def func(x):
    return x + 2

# 
def test_answer():
    assert func(3) == 5
    
    
print "hello world"
import urllib
import json

def get_dic(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    dic=json.loads(html)
    return dic

dic = get_dic("http://www.weather.com.cn/data/cityinfo/101010100.html")

print dic['weatherinfo']['city']
print dic['weatherinfo']['ptime']
print dic['weatherinfo']['temp1']
print dic['weatherinfo']['temp2']
print dic['weatherinfo']['weather']
