from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("fruitipedia_app.common.urls")),
    path("dashboard/", include("fruitipedia_app.dashboard.urls")),
    path("fruit/", include("fruitipedia_app.fruit.urls")),
    path("profile/", include("fruitipedia_app.profiles.urls")),

]
