from django.urls import path
from .views import *


urlpatterns = [
  path('<str:slug>/', blogPage),
  path('<str:slug>/retrieve/', blog_post_detail_view),
  path('<str:slug>/edit/', blog_post_edit_view),
  path('<str:slug>/delete/', blog_post_delete_view),
  path('', blog_post_list_view),
]
