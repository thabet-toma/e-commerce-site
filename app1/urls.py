from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home),
    path('home', views.home1),
    path('reg', views.reg),
    path('pc', views.pc),
    path('login', views.login),
    path('phones',views.phones),
    path('electronicTool',views.electronicTool),
    path('pro123',views.pro123),
    path('show',views.show),
    path('regProc',views.regProc),
    
]
