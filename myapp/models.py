from django.db import models

class Operator(models.Model):
    operator_name=models.CharField(max_length=100)
    telephone=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    websiteInfo=models.CharField(max_length=50)

    def __str__(self):
        return self.operator_name


class Route(models.Model):
    fromSource=models.CharField(max_length=100)
    toDestination=models.CharField(max_length=100)
    departureTime=models.CharField(max_length=100)
    estimatedArrivalTime=models.CharField(max_length=100)
    firstTakeOff=models.CharField(max_length=100)
    secondTakeOff=models.CharField(max_length=100)
    fare=models.DecimalField(decimal_places=2, max_digits=6)
    description=models.CharField(max_length=300)
    operator=models.ForeignKey(Operator, on_delete=models.CASCADE)

    def _str_(self):
        return "%s-%s" % (self.fromSource, self.toDestination)

class Location(models.Model):
    name=models.CharField(max_length=70)
    town=models.CharField(max_length=50)
    operator_info=models.CharField(max_length=70)
    operators=models.ForeignKey(Operator,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



    