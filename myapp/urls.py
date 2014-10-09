from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.startpage, name='startpage'),
    
    url(r'^film/$', views.films, name='films'),    
    url(r'^film/add/$', views.addFilm, name='addfilm'),
    url(r'^film/add/newfilm/$', views.addFilmRes, name='addfilmres'),
    url(r'^film/(?P<film_id>\w+)/delete/$', views.delFilm, name='delfilm'),
    url(r'^film/(?P<film_id>\w+)/$', views.film, name='film'),
    
    url(r'^cinema/$', views.cinemas, name='cinemas'),    
    url(r'^cinema/add/$', views.addCinema, name='addcinema'),
    url(r'^cinema/add/newcinema/$', views.addCinemaRes, name='addcinemares'),
    url(r'^cinema/(?P<cinema_id>\w+)/delete/$', views.delCinema, name='delcinema'),
    url(r'^cinema/(?P<cinema_id>\w+)/$', views.cinema, name='cinema'),
    
    url(r'^session/$', views.sessions, name='sessions'),    
    url(r'^session/add/newsession/$', views.addSessionRes, name='addsessionres'),
    url(r'^session/add/$', views.addSession, name='addsession'),
    url(r'^session/(?P<session_id>\w+)/$', views.session, name='session'),
    url(r'^session/(?P<session_id>\w+)/delete/$', views.delSession, name='delsession'),
    
    url(r'^search-film/$', views.searchFilm),
    url(r'^search-cinema/$', views.searchCinema),
    url(r'^search-session/$', views.searchSession),
    url(r'^search-film/search/$', views.searchFilmRes),
    url(r'^search-cinema/search/$', views.searchCinemaRes),
    url(r'^search-session/search/$', views.searchSessionRes)
    
    
    
)
