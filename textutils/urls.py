from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.index, name='index'),
   path('about', views.about, name='about'),
   path('analyze', views.analyze, name='analyze')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)