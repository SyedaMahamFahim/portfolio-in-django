from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class About(models.Model):
    section_title = models.CharField(max_length=150)
    section_description = models.CharField(max_length=255)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    birthday = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    long_description=RichTextUploadingField()
    degree=models.CharField(max_length=150,default="Software Engineer")
    email=models.CharField(max_length=150,default="bakhtwarefahim@gmail.com")
    freelance=models.CharField(max_length=150,default="YES")
    age=models.IntegerField(default=19)
   


    def __str__(self):
        return self.title

class Achievement(models.Model):
    section_title = models.CharField(max_length=150)
    section_description = models.CharField(max_length=255)
    icon_one_title=models.CharField(max_length=150)
    icon_one_number=models.IntegerField(default=19)
    icon_two_title=models.CharField(max_length=150)
    icon_two_number=models.IntegerField(default=19)
    icon_three_title=models.CharField(max_length=150)
    icon_three_number=models.IntegerField(default=19)
    icon_four_title=models.CharField(max_length=150)
    icon_four_number=models.IntegerField(default=19)

    def __str__(self):
        return self.section_title


class Skills(models.Model):
    section_title = models.CharField(max_length=150)
    section_description = models.CharField(max_length=255)
    skill_one=models.CharField(max_length=150)
    skill_two=models.CharField(max_length=150)
    skill_three=models.CharField(max_length=150)
    skill_four=models.CharField(max_length=150)
    skill_five=models.CharField(max_length=150)
    skill_six=models.CharField(max_length=150)
    

    def __str__(self):
        return self.section_title

class Testimonials(models.Model):
    section_title = models.CharField(max_length=150)
    section_description = models.CharField(max_length=255)
    testimonials_name=models.CharField(max_length=150)
    testimonials_description=RichTextUploadingField()
    testimonials_image=models.ImageField(blank=True,upload_to='resume/images/')
   

    def __str__(self):
        return self.testimonials_name
class Services(models.Model):
    section_title = models.CharField(max_length=150)
    section_description = models.CharField(max_length=255)
    services_name=models.CharField(max_length=150)
    services_description=RichTextUploadingField()
    icon_d=models.CharField(max_length=150,default="put")
   

    def __str__(self):
        return self.services_name



class Portfolio(models.Model):
    CATEGORY = (
        ('None', 'None'),
        ('Web Development', 'Web Development'),
        ('Web Designing','Web Designing'),
        ('eCommerce','eCommerce'),
        ('WordPress','WordPress'),
    )
    section_title = models.CharField(max_length=150)
    section_description = models.CharField(max_length=255)
    portfolio_name=models.CharField(max_length=150)
    portfolio_description=RichTextUploadingField()
    category=models.CharField(max_length=100,choices=CATEGORY, default='None')
    image=models.ImageField(blank=True,upload_to='resume/images/')
   

    def __str__(self):
        return self.portfolio_name+"---->"+self.category
