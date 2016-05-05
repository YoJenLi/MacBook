# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from models import jobinfo
from models import searchJob
from django.shortcuts import render_to_response

def index(request):
	return render(request,'index.html')

def getjob(request,name):
	name = request.GET['name']

	job = searchJob().search(name)

	return render_to_response('post_list.html',locals())	
	#render_to_response = 取得模板(get_template)+填寫模板(context+render)+回應(HttpResponse)
	#locals()內建函數會回傳一個字典('post_list.html',{'job':job})直接用locals代替

