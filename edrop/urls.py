from django.contrib import admin
from django.urls import path
from firstapp import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('case/<str:name>/', views.case),
    path( "hello/<str:name>/<str:case>/",views.hello),
    path("", views.index),
    path('accounts/', include('allauth.urls')),
    path('logout/',views.logout_view)
  

]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
