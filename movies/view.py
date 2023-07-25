from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from .models import UserTable
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def movies(request):
    data = Movie.objects.all()
    return render(request,'movies/movies.html',{'movies':data})

def detail(request,id):
    data= Movie.objects.get(pk=id)
    return render(request,'movies/detail.html',{'movies':data})
def add(request):
    url=''
    info=''
    title=request.POST.get('title')
    year=request.POST.get('year')
    url=request.POST.get('url')
    info=request.POST.get('info')
    rate=request.POST.get('rate')
    if title and year:
        movie= Movie(title =title, year=year,url=url,info=info,rate_system=rate)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request,'movies/add.html')
def delete(request,id):
    try:
        Movie.objects.get(pk=id).delete()
    except:
        raise Http404('Movie not here')
    return HttpResponseRedirect('/movies')
def database(request):
    data = Movie.objects.all()
    return render(request,'movies/dataList.html',{'movies':data})
def filtered(request):
     if request.method == 'POST':
        movies_rate = request.POST.get('selected_option')
        if movies_rate == 'clear':
            data = Movie.objects.all()
            return render(request,'movies/movies.html',{'movies':data})
        data = Movie.objects.filter(rate_system=movies_rate)
        return render(request,'movies/movies.html',{'movies':data})
def login(request):
    error_message = ''  # 错误消息
    
    if request.method == 'POST':
        userName=request.POST.get('userName')
        pwd=request.POST.get('pwd')
        user = authenticate(username=userName, password=pwd)
        print(pwd)
        if user is not None:
           
            login(request, user)  # 执行登录操作
            return HttpResponseRedirect('/movies')  # 重定向到主页或其他页面
        else:
            # 密码验证失败
            error_message = 'Invalid username or password.'  # 错误消息
            return render(request, 'movies/login.html', {'error_message': error_message})
    return render(request,'movies/login.html')
def sign(request):
    userName=request.POST.get('userName')
    pwd=request.POST.get('pwd')
    if userName and pwd:
        user = UserTable.objects.create_user(username=userName, password=pwd)
        
        user.save()
        return HttpResponseRedirect('/movies/login')
    return render(request,'movies/sign.html')


