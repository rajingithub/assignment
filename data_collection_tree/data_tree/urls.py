from django.urls import path
from .views import DataInsert,DataQuery


app_name = "data_tree"


urlpatterns = [
    path("v1/insert",DataInsert.as_view()),
    path("v1/query",DataQuery.as_view())
]