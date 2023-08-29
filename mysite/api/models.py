from django.db import models


class Sample(models.Model):
    city = models.CharField(
        max_length=50, unique=True, null=False, blank=False, primary_key=True
    )
    link = models.CharField(max_length=500, null=False)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)

    def __str__(self):
        return str(self.city)

    class Meta:
        db_table = '"traveldata"."cities"'
