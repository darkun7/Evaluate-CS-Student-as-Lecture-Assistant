from django.db import models

# Create your models here.
class Lab(models.Model):
    name  = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=200, null=True)
    result= models.ForeignKey(Lab ,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    name  = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class TrainingValue(models.Model):
    training_id = models.ForeignKey(Training ,null=True, on_delete=models.SET_NULL)
    attribute_id = models.ForeignKey(Attribute ,null=True, on_delete=models.SET_NULL)
    value = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.training_id)+": "+str(self.attribute_id)+"("+str(self.value)+")"
