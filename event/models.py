from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import date

Event_Date=(
    ("Upcoming",date.today()),
    ("Past Events",date.today())
)
Category=(
    ('E-Sports', "E-Sports"),
    ('Sports', "Sports"),
    ('Dance', "Dance"),
    ('Music', "Music"),
)

Dept=(
    ('CS','CS'),
    ('BBA','BBA'),
    ('B.Com.','B.Com.'),
)

class Post(models.Model):
    dept = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Event(models.Model):
    id1 = models.IntegerField(primary_key=True)  # AutoField?
    name = models.TextField()
    temail = models.TextField()
    femail = models.TextField()
    body = models.TextField()
    date = models.TextField()
    venue = models.TextField()
    link = models.BinaryField()
    contact = models.TextField()
    category=models.CharField(max_length=25,choices=Category)
    dept=models.CharField(max_length=20,choices=Dept)

    class Meta:
        managed = False
        db_table = 'event'

class EventDetail(models.Model):
    id1 = models.IntegerField()
    email = models.EmailField()

    def publish(self):
        self.save()

    class Meta:
        db_table = 'event_detail'

    # def save(request):
    #     publisher.save()

