from django.conf.urls import include, url
from users.views import dashboard

urlpatterns = [
    url(r"", dashboard, name="dashboard"),
]