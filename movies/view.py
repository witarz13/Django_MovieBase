from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect

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
    if title and year:
        movie= Movie(title =title, year=year,url=url,info=info)
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


