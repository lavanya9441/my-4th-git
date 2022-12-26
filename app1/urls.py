from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[

    path('function1/',function1,name='function1'),
    path('function2/',function2,name='function2'),
]
