from django.http import HttpResponse
from django.shortcuts import render

def reverse(request):
    return render(request,'reverse/reverse.html')

def print_rever(request):
    text=request.POST.get('title')
    newtext=''
    for n in range(len(text)-1,-1,-1):
        newtext=newtext+text[n]
    return render(request,'reverse/reversed.html',{'data':newtext})
    
