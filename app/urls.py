from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'), # homepage that lists all blog posts with titles and short descriptions.
    path('detailView/<int:pk>/',views.detailView, name='detailView'),# detailed view page
    path('register/',views.register, name='register'), # register as a blog user 
    path('login/',views.login, name='login'),  #login for bolg post user
    path('logout/',views.logout, name='logout'),
    path('blogerIndex/',views.blogerIndex, name='blogerIndex'), #render where blog user post blog
    path('BlogerView/', views.BlogerView, name="BlogerView"), # blog user see their posts
    path('blogerDeletePost/<int:pk>', views.blogerDeletePost, name="blogerDeletePost"), #blog user delete their posts
    
]
