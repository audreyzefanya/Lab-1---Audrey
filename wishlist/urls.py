from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_XML #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_XML, name='show_XML'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]