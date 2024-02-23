from django.shortcuts import render
from django.views import generic as views

from fruitipedia_app.fruit.models import Fruit


class DashboardView(views.ListView):
    queryset = Fruit.objects.all()

    template_name = "dashboard/dashboard.html"
