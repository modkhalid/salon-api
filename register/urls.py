from django.conf.urls import url,include
from django.contrib import admin
from .views import Register
from . import views
app_name="register"
urlpatterns = [
    url(r'^$',views.Register.as_view(),name="register"),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
