from django.urls import path, include

from fruitipedia_app.fruit.views import CreateFruitView, DetailsFruitView, EditFruitView, DeleteFruitView

urlpatterns = (
    path("create/", CreateFruitView.as_view(), name="create fruit"),
    path("<int:pk>/", include([
                         path("details/", DetailsFruitView.as_view(), name="details fruit"),
                         path("edit/", EditFruitView.as_view(), name="edit fruit"),
                         path("delete/", DeleteFruitView.as_view(), name="delete fruit"),
                            ]),
         ),

)
