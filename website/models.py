from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    addrress = models.CharField(max_length=200,null=True,blank=True)
    gender_choice = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHERS'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=gender_choice,
        null=True,blank=True        
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - ({self.user.username})'

class doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - ({self.speciality})'

class availability(models.Model):
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time_choice = [
        ('1', '10:00am - 10:15am'),
        ('2', '10:15am - 10:30am'),
        ('3', '10:30am - 10:45am'),
        ('4', '10:45am - 11:00am'),
        ('5', '11:00am - 11:15am'),
        ('6', '11:15am - 11:30am'),
        ('7', '11:30am - 11:45am'),
        ('8', '11:45am - 12:00pm'),
        ('9', '12:00pm - 12:15pm'),
        ('10', '12:15pm - 12:30pm'),
        ('11', '12:30pm - 12:45pm'),
        ('12', '12:45pm - 1:00pm'),
        ('13', '1:00pm - 1:15pm'),
        ('14', '1:15pm - 1:30pm'),
        ('15', '1:30pm - 1:45pm'),
        ('16', '1:45pm - 2:00pm'),
        ('17', '2:00pm - 2:15pm'),
        ('18', '2:15pm - 2:30pm'),
        ('19', '2:30pm - 2:45pm'),
        ('20', '2:45pm - 3:00pm'),
    ]
    time = models.CharField(
        max_length=2,
        choices=time_choice,
        default='1'    
    )

    class Meta:
        unique_together = ('date', 'time',)


@receiver(post_save, sender=User)
def user_is_created (sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    else:
        instance.profile.save()