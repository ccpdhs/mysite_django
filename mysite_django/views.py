from django.http import HttpResponse


def  index(reguest):
	return HttpResponse("Hello,World!")