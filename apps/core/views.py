from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
import traceback 

# Import Models
from apps.expenses.models import Expense
from apps.budgets.models import Budget
from apps.categories.models import Category
from apps.ai_services.models import AIInsight

from apps.ai_services.utils import generate_weekly_summary

from apps.core.currency_rates import convert_amount 

def home(request):
    """Homepage / Landing page"""
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    try:
        user_prefs = getattr(request.user, 'preferences', None)
        
        if user_prefs and user_prefs.ai_suggestions_enabled:
            today = timezone.now().date()
            
            last_summary_exists = AIInsight.objects.filter(
                user=request.user, 
                insight_type='weekly_summary',
                generated_at__gte=today - timedelta(days=7)
            ).exists()

            if not last_summary_exists:
                generate_weekly_summary(request.user)
        now = timezone.now()
        first_day = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        if hasattr(request.user, 'preferences') and request.user.preferences.ai_suggestions_enabled:
            last_summary_exists = AIInsight.objects.filter(
                user=request.user, 
                insight_type='weekly_summary',
                generated_at__gte=now.date() - timedelta(days=7)
            ).exists()
            if not last_summary_exists:
                generate_weekly_summary(request.user)

        target_curr = getattr(request.user, 'preferences', None) and request.user.preferences.currency or 'USD'

        if hasattr(request.user, 'preferences'):
            target_curr = request.user.preferences.currency

        expenses = Expense.objects.filter(
            user=request.user,
            expense_date__gte=first_day.date(),
            expense_date__lte=now.date()
        ).select_related('category')

        total_spent = 0.0
        category_totals = {}

        for exp in expenses:
            src_curr = exp.currency if hasattr(exp, 'currency') and exp.currency else 'USD'
            converted_val = float(convert_amount(exp.amount, src_curr, target_curr))
            total_spent += converted_val

        # Safely handle missing category
        if exp.category:
            cat_name = exp.category.category_name
            icon = exp.category.icon
            color = exp.category.color
        else:
            cat_name = 'Uncategorized'
            icon = 'fa-question-circle'  # or any default icon
            color = '#6c757d'            # default gray color

        if cat_name not in category_totals:
            category_totals[cat_name] = {
                'name': cat_name,
                'icon': icon,
                'color': color,
                'total': 0.0,
                'count': 0
            }

        category_totals[cat_name]['total'] += converted_val
        category_totals[cat_name]['count'] += 1

        spending_by_category = sorted(category_totals.values(), key=lambda x: x['total'], reverse=True)[:5]
        expense_count = expenses.count()

        recent_expenses = Expense.objects.filter(
            user=request.user
        ).select_related('category').order_by('-expense_date', '-created_at')[:5]

        budgets = Budget.objects.filter(
            user=request.user,
            start_date__lte=now.date(),
            end_date__gte=now.date()
        ).select_related('category')
        
        budget_status = []
        for budget in budgets:
            b_expenses = Expense.objects.filter(
                user=request.user,
                category=budget.category,
                expense_date__gte=budget.start_date,
                expense_date__lte=budget.end_date
            )
            
            budget_original_curr = getattr(budget, 'currency', 'USD')
            limit_original = float(budget.budget_limit)

            spent_original = 0.0
            for be in b_expenses:
                src = be.currency if hasattr(be, 'currency') and be.currency else 'USD'
                val = convert_amount(be.amount, src, budget_original_curr)
                spent_original += float(val)
            
            percentage = (spent_original / limit_original * 100) if limit_original > 0 else 0
            
            spent_display = convert_amount(spent_original, budget_original_curr, target_curr)
            limit_display = convert_amount(limit_original, budget_original_curr, target_curr)
            remaining_display = float(limit_display) - float(spent_display)

            budget_status.append({
                'budget': budget,
                'spent': float(spent_display),         # Now in Target Currency
                'limit_display': float(limit_display), # Now in Target Currency
                'remaining': remaining_display,
                'percentage': round(percentage, 1),
                'status': 'danger' if percentage >= 100 else 'warning' if percentage >= 80 else 'success'
            })

        context = {
            'total_spent': total_spent,
            'expense_count': expense_count,
            'spending_by_category': spending_by_category,
            'recent_expenses': recent_expenses,
            'budget_status': budget_status,
            'current_month': now.strftime('%B %Y'),
            'target_currency': target_curr,
        }

    except Exception as e:
        print(f"ERROR: {e}")
        print(traceback.format_exc())
        context = {
            'error_message': str(e),
            'target_currency': getattr(request.user, 'preferences', None) and request.user.preferences.currency or 'USD'
        }

    return render(request, 'core/dashboard.html', context)

def about(request):
    return render(request, 'core/about.html')