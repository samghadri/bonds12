from django.db import models

class Flatbond(models.Model):
    fixed_memebership_fee = models.BooleanField(default=False)
    rent = models.IntegerField()


    @property
    def tax(self):
        return self.rent * 0.2

    @property
    def membership_fee(self):
        """ returns Membership fee"""
        return self.rent + self.tax

    @property
    def fixed_memebership_fee_amount(self):
        """ returns Fixed Membership fee"""
        if self.fixed_memebership_fee == True:
            return self.rent - self.tax
        
        
