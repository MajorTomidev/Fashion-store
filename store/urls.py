from django.urls import path
from .views import HomePage, DetailPage

urlpatterns = [
    path('<int:pk>/', DetailPage.as_view(), name='details'),
    path('',HomePage.as_view(), name='home'),
    

]