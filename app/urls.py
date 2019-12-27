from django.urls import path

from . import views

urlpatterns = [
    path("set_session/",views.set_session,name="set_session"),
    path("get_session/",views.get_session,name="get_session"),
]