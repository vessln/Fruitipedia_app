from django.urls import path

from fruitipedia_app.common.views import home_page

urlpatterns = (
    path("", home_page, name="home page"),

)