from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'), # homepage that lists all blog posts with titles and short descriptions.
    path('register/',views.register, name='register'), # register blog user and admin action
    path('login/',views.login, name='login'),  #login for bolg post user
    path('logout/',views.logout, name='logout'),
    path('blogerIndex/',views.blogerIndex, name='blogerIndex'), #render where blog user post blog
    path('detailView/<int:pk>/',views.detailView, name='detailView'),# detailed view page
    
    #Admin Actions 
    path('allUser/',views.allUser,name='allUser'), #Update and Delete Button on this url page
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),

]
