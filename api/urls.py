from django.urls import path
from api.views import GetDummyItemAPI

urlpatterns = [
    path('', GetDummyItemAPI.as_view(), name='get-dummy-item'),
]
