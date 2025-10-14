from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('csv/', views.csv_table_view, name='csv_table'),
]
