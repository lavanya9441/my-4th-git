from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[

    path('function3/',function3,name='function3'),
    path('function4/',function4,name='function4'),
]