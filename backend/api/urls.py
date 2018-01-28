from django.urls import path
from api import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>/', views.ArtistDetail.as_view()),
    path('paintings/', views.PaintingList.as_view()),
    path('paintings/<int:pk>/', views.PaintingDetail.as_view()),
]