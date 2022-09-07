from django.conf.urls.static import static
from django.conf.urls.static import settings
from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name = 'register'),
    path('',views.index,name='main'),
    path('about/',views.about,name='about'),
    path('addpage/',AddPage.as_view(),name = 'add_page'),
    path('contact/',views.contact,name= 'contact'),
    path('post/<int:post_id>/',ShowPost.as_view(),name = 'post'),
    path('category/<int:cat_id>/',views.show_category,name = 'category'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)