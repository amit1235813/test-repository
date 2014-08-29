from django.db import models
from django.utils.encoding import smart_text

# Create your models here.
# Test Change to see who the author is
# Test change 2 by amit

class Questions(models.Model):
    question_id = models.CharField(max_length=10, null=False, blank=False)
    question = models.CharField(max_length=1200, null=False, blank=False)
    option_1 = models.CharField(max_length=1200, null=False, blank=False)
    option_2 = models.CharField(max_length=1200, null=False, blank=False)
    option_3 = models.CharField(max_length=1200, null=False, blank=False)
    option_4 = models.CharField(max_length=1200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    timestamp_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_text(self.question_id)