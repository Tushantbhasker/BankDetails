from django.db import models

# Create your models here.
class BankDetails(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=49, blank=True, null=True)
    bank_ifsc = models.CharField(max_length=11, blank=True, null=True)
    bank_branch = models.CharField(max_length=74, blank=True, null=True)
    bank_address = models.CharField(max_length=195, blank=True, null=True)
    bank_city = models.CharField(max_length=50, blank=True, null=True)
    bank_district = models.CharField(max_length=50, blank=True, null=True)
    bank_state = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        db_table = 'bank_details'


