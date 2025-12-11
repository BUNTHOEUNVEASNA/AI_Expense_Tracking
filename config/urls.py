from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', include('apps.core.urls')),
    path('', include('apps.core.urls')),
    
    path('users/', include('apps.users.urls')),
    
    path('expenses/', include('apps.expenses.urls')),
    path('categories/', include('apps.categories.urls')),
    path('budgets/', include('apps.budgets.urls')), # Keep this one
    path('ai/', include('apps.ai_services.urls')),
    # path('analytics/', include('apps.analytics.urls')),
    # REMOVE THE DUPLICATE LINE BELOW:
    # path('budgets/', include('apps.budgets.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)