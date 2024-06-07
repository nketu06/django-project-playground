from django.urls import path
from .import views

urlpatterns=[
    path('fee-detail/',views.fees_detail),
]