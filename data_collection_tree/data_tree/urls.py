from django.urls import path
from .views import DataInsert


app_name = "data_tree"


urlpatterns = [
    path("v1/insert",DataInsert.as_view())
]