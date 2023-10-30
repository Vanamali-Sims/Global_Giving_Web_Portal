from django.urls import path,include
from test0 import views

urlpatterns = [
       path('homes',views.viewme,name="homes")
]