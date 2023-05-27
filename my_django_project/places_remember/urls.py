from django.urls import path

from .views import index, add_memory, logout

app_name = 'places_remember social'

urlpatterns = [
    path('', index, name='index'),
    path('add-memory/', add_memory, name='add-memory'),
    path('logout/', logout, name='logout'),
]
