from django.urls import path,include
from .views import blog_detail, blog_create, blog_update, blog_delete, BlogListView
app_name = 'blog'
urlpatterns = [
    path('list', BlogListView.as_view(), name="list"),
    path('<slug>/', blog_detail, name="detail"),
    path('create', blog_create, name="create"),
    path('<slug>/update', blog_update, name="update"),
    path('<slug>/delete', blog_delete, name="delete"),
]