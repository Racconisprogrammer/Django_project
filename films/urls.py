from django.urls import path
from .views import HomePageView, HomePageViewDetail, CreatePageView, UpdatePageView, DeletePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', HomePageViewDetail.as_view(), name='post_detail'),
    path('post/update/<int:pk>/', UpdatePageView.as_view(), name='update_post'),
    path('post/delete  /<int:pk>/', DeletePageView.as_view(), name='delete_post'),
    path('post/new/', CreatePageView.as_view(), name='create_post'),
]
