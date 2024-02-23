from django.urls import path

from fruitipedia_app.dashboard.views import DashboardView

urlpatterns = (
    path("", DashboardView.as_view(), name="dashboard"),

)