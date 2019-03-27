from django.shortcuts import render

# Create your views here.

def phil(request):
	return render(request, 'jobs/phil.html')