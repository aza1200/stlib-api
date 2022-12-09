from django.urls import path
from . import views

urlpatterns = [
    path("", views.Boards.as_view()),
    path("<int:pk>", views.BoardDetail.as_view()),
    path("<int:pk>/comments", views.BoardDetailComments.as_view()),
    path("<int:pk>/photos", views.BoardPhotos.as_view()),
    path("make-error", views.make_error),
]