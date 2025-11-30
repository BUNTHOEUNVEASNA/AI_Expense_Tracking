from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Category
from .forms import CategoryForm

@login_required
def category_list(request):
    """List user's categories"""
    categories = Category.objects.filter(user=request.user).order_by('category_name')
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    """Create a new category"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.is_default = False
            category.save()
            messages.success(request, f"Category '{category.category_name}' created!")
            return redirect('categories:list')
    else:
        form = CategoryForm()
    
    return render(request, 'categories/category_form.html', {
        'form': form,
        'title': 'Add Category'
    })

@login_required
def category_update(request, pk):
    """Edit an existing category"""
    category = get_object_or_404(Category, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('categories:list')
    else:
        form = CategoryForm(instance=category)
        
    return render(request, 'categories/category_form.html', {
        'form': form,
        'title': 'Edit Category'
    })

@login_required
def category_delete(request, pk):
    """Delete a category (Safe Delete)"""
    category = get_object_or_404(Category, pk=pk, user=request.user)
    
    if request.method == 'POST':
        try:
            category.delete()
            messages.success(request, 'Category deleted successfully!')
            return redirect('categories:list')
        except ProtectedError:
            messages.error(request, f"Cannot delete '{category.category_name}' because it contains expenses. Delete those expenses first.")
            return redirect('categories:list')
            
    return render(request, 'categories/category_confirm_delete.html', {'category': category})