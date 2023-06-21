"""my_resume_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_resume_drf_app import views
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'personal_info', views.PersonalInfoViewSet)
router.register(r'skills', views.SkillsViewSet)
router.register(r'tech_stack', views.TechStackViewSet)
router.register(r'employment_history', views.EmploymentHistoryViewSet)
router.register(r'education', views.EducationViewSet)


schema_view = get_schema_view(
        title="My Resume API",
        description="My resume but built with Django REST API and PostgreSQL",
        version="v1"
    )

urlpatterns = [
    path('api/', include(router.urls)),
    path('schema/', schema_view, name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
