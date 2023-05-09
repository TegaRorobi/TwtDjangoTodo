from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('<int:id>/',views.index ,name='index'),
    path('',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('create/',views.create,name='create'),
    path('delete/',views.delete,name='delete'),
    path('my_logout/',views.logout,name='logout'),
] 