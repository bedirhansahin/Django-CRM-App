from django.db import models


class Record(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_column="Created Date")
    first_name = models.CharField(max_length=50, db_column="First Name")
    last_name = models.CharField(max_length=50, db_column="Last Name")
    email = models.EmailField(max_length=100, db_column="Email")
    phone = models.CharField(max_length=15, db_column="Phone Number")
    country = models.CharField(max_length=150, db_column="Country")
    city = models.CharField(max_length=50, db_column="City")
    zipcode = models.CharField(max_length=20, db_column="Zipcode")

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
        db_table = 'newschema"."record'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
