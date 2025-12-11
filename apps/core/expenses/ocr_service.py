import datetime
from decimal import Decimal
from typing import Dict, Any

# Mocking the OCR process for demonstration purposes.
# In a real app, you would integrate a service here (e.g., Mindee, Google Vision, pytesseract).

def perform_receipt_ocr(receipt_file_path: str) -> Dict[str, Any]:
    """
    Simulates sending a receipt image to an OCR service and getting extracted data.

    Args:
        receipt_file_path: The path to the uploaded image file.

    Returns:
        A dictionary containing the extracted expense fields.
    """
    print(f"Simulating OCR for file: {receipt_file_path}")
    
    # --- MOCK DATA EXTRACTION ---
    # This data would be extracted from the image by the OCR service.
    extracted_data = {
        'amount': Decimal('45.99'),
        'currency': 'USD',
        'expense_date': datetime.date.today(), # Or a date extracted from the image
        'merchant_name': 'SuperMart',
        'description': 'Groceries for the week.',
        'payment_method': 'Credit Card',
        # 'entry_method' is set in the view to 'receipt_scan'
        'category_name': 'Food & Groceries', # Assuming OCR provides a category name
        # 'user' and 'receipt' will be set by the view.
    }
    
    return extracted_data