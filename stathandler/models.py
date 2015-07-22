from django.db import models

# Create models here.


class Committee(models.Model):
    # This Model defines what a committee consists of.

    # Firstly, it consists of the committees acronym. This could be ENVI or AGRI II as an example. It should not be the long form of the committees name.
    acronym = models.CharField(max_length=10)

    # This is the long name of the committee. It should start with a "the" as the templates do not include it when displayint sentences using the committees long name.
    longName = models.CharField(max_length=200)

    # This is the committees topic. It will be used in list and individual displays.
    topic = models.TextField()

    # This is the position of the committe in GA. The committee with the number 0.1 will be displayed first, the one with number 0.1 second and so on. The tenth committee would be 1 and the eleventh 1.1
    gaPosition = models.CharField(max_length=3, null=True)

    def __unicode__(self):
        # This function defines what the object will return when it's viewed as a whole. This is especially practical for list views.
        return self.acronym

    class Meta:
        # This is used to specify how a list of committees will be ordered. It is most likely always the best thing to order them in the same way as the debates will be held in.
        ordering = ["gaPosition"]


class CommitteeStatistic(models.Model):
    # This model will contain the statistical information about the committee it's linked to by the OneToOneField. If AGRI says 5 things about clause 3 that ENVI wrote, this should be saved here with ENVI being the OneToOneField and AGRI the ForeignKey.

    # This is the committee who is currently presenting its resolution
    proposingCommittee = models.ForeignKey(Committee)

    # This is the committee who is currently commenting on something / making a point
    speakingCommittee = models.ForeignKey(Committee, related_name="+") #The related_name="+" meand that no backwards relation will be created for this ForeignKey. You can not call a set of this in relation to Committe as a cause of this.

    # This is the type of point that has been made. It can either be a DirectResponse or a normal Point at the moment. Of course, there are other types of points but these normally don't contribute to the debate which is why it might be good to leave them out.
    pointType = models.CharField(max_length=20, choices=(("Point", "Point"), ("DirectResponse", "Direct Response")), default="Point")

    # This field stores the contents of what has been said. It should be a (brief) resume of the point that has been made.
    pointResume = models.TextField()

    # This part of the code makes each CommitteeStatistic Object return it's value for its pointResume when called upon without further specification. The reasoning for this is that this is the most unique property of each CommitteeStatistic Object.
    def __unicode__(self):
        return self.pointResume

    class Meta:
        # This defines the behaviour when calling a list of CommitteeStatistic s. It will be ordered with the newest point first in the list as the primary key (pk) increases with each added CommitteeStatistic
        ordering = ["-pk"]
