from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


Rel_Status_For_Choices = (
    ("single", "Single"),
    ("divorced", "Divorced"),
    ("complicated", "It's Complicated"),
    ("married", "Married"),
)


Looking_For_Choices = (
    ("women", "Women"),
    ("men", "Men"),
    ("both", "Both"),
)


Age_Choices = (
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
    ("24", "24"),
    ("25", "25"),
    ("26", "26"),
    ("27", "27"),
    ("28", "28"),
    ("29", "29"),
    ("30", "30"),
    ("31", "31"),
    ("32", "32"),
    ("33", "33"),
    ("34", "34"),
    ("35", "35"),
    ("36", "36"),
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
    ("47", "47"),
    ("48", "48"),
    ("49", "49"),
    ("50", "50"),
    ("51", "51"),
    ("52", "52"),
    ("53", "53"),
    ("54", "54"),
    ("55", "55"),
    ("56", "56"),
    ("57", "57"),
    ("58", "58"),
    ("59", "59"),
    ("60", "60"),
    ("61", "61"),
    ("62", "62"),
    ("63", "63"),
    ("64", "64"),
    ("65", "65"),
    ("66", "66"),
    ("67", "67"),
    ("68", "68"),
    ("69", "69"),
    ("70", "70"),
    ("71", "71"),
    ("72", "72"),
    ("73", "73"),
    ("74", "74"),
    ("75", "75"),
    ("76", "76"),
    ("77", "77"),
    ("78", "78"),
    ("79", "79"),
    ("80", "80"),
)


class UserProfile(models.Model):
    """
    A user profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    bio = models.TextField(max_length=500, null=False, blank=False)
    age = models.CharField(max_length=80, null=True, blank=True, choices=Age_Choices,
                            default='18')
    relationship_status = models.CharField(max_length=80, null=True, blank=True, choices=Rel_Status_For_Choices,
                            default='Single')
    looking_for = models.CharField(max_length=80, null=True, blank=True, choices=Looking_For_Choices,
                            default='Women')
    image = CloudinaryField('image', default='placeholder')
    job_title = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user
