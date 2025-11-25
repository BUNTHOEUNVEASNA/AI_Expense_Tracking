
from django.urls import path
from . import views

# App namespace (use in templates: {% url 'users:login' %})
app_name = 'users'

urlpatterns = [
    # ============================================
    # AUTHENTICATION URLs
    # ============================================
    
    # Register new account
    # URL: /users/register/
    path('register/', views.register_view, name='register'),
    
    # Login to existing account
    # URL: /users/login/
    path('login/', views.login_view, name='login'),
    
    # Logout current user
    # URL: /users/logout/
    path('logout/', views.logout_view, name='logout'),
    
    # ============================================
    # PROFILE & SETTINGS URLs
    # ============================================
    
    # View and edit user profile
    # URL: /users/profile/
    path('profile/', views.profile_view, name='profile'),
    
    # Edit user preferences/settings
    # URL: /users/preferences/
    path('preferences/', views.preferences_view, name='preferences'),
]