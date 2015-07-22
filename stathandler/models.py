from django.db import models

# Create models here.


class Committee(models.Model):
    # This Model defines what a committee consists of.
    acronym = models.CharField(max_length=10)
    longName = models.CharField(max_length=200)
    topic = models.TextField()
    gaPosition = models.CharField(max_length=3, null=True)

    def __unicode__(self):
        # This function defines what the object will return when it's viewed as a whole.
        return self.acronym

    class Meta:
        ordering = ["gaPosition"]


class CommitteeStatistic(models.Model):
    # This model will contain the statistical information about the committee it's linked to by the ForeignKey. If AGRI says 5 things about clause 3 that ENVI wrote, this should be saved here with ENVI being the Foreign Key.
    proposingCommittee = models.ForeignKey(Committee)
    # This model will contain the statistical information about the committee it's linked to by the OneToOneField. If AGRI says 5 things about clause 3 that ENVI wrote, this should be saved here with ENVI being the OneToOneField and AGRI the ForeignKey.
    speakingCommittee = models.ForeignKey(Committee, related_name="+")
    pointResume = models.TextField()

    def __unicode__(self):
        return self.pointResume

    class Meta:
        ordering = ["-pk"]
