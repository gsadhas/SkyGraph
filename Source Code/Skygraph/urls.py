from django.conf.urls import patterns, url
from Skygraph import views

urlpatterns = patterns('',
      url(r'^$', views.home, name='home'),
      url(r'^area/', views.area, name='area'),
      url(r'^areal/', views.areal, name='areal'),

      url(r'^newy/', views.newy, name='newy'),
      url(r'^newyl/', views.newyl, name='newyl'),

      url(r'^help/', views.help, name='help'),
      url(r'^helpl/', views.helpl, name='helpl'),

      url(r'^data_hotdog/', views.data, name='data'),
      url(r'^list/', views.list, name='list'),

      #url(r'^loggedin/', sessionmgmt.main, name='main'),

      url(r'^losa/', views.losa, name='losa'),
      url(r'^losal/', views.losal, name='losal'),

      url(r'^hous/', views.hous, name='hous'),
      url(r'^housl/', views.housl, name='housl'),

      url(r'^sanf/', views.sanf, name='sanf'),
      url(r'^sanfl/', views.sanfl, name='sanfl'),
      url(r'^account/', views.account, name='account'),

      url(r'^editacc/', views.editacc, name='editacc'),
      url(r'^edituser/', views.edituser, name='edituser'),
     url(r'^widgets/', views.widgets, name='widgets'),
      url(r'^share/', views.share, name='share'),
      url(r'^export/', views.export, name='export'),



    )
