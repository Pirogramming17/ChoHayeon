from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
  path('', views.idealist, name="idealist"),
  path('idearegister', views.idearegister, name="idearegister"),
  path('ideadetail/<int:id>', views.ideadetail, name="ideadetail"),
  path('ideaupdate/<int:id>', views.ideaupdate, name="ideaupdate"),
  path('ideadelete/<int:id>', views.ideadelete, name="ideadelete"),
  path('devtoollist', views.devtoollist, name="devtoollist"),
  path('devtoolregister', views.devtoolregister, name="devtoolregister"),
  path('devtooldetail/<int:id>', views.devtooldetail, name="devtooldetail"),
  path('devtoolupdate/<int:id>', views.devtoolupdate, name="devtoolupdate"),
  path('devtooldelete/<int:id>', views.devtooldelete, name="devtooldelete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)