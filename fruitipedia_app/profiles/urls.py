from django.urls import path

from fruitipedia_app.profiles.views import CreateProfileView, DetailsProfileView, EditProfileView, DeleteProfileView

urlpatterns = (
    path("create/", CreateProfileView.as_view(), name="create profile"),
    path("details/", DetailsProfileView.as_view(), name="details profile"),
    path("edit/", EditProfileView.as_view(), name="edit profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete profile"),

)