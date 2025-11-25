from django.db import models
# from apps.users.models import User
# from apps.categories.models import Category


# class Expense(models.Model):
#     ENTRY_METHOD = (
#         ('manual', 'manual'),
#         ('receipt_scan', 'receipt_scan'),
#         ('voice_input', 'voice_input'),
#         ('text_parsing', 'text_parsing'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.RESTRICT)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     currency = models.CharField(max_length=3, default="USD")
#     expense_date = models.DateField()
#     merchant_name = models.CharField(max_length=100, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     payment_method = models.CharField(max_length=50, null=True, blank=True)
#     entry_method = models.CharField(max_length=20, choices=ENTRY_METHOD, default="manual")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "EXPENSE"
#         indexes = [
#             models.Index(fields=["user"]),
#             models.Index(fields=["category"]),
#             models.Index(fields=["expense_date"]),
#             models.Index(fields=["created_at"]),
#             models.Index(fields=["user", "expense_date"]),
#         ]


# class Receipt(models.Model):
#     expense = models.OneToOneField(Expense, on_delete=models.CASCADE)
#     file_path = models.CharField(max_length=500)
#     file_type = models.CharField(max_length=50)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     ocr_text = models.TextField(null=True, blank=True)

#     class Meta:
#         db_table = "RECEIPT"
#         indexes = [
#             models.Index(fields=["expense"]),
#             models.Index(fields=["uploaded_at"]),
#         ]
