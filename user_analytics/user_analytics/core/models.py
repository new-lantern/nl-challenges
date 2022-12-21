from django.db import models
from hashid_field import HashidAutoField

# List sourced from:
# http://dicomlookup.com/modalities.asp
class Modality(models.TextChoices):
    CT = ("CT", "CT")
    MR = ("MR", "MR")
    XA = ("XA", "XA")
    CR = ("CR", "CR")
    DX = ("DX", "DX")
    PET = ("PET", "PET")
    NM = ("NM", "NM")
    US = ("US", "US")
    RF = ("RF", "RF")
    ECG = ("ECG", "ECG")
    SC = ("SC", "SC")
    MG = ("MG", "MG")

class BodyPart(models.TextChoices):
    ABDOMEN = ("ABDOMEN", "ABDOMEN")
    ANKLE = ("ANKLE", "ANKLE")
    BACK = ("BACK", "BACK")
    BREAST = ("BREAST", "BREAST")
    CHEST = ("CHEST", "CHEST")
    WHOLEBODY = ("WHOLEBODY", "WHOLEBODY")
    FOOT = ("FOOT", "FOOT")
    HAND = ("HAND", "HAND")
    HEAD = ("HEAD", "HEAD")
    HIP = ("HIP", "HIP")
    KNEE = ("KNEE", "KNEE")
    LEG = ("LEG", "LEG")
    NECK = ("NECK", "NECK")
    SHOULDER = ("SHOULDER", "SHOULDER")
    SPINE = ("SPINE", "SPINE")
    ARM = ("ARM", "ARM")
    UTERUS = ("UTERUS", "UTERUS")
    WRIST = ("WRIST", "WRIST")


# Create your models here.
class User(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    subspecialty_modality = models.CharField(max_length=16, choices=Modality.choices, null=True, blank=True)
    subspecialty_body_part = models.CharField(max_length=32, choices=BodyPart.choices, null=True, blank=True)
    sla_goal = models.FloatField(null=True, blank=True)
    revenue_goal = models.PositiveIntegerField(null=True, blank=True)
    studies_goal = models.PositiveIntegerField(null=True, blank=True)

class Study(models.Model):
    id = HashidAutoField(primary_key=True)
    assigned_to = models.ManyToManyField(User, related_name="studies_assigned")
    date = models.DateField(null=True, blank=True)
    revenue = models.PositiveIntegerField(null=True, blank=True)
    modality = models.CharField(max_length=32, choices=Modality.choices, null=True, blank=True)
    body_part = models.CharField(max_length=16, choices=BodyPart.choices, null=True, blank=True)
    sla = models.IntegerField(null=True, blank=True)
