from django.urls import path
from . import views

urlpatterns = [
  path("", views.Home.as_view(), name="home"),
  path("about/", views.about, name="about"),
  path("artsupplies/", views.artsupplies_index, name="artsupplies_index"),
  path("accounts/signup/", views.signup, name="signup"),
  path("artsupplies/<int:artsupply_id>/", views.artsupplies_detail, name="artsupplies_detail"),
  path("artsupplies/create/", views.ArtsupplyCreate.as_view(), name="artsupplies_create"),
  path("artsupplies/<int:pk>/update/", views.ArtsupplyUpdate.as_view(), name="artsupplies_update"),
  path("artsupplies/<int:pk>/delete/", views.ArtsupplyDelete.as_view(), name="artsupplies_delete"),
  path("artsupplies/<int:artsupply_id>/add_photo/", views.add_photo, name="add_photo"),
]