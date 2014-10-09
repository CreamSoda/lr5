from django.conf.urls import patterns, url
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myapp.models import Film, Cinema, Session

def startpage(request):
    return render(request,'index.html',[])

def films(request):
    film_list = Film.objects.order_by('name')
    context = {'film_list':film_list}
    return render(request, 'films/index.html', context)
    
def cinemas(request):
    cinema_list = Cinema.objects.order_by('name')
    context = {'cinema_list':cinema_list}
    return render(request, 'cinemas/index.html', context)
    
def sessions(request):
    session_list = Session.objects.order_by('start')
    context = {'session_list':session_list}
    return render(request, 'sessions/index.html', context)
    
def film(request, film_id):
    film =  get_object_or_404(Film, pk=film_id)
    return render(request, 'films/film.html', {'film': film})    
        
def cinema(request, cinema_id):
    cinema =  get_object_or_404(Cinema, pk=cinema_id)
    return render(request, 'cinemas/cinema.html', {'cinema': cinema})  
    
def session(request, session_id):
    session =  get_object_or_404(Session, pk=session_id)
    return render(request, 'sessions/session.html' , {'session': session})

def searchFilm(request):
    return render_to_response('films/search.html')
    
def searchCinema(request):
    return render_to_response('cinemas/search.html')
    
def searchSession(request):
    return render_to_response('sessions/search.html')
    
def searchFilmRes(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        film_list = Film.objects.filter(name__icontains=q)
        return render_to_response('films/search_res.html',
            {'film_list': film_list, 'query': q})
    else:
        return HttpResponse('')  
        
def searchCinemaRes(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        cinema_list = Cinema.objects.filter(name__icontains=q)
        return render_to_response('cinemas/search_res.html',
            {'cinema_list': cinema_list, 'query': q})
    else:
        return HttpResponse('')
        
def searchSessionRes(request):
    if 'q1' in request.GET and request.GET['q1']:
        if 'q2' in request.GET and request.GET['q2']:
            q1 = request.GET['q1']
            q2 = request.GET['q2']
            session_list = Session.objects.filter(start__gte=q1)
            session_lisr = session_list.filter(end__gte=q2)
            return render_to_response('sessions/search_res.html',
                {'session_list': session_list, 'query1': q1, 'query2':q2 })
    else:
        return HttpResponse('')
        
        
def addFilm(request):    
    return render_to_response('films/add.html')

def addFilmRes(request):
    if 'N' in request.GET and request.GET['N']:
        if 'D' in request.GET and request.GET['D']:
            film = Film(name=request.GET['N'], description = request.GET['D'])
            film.save(force_insert=True)
    return render_to_response('films/film.html', {'film':film})
    
def addCinema(request):
    return render_to_response('cinemas/add.html')

def addCinemaRes(request):
    if 'N' in request.GET and request.GET['N']: 
        if 'D' in request.GET and request.GET['D']: 
            if 'A' and request.GET['A']:
                cinema = Cinema(name=request.GET['N'], description = request.GET['D'], adress = request.GET['A'])
                cinema.save(force_insert=True)
    return render_to_response('cinemas/cinema.html', {'cinema':cinema})
    
def addSession(request):
    return render_to_response('sessions/add.html')
    
def addSessionRes(request):
    if 'F' in request.GET and request.GET['F'] and 'C' in request.GET and request.GET['C'] and 'st' and request.GET['st'] and 'ed' and request.GET['ed']:
            session = Session(film = Film.objects.filter(name=request.GET['F'])[0], cinema = Cinema.objects.filter(name=request.GET['C'])[0], start = request.GET['st'], end = request.GET['ed'])
            session.save(force_insert=True)
    return render_to_response('sessions/session.html',{'session':session })
    
def delFilm(request, film_id):
    f = get_object_or_404(Film, pk=film_id)
    Session.objects.filter(film=f).delete()
    f.delete()
    return render_to_response('films/del.html')
    
def delCinema(request, cinema_id):
    c = get_object_or_404(Cinema, pk=cinema_id).delete()
    Session.objects.filter(cinema=c).delete()
    c.delete()
    return render_to_response('cinemas/del.html')
    
def delSession(request, session_id):
    get_object_or_404(Session, pk=session_id).delete()
    return render_to_response('sessions/del.html')
    
