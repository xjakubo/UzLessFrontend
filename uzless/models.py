from django.db import models


class PrinterModel(models.Model):
    printerId = models.IntegerField()
    name = models.CharField(max_length=255)
    printerTypeId = models.IntegerField()
    printerQueueId = models.IntegerField()
    printStateId = models.IntegerField()

    def __str__(self):
        return self.name


class ContractorModel(models.Model):
    contractorId = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    nip = models.BigIntegerField()

    def __str__(self):
        return self.fullName
