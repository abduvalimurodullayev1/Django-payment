from django.urls import path

from .views import prepare, complete

urlpatterns = [
    path("click/prepare/", prepare, ),
    path("click/complete/", complete, ),
]
