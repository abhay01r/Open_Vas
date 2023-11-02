from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add-target/', views.add_target, name='add_target'),
    path('start-scan/<int:target_id>/', views.start_scan, name='start_scan'),
    path('download-report/<int:report_id>/', views.download_report, name='download_report'),
]
