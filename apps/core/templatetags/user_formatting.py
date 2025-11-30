from django import template
from decimal import Decimal
from ..currency_rates import convert_amount

register = template.Library()

@register.simple_tag
def smart_convert(amount, source_currency, user):
    """
    Converts an amount from Source -> User Preference.
    Usage: {% smart_convert expense.amount expense.currency request.user %}
    """
    if amount is None:
        return ""

    try:
        pref = getattr(user, 'preferences', None)
        target_currency = pref.currency if pref else 'USD'
        
        source = source_currency if source_currency else 'USD'

        converted_val = convert_amount(amount, source, target_currency)

        return format_currency_string(converted_val, target_currency)

    except Exception:
        return f"{amount}"

@register.filter
def currency_display(amount, currency_code):
    """
    Formats a number with the correct symbol. Assumes math is already done.
    Usage: {{ total_spent|currency_display:target_currency }}
    """
    if amount is None:
        return ""
    
    # Default to USD if code is missing
    code = currency_code if currency_code else 'USD'
    return format_currency_string(amount, code)

@register.filter
def user_date(date_obj, user):
    """
    Formats a date string according to user preference.
    """
    if not date_obj:
        return ""
        
    try:
        pref = getattr(user, 'preferences', None)
        fmt_choice = pref.date_format if pref else 'YYYY-MM-DD'
        
        format_map = {
            'YYYY-MM-DD': '%Y-%m-%d',
            'MM/DD/YYYY': '%m/%d/%Y',
            'DD/MM/YYYY': '%d/%m/%Y',
        }
        
        django_fmt = format_map.get(fmt_choice, '%Y-%m-%d')
        return date_obj.strftime(django_fmt)
        
    except Exception:
        return str(date_obj)

def format_currency_string(amount, code):
    try:
        symbols = {
            'USD': '$', 'EUR': '€', 'GBP': '£',
            'JPY': '¥', 'CNY': '¥', 'KHR': '៛',
        }
        symbol = symbols.get(code, code)
        val = float(amount)

        if code == 'KHR':
            return f"{symbol}{int(val):,}"
        else:
            return f"{symbol}{val:,.2f}"
    except:
        return str(amount)