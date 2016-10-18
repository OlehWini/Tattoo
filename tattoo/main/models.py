from __future__ import unicode_literals
from django.utils import timezone
# import datetime
from django.db import models


# Create your models here.


class Article(models.Model):
    header_text = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    pubDate = models.DateTimeField('dataPublished', default=timezone.now)
    photo = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.header_text


class Master(models.Model):
    name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    years_old = models.IntegerField()
    about = models.TextField()
    his_photo = models.FileField(null=True, blank=True)
    experience = models.IntegerField()
    city = models.CharField(max_length=100)
    link_on_works = models.TextField()

    # his_works = models.ForeignKey(MastersWorks, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Topic(models.Model):
    header_text = models.CharField(max_length=100)
    count_of_records = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.header_text


class Record(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text_of_record = models.TextField()
    pub_date = models.DateTimeField('date published')
    