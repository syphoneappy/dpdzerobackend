from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('index/',views.index),
    path('register/',views.create_user),
    path('token/', obtain_auth_token, name='login_user'),
    path("data/",views.store_data),
    path("getdata/",views.get_store_data),
    path("updatedata/",views.update_store_data),
    path("delete/",views.delete_store_data)
]