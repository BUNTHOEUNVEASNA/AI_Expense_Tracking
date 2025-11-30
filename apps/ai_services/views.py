import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AIInsight
from .utils import generate_weekly_summary, check_budget_alerts

@login_required
def insight_list(request):
    """
    View list of all AI-generated insights (Weekly Summaries & Alerts)
    """
    insights = AIInsight.objects.filter(user=request.user).order_by('-generated_at')
    
    for item in insights:
        if isinstance(item.insight_data, str):
            try:
                item.data_dict = json.loads(item.insight_data)
            except json.JSONDecodeError:
                item.data_dict = {}
        else:
            item.data_dict = item.insight_data or {}

    return render(request, 'ai_services/insight_list.html', {'insights': insights})

@login_required
def trigger_analysis(request):
    """
    Manually trigger the AI analysis (Button click)
    """
    generate_weekly_summary(request.user)
    alerts = check_budget_alerts(request.user)
    
    if alerts:
        messages.warning(request, f"Analysis Complete. Found {len(alerts)} budget alerts!")
    else:
        messages.success(request, "Analysis Complete. Weekly summary generated.")
        
    return redirect('ai_services:list')