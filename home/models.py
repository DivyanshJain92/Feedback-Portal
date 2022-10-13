from random import choices
from django.db import models
import datetime


choiceType = (
            ('1',"General"),
            ('2',"Management Related"),
            ('3',"Job Related"),
            ('4',"Workplace/Culture"),
            ('5',"Other")
        )
# Create your models here.
class Suggestion(models.Model):
    name=models.CharField(max_length=122)
    opt = models.CharField(max_length=25,default = "General Management", editable=False,null=True)
    des=models.TextField()
    sugg = models.TextField()
    
    

    def __str__(self):
        return self.name