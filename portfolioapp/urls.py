from django.urls import path
from portfolioapp import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('blog', views.handleblogs,name='handleblogs'),
]