from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),  # home
    path('detail/', views.show_detail, name="show-detail"),  # show detail
    path('keyword/', views.get_keyword, name="get-keyword"),  # main search
    path('search/', views.search, name="search"),  # sub search
    path('all/', views.get_all, name='all'),  # all orders
]
