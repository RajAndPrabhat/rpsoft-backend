from django.urls import path
from .views import lead_api, ourWork_api, slider_api, client_review_api, ourservice_api, ourtech_api

urlpatterns = [
    path('lead/', lead_api),
    path('lead/<int:pk>', lead_api),
    path('ourwork/', ourWork_api),
    path('ourwork/<int:pk>', ourWork_api),
    path('slider/', slider_api),
    path('slider/<int:pk>', slider_api),
    path('review/', client_review_api),
    path('review/<int:pk>', client_review_api),
    path('ourservice/', ourservice_api),
    path('ourservice/<int:pk>', ourservice_api),
    path('ourtech/', ourtech_api),
    path('ourtech/<int:pk>', ourtech_api),
    
    
]

