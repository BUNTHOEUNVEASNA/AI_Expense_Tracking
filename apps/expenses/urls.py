# apps/expenses/urls.py

from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    # Basic CRUD paths (from your traceback)
    path('', views.expense_list, name='list'),
    path('add/', views.expense_create, name='create'), # <-- This is your 'expenses:create'
    path('<int:pk>/edit/', views.expense_update, name='update'),
    path('<int:pk>/delete/', views.expense_delete, name='delete'),
    
    # --- New Paths to fix the NoReverseMatch errors ---
    
    # 1. Voice Input (Missing path)
    path('create/voice/', views.voice_input, name='voice_input'), 
    
    # 2. AI Text Parsing (Missing path)
    path('create/text-parse/', views.text_parse, name='text_parse'),
    
    # --------------------------------------------------
    
    # Receipt Scan Flow
    path('create/receipt/', views.receipt_upload, name='receipt_upload'),
    path('review/<int:pk>/', views.receipt_review, name='review_receipt'),
    path('detail/<int:pk>/', views.expense_detail, name='detail'), 
    
    # Placeholder for manual create (This path leads to manual_create.html)
    # NOTE: The name 'create' is already used by 'add/'. Using 'manual' here is safer, 
    # but based on the nav bar, you intended 'add/' to be the manual form.
    # To fix the nav bar URL, you should remove this duplicate path:
    # path('create/', views.manual_create, name='create'), <--- REMOVE THIS DUPLICATE
]