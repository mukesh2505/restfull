from django.urls import path,include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from django.conf.urls  import url
from django.conf import settings
from rest_framework import routers, permissions
router = routers.DefaultRouter()
#router.register(r'Employee_list/',Employee_list),
router.register(r'Employee_details',Employee_details),


urlpatterns = [
	url(r'^', include(router.urls)),

    path('', Base.as_view(), name="base"),

    path('api-auth/', include('rest_framework.urls')),

    #path('Employee_list/', Employee_list.as_view())
  #  path('Employee/<int:pk>/', views.Employee_details.as_view())
   #  path("", views.project_index, name="project_index"),
   #  path("<int:pk>/", views.project_detail, name="project_detail"),
    ]