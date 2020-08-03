from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(null=True, default='', upload_to="blogimg")
    body = models.TextField()

    def __str__(self):
        return self.title