from django.conf.urls.static import static
from django.urls import path

from Electronicshopping import settings
from myapp import views
urlpatterns = [
    path('',views.myindex,name='myhome' ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)