from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('csv/', views.csv_table_view, name='csv_table'),
    # path('ph_calib/', views.ph_calib, name='ph_calib'),
    
    path('calibration_page/', views.calibration_page, name='calibration_page'),
    
    # ph sensor calibration
    path('calibrate/ph/', views.calibration_acid_view, name='calibrate_ph'),

    # do calibration
    path('calibrate/do/', views.calibration_do_view, name='calibrate_do'),

    # ec calibration
    path('calibrate/ec/', views.calibration_ec_view, name='calibrate_ec'),
]
