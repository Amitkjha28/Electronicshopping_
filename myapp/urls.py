from django.conf.urls.static import static
from django.urls import path

from Electronicshopping import settings
from myapp import views
urlpatterns = [
    path('',views.myindex,name='myhome' ),
    path('user_login',views.mylogin,name='login' ),
    path('user_sinup',views.mysignup,name='signup' ),
    # path('computer',views.mycomputer,name='comp' ),
    # path('laptop',views.mylaptop,name='lap' ),
    # path('product',views.myproduct,name='pro' ),
    # path('contact',views.mycontact,name='cont' ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)