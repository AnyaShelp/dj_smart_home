from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=350)

    def __str__(self):
        return str(self.id)


class Temp(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete= models.PROTECT, related_name= "measurements")
    temperature = models.FloatField()
    created_at = models.DateTimeField()

    def __str__(self):
        return {"temperature": 24.5, "created_at": "2021-10-23T16:44:51.432328Z"}
