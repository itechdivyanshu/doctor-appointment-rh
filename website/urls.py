from django.urls import path, include
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('add-appointment/', views.appointment, name="appointment"),
]