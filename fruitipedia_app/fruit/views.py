from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia_app.common.views import get_current_profile
from fruitipedia_app.fruit.forms import DeleteFruitForm
from fruitipedia_app.fruit.models import Fruit


class CreateFruitView(views.CreateView):
    queryset = Fruit.objects.all()

    fields = ("name", "image_url", "description", "nutrition")

    template_name = "fruit/create-fruit.html"

    success_url = reverse_lazy("dashboard")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["name"].label = ""
        form.fields["image_url"].label = ""
        form.fields["description"].label = ""
        form.fields['nutrition'].label = ""

        form.fields['name'].widget.attrs['placeholder'] = 'Fruit Name'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        form.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        form.fields['nutrition'].widget.attrs['placeholder'] = 'Nutrition Info'

        return form

    def form_valid(self, form):
        form.instance.owner = get_current_profile()

        return super().form_valid(form)


class DetailsFruitView(views.DetailView):
    queryset = Fruit.objects.all()

    template_name = "fruit/details-fruit.html"


class EditFruitView(views.UpdateView):
    queryset = Fruit.objects.all()

    fields = ["name", "image_url", "description", "nutrition"]

    template_name = "fruit/edit-fruit.html"

    success_url = reverse_lazy("dashboard")


class DeleteFruitView(views.DeleteView):
    queryset = Fruit.objects.all()

    template_name = "fruit/delete-fruit.html"

    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DeleteFruitForm(instance=self.get_object())

        return context


