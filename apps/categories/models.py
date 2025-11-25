from django.db import models
# from apps.users.models import User


# class Category(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category_name = models.CharField(max_length=50)
#     icon = models.CharField(max_length=10, default="📦")
#     color = models.CharField(max_length=7, default="#A8D8EA")
#     is_default = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = "CATEGORY"
#         unique_together = ("user", "category_name")
#         indexes = [
#             models.Index(fields=["user"]),
#             models.Index(fields=["category_name"]),
#         ]
