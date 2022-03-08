from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

class Investment(models.Model):
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def validate_investment_amount(value):
        if value < 0.0:
            raise ValidationError('%(value)s must be positive', params={'value': value})

    def validate_fee_percentage(value):
        if value < 0.0 or value > 100.0:
            raise ValidationError('%(value)s must be in the range [0.0, 100.0]', params={'value': value})

    user = models.ForeignKey(User, related_name='investments', on_delete=models.CASCADE, null=False)
    investment_amount = models.FloatField(validators=[validate_investment_amount], null=False)
    fee_percentage = models.FloatField(default=0, validators=[validate_fee_percentage])
    investment_date = models.DateField(auto_now_add=True)
    up_front_payed = models.BooleanField(default=False)
    
class Bill(models.Model):
    user = models.ForeignKey(User, related_name='bills', on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=30)
    status = models.CharField(max_length=20, null=False,  default='validated') #status can be validated, sent, paid, overdue  
    bill_date = models.DateField(auto_now_add=True)
    
