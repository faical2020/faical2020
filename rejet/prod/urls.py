from django.contrib import admin
from django.urls import path
from django.views.generic.detail import DetailView

from prod.models.preprod import Preprod
from .views import home,preprod

urlpatterns = [
    path('', home.index,name='hello'),
    path('preprods', preprod.preprod_liste ,name='preprods'),
    path('preprods/create', preprod.CreatePreprod.as_view() ,name='create_preprod'),
    path('preprods/update/<int:pk>', preprod.UpdatePreprod.as_view() ,name='update_preprod'),
    path('preprods/<int:pk>',
    DetailView.as_view(model=Preprod, template_name="prod/preprod/preprod_detail.html"),
    name='detail_preprod'),
]