from kobert import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # kobert 첫페이지
    path("", views.home),
    path("transfer", views.transfer),
  # detail에서 받은 query(url info)를 밑에 경로에서 받을거임
    path('kst_model', views.kst_model, name='info'),

]
