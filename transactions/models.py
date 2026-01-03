from django.db import models
from users.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_status = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    routing_number = models.CharField(max_length=20, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    swift_code = models.CharField(max_length=11, null=True, blank=True)
    transfer_method = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.amount} - {self.transaction_status}"
