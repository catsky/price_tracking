from django.db import models

class Todo(models.Model):
    title = models.CharField( max_length=255)
    finished = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Product(models.Model):
    productName = models.CharField( max_length=500, blank=True)
    productLink = models.CharField( max_length=500)
    star = models.CharField(max_length=5, blank=True)
    feature = models.CharField(max_length=500, blank=True)
    details = models.CharField(max_length=1000, blank=True)
    originPrice = models.FloatField(default=0, null=True)
    currentPrice = models.FloatField(default=0, null=True)
    crawlDate = models.DateTimeField(null=True, blank=True)
    inStock = models.BooleanField(blank=True)
    firstCommentDate = models.DateTimeField(blank=True, null=True)
    firstComment = models.CharField(max_length=1000, blank=True)
    secondCommentDate = models.DateTimeField(blank=True, null=True)
    secondComment = models.CharField(max_length=1000, blank=True)  
    thirdCommentDate = models.DateTimeField(blank=True, null=True)
    thirdComment = models.CharField(max_length=1000, blank=True)      
    imageLink = models.CharField(max_length=1000, blank=True)


    def __unicode__(self):
        return self.productName

class PriceHistory(models.Model):
    title = models.CharField( max_length=255)
    finished = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class User(models.Model):
    title = models.CharField( max_length=255)
    finished = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Alert(models.Model):
    title = models.CharField( max_length=255)
    finished = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
