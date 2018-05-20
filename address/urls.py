from django.conf.urls import url
from address.views import *

urlpatterns = [
    url(r'^address/$', AddressList.as_view(), name='address')
]