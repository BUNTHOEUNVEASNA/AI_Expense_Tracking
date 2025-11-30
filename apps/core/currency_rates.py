import requests
from django.core.cache import cache
from decimal import Decimal, InvalidOperation

FALLBACK_RATES = {
    'USD': 1.0,
    'KHR': 4000.0,
    'EUR': 0.95,
    'GBP': 0.79,
    'JPY': 150.0,
    'CNY': 7.2,
    'THB': 35.0,
    'VND': 24000.0,
}

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
CACHE_KEY = "currency_exchange_rates"
CACHE_TIMEOUT = 86400  

def get_live_rates():
    """
    Fetches rates from Cache first. 
    If missing, fetches from API and saves to Cache.
    If API fails, returns Fallback.
    """
    rates = cache.get(CACHE_KEY)
    if rates:
        return rates

    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status() # Check for errors
        data = response.json()
        
        rates = data.get('rates', {})
        
        cache.set(CACHE_KEY, rates, CACHE_TIMEOUT)
        print("✅  Updated Exchange Rates from API")
        return rates

    except Exception as e:
        print(f"⚠️  Currency API Failed: {e}")
        print("Using Fallback Rates instead.")
        return FALLBACK_RATES

def convert_amount(amount, source_currency, target_currency):
    """
    Converts amount using Live Rates.
    """
    if amount is None or amount == '':
        return Decimal('0.00')
    
    try:
        amount_str = str(amount).replace(',', '').replace(' ', '')
        amount_dec = Decimal(amount_str)
    except (InvalidOperation, ValueError):
        return Decimal('0.00')

    rates = get_live_rates()

    try:
        source_rate = Decimal(str(rates.get(source_currency, 1.0)))
        target_rate = Decimal(str(rates.get(target_currency, 1.0)))
    except:
        source_rate = Decimal('1.0')
        target_rate = Decimal('1.0')

    if source_rate == 0: source_rate = Decimal('1.0')
    
    amount_in_usd = amount_dec / source_rate
    final_amount = amount_in_usd * target_rate

    return final_amount