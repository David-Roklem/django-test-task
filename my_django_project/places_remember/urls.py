from django.urls import path

from .views import index, add_memory, logout, get_location

app_name = 'places_remember social'

urlpatterns = [
    path('', index, name='index'),
    path('add-memory/', add_memory, name='add-memory'),
    path('get-location/', get_location, name='get-location'),
    path('logout/', logout, name='logout'),
]
