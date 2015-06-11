from django.db import models

# Create your models here.


class DummyData(models.Model):
    # This is a DummyData model to test the database connection of new views.
    number = models.CharField(max_length=100)

    def __unicode__(self):
        # This function defines what the object will return when it's viewed as a whole. In the case of the Django Admin the list will contain the corresponding number.
        return self.number


class Committee(models.Model):
    # This Model defines what a committee consists of.
    acronym = models.CharField(max_length=10)
    longName = models.CharField(max_length=200)
    topic = models.TextField()
    gaPosition = models.CharField(max_length=3, null=True)

    def __unicode__(self):
        # This function defines what the object will return when it's viewed as a whole.
        return self.acronym


class CommitteeStatistic(models.Model):
    # This model will contain the statistical information about the committee it's linked to by the ForeignKey. If AGRI says 5 things about clause 3 that ENVI wrote, this should be saved here with ENVI being the Foreign Key.
    committee = models.ForeignKey(Committee)
    point_resume = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.committee.acronym
