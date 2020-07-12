from django.shortcuts import render

# Create your views here.

def show_message(request):
	return render(request, 'hello_world.html',{})