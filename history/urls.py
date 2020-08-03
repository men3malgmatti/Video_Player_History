from django.contrib import admin
from django.urls import path
from .views import historyList, StoreToHistory


urlpatterns = [
    path('', historyList),
    path('store/', StoreToHistory)

]
