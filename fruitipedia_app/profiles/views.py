from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia_app.common.views import get_current_profile
from fruitipedia_app.profiles.forms import CreateProfileForm
from fruitipedia_app.profiles.models import Profile


class CreateProfileView(views.CreateView):
    # model = Profile
    # fields = "__all__"
    form_class = CreateProfileForm
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("dashboard")

    # extra_context = {"current_profile": Profile.objects.all()}


class DetailsProfileView(views.DetailView):
    queryset = Profile.objects.all()

    template_name = "profiles/details-profile.html"

    def get_object(self, queryset=None):
        return get_current_profile()


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()

    fields = ["first_name", "last_name", "image_url", "age"]

    template_name = "profiles/edit-profile.html"

    success_url = reverse_lazy("details profile")

    def get_object(self, queryset=None):
        return get_current_profile()

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["first_name"].label = "First Name"
        form.fields['last_name'].label = "Last Name"

        return form


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()

    template_name = "profiles/delete-profile.html"

    success_url = reverse_lazy("home page")

    def get_object(self, queryset=None):
        return get_current_profile()

