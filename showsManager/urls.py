from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.newShow),
    path('shows/newShow', views.createNewShow),
    path('shows/<int:showId>',views.displayShow),
    path('shows/<int:showId>/edit',views.editShow),
    path('shows/<int:showId>/setEdit', views.setEdit),
    path('shows/<int:showId>/delete', views.delete)
]