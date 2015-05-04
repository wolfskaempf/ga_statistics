from django.db import models

# Create your models here.


class DummyData(models.Model):
    number = models.CharField(max_length=100)

    def __unicode__(self):
        return self.number


class Committee(models.Model):
    acronym = models.CharField(max_length=10)
    longName = models.CharField(max_length=200)
    topic = models.TextField()
    gaPosition = models.CharField(max_length=3, null=True)

    def __unicode__(self):
        return self.acronym


class CommitteeStatistic(models.Model):
    committee = models.ForeignKey(Committee)
    funFactDummy = models.TextField()

    def __unicode__(self):
        return self.committee.acronym
