from django.urls import path
from main.views import show_main, create_object_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
     path('create-object-entry', create_object_entry, name='create_object_entry'),
]
