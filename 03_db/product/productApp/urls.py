from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name="home"),
   path('<int:product_id>/', views.detail, name="product_detail")
]
