from django.db.models import Model, CharField, PositiveSmallIntegerField


# Create your models here.
class Course(Model):
    code = CharField(primary_key=True, max_length=6)
    name = CharField(max_length=50)
    credits = PositiveSmallIntegerField()

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.name, self.credits)
