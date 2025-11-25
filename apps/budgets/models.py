from django.db import models
# from apps.users.models import User
# from apps.categories.models import Category


# class Budget(models.Model):
#     PERIOD_TYPE = (
#         ('daily', 'daily'),
#         ('weekly', 'weekly'),
#         ('monthly', 'monthly'),
#         ('yearly', 'yearly'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     budget_limit = models.DecimalField(max_digits=10, decimal_places=2)
#     period_type = models.CharField(max_length=10, choices=PERIOD_TYPE, default="monthly")
#     start_date = models.DateField()
#     end_date = models.DateField()
#     alert_enabled = models.BooleanField(default=True)
#     alert_threshold = models.IntegerField(default=80)

#     class Meta:
#         db_table = "BUDGET"
#         unique_together = ("user", "category", "start_date", "end_date")
#         indexes = [
#             models.Index(fields=["user"]),
#             models.Index(fields=["category"]),
#             models.Index(fields=["start_date", "end_date"]),
#         ]
