from django.db import models

class Flatbond(models.Model):
    fixed_memebership_fee = models.BooleanField(default=False)
    rent = models.IntegerField()
    postcode = models.CharField(max_length=20, blank=True, null=True)


    @property
    def tax(self):
        """ returns 20% Tax """
        return self.rent * 0.2


    @property
    def membership_fee(self):
        """ returns Membership fee"""
        if self.rent < 100:
            return 120
        else:
            return self.rent + self.tax


    @property
    def fixed_memebership_fee_amount(self):
        """ returns Fixed Membership fee"""
        if self.fixed_memebership_fee == True:
            return self.rent + self.tax
    
    
    def __str__(self):
        return self.postcode
        
