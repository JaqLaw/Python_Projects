from django.db import models


class djangoClasses(models.Model):
    # blank=True means that the form the user is filling out can be blank but null=False means that if it is empty,
    # it won't save in the database
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(blank=True, null=False)

    # below is how we make the object show its name rather than 'object(1)'
    objects = models.Manager()

    def __str__(self):
        return self.title