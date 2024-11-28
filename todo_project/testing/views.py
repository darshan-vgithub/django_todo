from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def testing(request):
    return render(request, 'hello_list.html')
    


