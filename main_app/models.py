from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import BooleanField, TextField

# Create your models here.

MEDIUMTYPE = (
  ("CH", "Charcoal"),
  ("CP", "Colored Pencil"),
  ("IA", "Ink: Alcohol-based"),
  ("II", "Ink: India"),
  ("IW", "Ink: Water-based"),
  ("MA", "Marker: Alcohol-based"),
  ("MW", "Marker: Water-based"),
  ("PA", "Paint: Acrylic"),
  ("PG", "Paint: Gouache"),
  ("PO", "Paint: Oil"),
  ("PW", "Paint: Watercolor"),
  ("PH", "Pastel: Hard"),
  ("OP", "Pastel: Oil"),
  ("PP", "Pastel: Pan"),
  ("PS", "Pastel: Soft "),
  ("PB", "Pen: Brush nib"),
  ("PL", "Pen: Fineliner"),
  ("PF", "Pen: Fountain"),
)

class Artsupply(models.Model):
  name = models.CharField(max_length = 100)
  brand = models.CharField(max_length = 100)
  medium = models.CharField(
    max_length=2,
    choices=MEDIUMTYPE,
    default=MEDIUMTYPE[0][0])
  familiarity = models.IntegerField(
    "Familiarity on a scale of 0 (first time using this material) to 5 (Regular professional use)",
    default=0,
    validators=[MaxValueValidator(5), MinValueValidator(0)]
  )
  description = TextField(max_length=500)
  favorite = BooleanField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("artsupplies_detail", kwargs={"artsupply_id": self.id})

class Photo(models.Model):
  url = models.CharField(max_length=250)
  artsupply = models.OneToOneField(Artsupply, on_delete=models.CASCADE)
  # image = models.ImageField(upload_to="images/")

  def __str__(self):
    return f"Photo for artsupply_id: {self.artsupply_id} @{self.url}"