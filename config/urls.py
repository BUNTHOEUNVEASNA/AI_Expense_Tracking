"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ============================================
    # APP URLs - Include all app-specific routes
    # ============================================
    
    # Core app (homepage, dashboard, about)
    path('', include('apps.core.urls')),
    
    # User authentication (login, register, profile)
    path('users/', include('apps.users.urls')),
    
    # Expense management
    path('expenses/', include('apps.expenses.urls')),
    
    # Category management
    # path('categories/', include('apps.categories.urls')),
    
    # Budget management
    # path('budgets/', include('apps.budgets.urls')),
    
    # AI processing features
    # path('ai/', include('apps.ai_services.urls')),
    
    # Analytics and reports
    # path('analytics/', include('apps.analytics.urls')),
]
