from django.shortcuts import render

# Create your views here.  Reference templates.

def home(request):
	return render(request, 'jobs/home.html')