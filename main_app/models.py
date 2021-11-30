from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import BooleanField, TextField

# Create your models here.

MEDIUMTYPE = (
  ("CH", "Charcoal"),
  ("CP", "Colored Pencil"),
  ("IA", "Alcohol Ink"),
  ("II", "India Ink"),
  ("IW", "Water-based Ink"),
  ("GR", "Graphite"),
  ("MA", "Alcohol Marker"),
  ("MW", "Water-based Marker"),
  ("PA", "Acrylic Paint"),
  ("PG", "Gouache Paint"),
  ("PO", "Oil Paint"),
  ("PW", "Watercolor Paint"),
  ("PH", "Hard Pastel"),
  ("OP", "Oil Pastel"),
  ("PP", "Pan Pastel"),
  ("PS", "Soft Pastel"),
  ("BP", "Ballpoint Pen"),
  ("PB", "Brush Pen"),
  ("GE", "Gel Pen"),
  ("PL", "Fineliner Pen"),
  ("PF", "Fountain Pen"),
  ("PE", "Paint Pen"),
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
  favorite = BooleanField("Check this box if you'll use it again")
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("artsupplies_detail", kwargs={"artsupply_id": self.id})


class Photo(models.Model):
  url = models.CharField(max_length=250)
  artsupply = models.ForeignKey(Artsupply, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for artsupply_id: {self.artsupply_id} @{self.url}"