from django.shortcuts import render

from fruitipedia_app.profiles.models import Profile


def get_current_profile():
    return Profile.objects.first() or None


def home_page(request):
    current_profile = get_current_profile()

    if current_profile is None:
        context = {"no_profile": True}
        return render(request, "common/index.html", context)

    return render(request, "common/index.html")



