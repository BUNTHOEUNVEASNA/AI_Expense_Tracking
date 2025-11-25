from django.db import models
# from apps.users.models import User


# class AiInsight(models.Model):
#     INSIGHT_TYPES = (
#         ('weekly_summary', 'weekly_summary'),
#         ('monthly_summary', 'monthly_summary'),
#         ('budget_alert', 'budget_alert'),
#         ('spending_pattern', 'spending_pattern'),
#         ('prediction', 'prediction'),
#         ('recommendation', 'recommendation'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     insight_type = models.CharField(max_length=30, choices=INSIGHT_TYPES)
#     insight_data = models.JSONField(null=True, blank=True)
#     message = models.TextField()
#     period_start = models.DateField(null=True, blank=True)
#     period_end = models.DateField(null=True, blank=True)
#     generated_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = "AI_INSIGHT"
#         indexes = [
#             models.Index(fields=["user"]),
#             models.Index(fields=["insight_type"]),
#             models.Index(fields=["generated_at"]),
#             models.Index(fields=["user", "insight_type"]),
#         ]
