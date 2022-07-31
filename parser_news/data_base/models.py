from django.db import models

class Title(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name

class Url(models.Model):

    name = models.URLField()

    def __str__(self):
        return self.name


class News(models.Model):

    text = models.TextField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    url = models.ForeignKey(Url, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

