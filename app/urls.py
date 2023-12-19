from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('blogerIndex/',views.blogerIndex, name='blogerIndex'),
    path('detailView/<int:pk>/',views.detailView, name='detailView'),

]
