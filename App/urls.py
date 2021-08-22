from . import views
from django.urls import path
from .feeds import LatestPostsFeed
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("upload", views.upload, name="upload"),
    path('signup', views.signup, name='signup'), #added
    path('contact', views.contact, name='contact'),
    path('currency', views.currency, name='currency'),
    path('signup', views.signup, name='signup'), #added
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)