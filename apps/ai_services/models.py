from django.db import models
# from apps.expenses.models import Expense

# class AiExtraction(models.Model):
#     expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
#     raw_data = models.JSONField()
#     confidence_score = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
#     extraction_method = models.CharField(max_length=50)
#     processed_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = "AI_EXTRACTION"
#         indexes = [
#             models.Index(fields=["expense"]),
#             models.Index(fields=["confidence_score"]),
#             models.Index(fields=["extraction_method"]),
#             models.Index(fields=["processed_at"]),
#         ]

