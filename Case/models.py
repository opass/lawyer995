from django.db import models


class Case(models.Model):
    STATUS_UNDO = 1
    STATUS_DOING = 2
    STATUS_DONE = 3

    clientName = models.CharField(max_length=10)
    clientPhone = models.CharField(max_length=12)
    arrestedReason = models.CharField(max_length=300, null=True, blank=True)
    arrestedTime = models.DateTimeField(null=True, blank=True, auto_now=True)
    estimatedArrivedTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    placeDescription = models.CharField(max_length=100, null=True, blank=True)
    placeCounty = models.ForeignKey("Info.County")
    status = models.IntegerField()
    lawyerAssigned = models.ForeignKey("Lawyer.Lawyer", null=True, blank=True)

    def __str__(self):
        return str(self.id) + "_" + self.clientName