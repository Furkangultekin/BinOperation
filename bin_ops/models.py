from django.db import models
from django.utils import timezone


class Bin(models.Model):
    bin_id = models.PositiveIntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=2)
    longitude = models.DecimalField(max_digits=7, decimal_places=2)


class Operation(models.Model):
    operation_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=25)


class BinOperation(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    collection_frequency = models.PositiveIntegerField()
    last_collection = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # Automatic save for last_collection datetime
        self.last_collection = timezone.now()
        return super(BinOperation, self).save(*args, **kwargs)
