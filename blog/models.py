from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title  # show title to admin page

    def summary(self):
        return self.body[:100]

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e %Y')


#  Create a blog model
#  add blog app to settings
#   create migrations
