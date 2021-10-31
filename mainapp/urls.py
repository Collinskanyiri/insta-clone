from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('', views.index, name='home'),
path('profile/', views.profile, name='profile'),
path('upload/', views.save_image, name='save_img'),
path('like/<int:id>/', views.like_image, name='like'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)