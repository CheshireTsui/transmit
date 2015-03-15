# Create your views here.
# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
import urllib2
import re


def index(request, son_url=''):
    
    postUrl = 'http://magicard.herokuapp.com/'
    cookie_pattern = re.compile(r'Set-Cookie:\s?(.*?)\n',re.S)
    name_pattern = re.compile(r'^(.*?)=(.*?);',re.S)
    
    try:
        if son_url:
            postUrl = postUrl + son_url
        if request.method == 'POST':
            postData = request.raw_post_data #Use request.body instead in Django 1.7
            request2 = urllib2.Request(postUrl, postData)
        else:
            request2 = urllib2.Request(postUrl)
        #向request2中添加来自客户端的cookie
        raw_dict = request.COOKIES
        if raw_dict:
            lis = ''
            for i in raw_dict:
                lis = lis + i + '=' + raw_dict[i] + '; '
            request2.add_header('Cookie', lis)
        response = urllib2.urlopen(request2)
        postData = response.read()
        
        #向postData中添加来自服务器的cookie
        response2 = HttpResponse(postData)
        raw_list = cookie_pattern.findall(str(response.headers))
        if raw_list:
            for i in raw_list:
                lis = name_pattern.search(i).groups()
                response2.set_cookie(lis[0], lis[1])
        return response2
    
    except Exception, e:
        return HttpResponse(e)