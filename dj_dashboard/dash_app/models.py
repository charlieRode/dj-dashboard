from django.db import models




class Profile(models.Model):
    user = models.ForeignKey(User)
    # Profile picture will be stored on AWS's S3
    profile_pic = models.FileField(null=True, blank=True, max_length=150)
    # May need the url 
    url = models.CharField(null=True, max_length=150)
    profile_blurb = models.CharField(null=True, max_length=1000)