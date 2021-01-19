from django.urls import path
from .views import HomeView, AboutView, BlogDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('details/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
]
