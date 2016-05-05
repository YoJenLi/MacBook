from django.shortcuts import render_to_response

def math(request,a,b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b

	return render_to_response('math.html',locals())

