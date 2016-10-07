from django.shortcuts import render,HttpResponse
from firstapp.models import People
from django.template import Context,Template
# Create your views here.

def first_try(request):
	people=People(name='Zhangzhuqian',job='Officer')
	html_string='''
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset="utf-8">
				<title></title>
			</head>
			<body>
				<h1>Hello {{ person.name}}</h1>
			</body>
		</html>

	'''

	c=Context({'People': people})
	t=Template(html_string)
	web-page=t.render(c)
	return HttpResponse(web_page)
