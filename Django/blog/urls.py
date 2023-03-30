from django.urls import path

from blog.views import Andijon,home,Fargona

urlpatterns = [
    path("", home),
    path("andijon/", Andijon),
    path("fargona/", Fargona),
]
