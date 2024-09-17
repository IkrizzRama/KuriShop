from django.urls import path
from main.views import show_main, create_object_entry, show_xml, show_json
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-object-entry', create_object_entry, name='create_object_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
