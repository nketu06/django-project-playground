from django.urls import path
from .import views

urlpatterns=[
    path('fee-detail/',views.fees_detail,name='fee_detail'),
    path('fee-slip',views.fees_slip,name='fee_slip')
]