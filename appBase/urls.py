from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/v1/', include('address.urls'), name='address'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns +=[
    url(r'^api/v1/auth', include('rest_framework.urls')),
]
