from django.db import models

# Create your models here.
class Specialskills(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    t0 = [
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday'),
    ]
    Day = models.CharField(choices=t0,null=True,blank=True,max_length=30,default="None")
    t1 = [
        ('1-2 hours','1-2 hours'),
        ('Less than 1 hour','Less than 1 hour' ),
        ('None','None'),
    ]
    Cycling = models.CharField(choices=t1,null=True,blank=True,max_length=30,default="None")
    t2 = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    Journaling = models.CharField(choices=t2,null=True,blank=True,max_length=30,default="No")
    t3 = [
        ('Yes','Yes'),
        ('No','No'),
    ]    
    Assignment = models.CharField(choices=t3,null=True,blank=True,max_length=30,default="No")
    t4 = [
        ('1-2 hours','1-2 hours'),
        ('Less than 1 hour','Less than 1 hour'),
        ('None','None'),
    ]
    Workout = models.CharField(choices=t3,null=True,blank=True,max_length=30,default="No")
    t5 = [
        ('Done','Done'),
        ('Not done','Not done'),
    ]
    Grooming = models.CharField(choices=t3,null=True,blank=True,max_length=30,default="Not done")
    updatedat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Special skills"

class Week(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    t1 = [
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday'),
    ]
    Day = models.CharField(choices=t1,null=True,blank=True,max_length=30,default="None")

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural = "Week"

class Contactus(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    context = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural = "Contact Us"

class Workexp(models.Model):
    cmpname = models.CharField(max_length=100,null=True, blank=True)
    position = models.CharField(max_length=100,null=True, blank=True)
    shortdescription = models.CharField(max_length=100,null=True, blank=True)
    updatedat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cmpname + ' ' + self.position

    
    class Meta:
        verbose_name_plural = "Work Exp"

class Education(models.Model):
    edchoices = [
        ('jr','junior'),
        ('sr','senior'),
        ('gr','graduate'),
    ]
    schname = models.CharField(max_length=100,null=True, blank=True)
    hist = models.CharField(choices=edchoices,null=True,blank=True,max_length=10,default="junior")
    position = models.CharField(max_length=100,null=True, blank=True)
    shortdescription = models.CharField(max_length=100,null=True, blank=True)
    updatedat = models.DateTimeField(auto_now=True)
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.schname + ' ' + self.hist

    
    class Meta:
        verbose_name_plural = "Education"
