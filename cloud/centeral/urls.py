from django.contrib import admin
from django.urls import path

from .views import centeralViewSet



urlpatterns = [
    path('centeral', centeralViewSet.as_view({
        'post' : 'list'
    })),
    path('centeral/create', centeralViewSet.as_view({
        'post' : 'create'
    })),
    path('centeral/reserve', centeralViewSet.as_view({
        'post' : 'reserve_fly'
    })),
    path('centeral/filter', centeralViewSet.as_view({
        'post' : 'filter'
    })),
    path('centeral/carrier plane', centeralViewSet.as_view({
        'post' : 'get_planes_of_a_company'
    })),

    ]