from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/upload-attachment/', views.upload_attachment, name='upload_attachment'),
    path('article/<int:pk>/delete-attachment/<int:attachment_id>/', views.delete_attachment, name='delete_attachment'),
]
