from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import BooleanField, TextField

# Create your models here.

MEDIATYPE = (
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
  media = models.CharField(
    max_length=2,
    choices=MEDIATYPE,
    default=MEDIATYPE[0][0])
  familiarity = models.IntegerField(
    default=0,
    validators=[MaxValueValidator(5), MinValueValidator(0)]
  )
  description = TextField(max_length=500)
  favorite = BooleanField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)