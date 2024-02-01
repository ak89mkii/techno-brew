from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group



# Create your models here.

TYPES = (
    ('Inventory', 'Inventory'),
    ('Link', 'Link'),
    ('Tracker', 'Personal Equipment Tracker'),
    ('Wishlist', 'Public Supply Wishlist'),
    ('Tool', 'Tool'),

)

COLORS = (
    ('Dark', 'Dark'),
    ('Light', 'Light')
)

CARDS = (
    ('border-dark', 'White'),
    # ('text-white bg-primary', 'Blue
    # ('text-white bg-secondary', 'Grey'),
    # ('text-white bg-success', 'Green'),
    # ('text-white bg-danger', 'Red'),
    ('border-dark bg-warning', 'Yellow'),
    ('border-dark bg-info', 'Light Blue'),
    ('text-white bg-dark', 'Black')
)


class Link(models.Model):
    description = models.CharField(verbose_name='Description (Link Share) ', max_length=1000, default="None")
    link = models.CharField(verbose_name='Link (Link Share)', max_length=1000, default="None")
    color = models.CharField(
        max_length=30,
        choices=CARDS,
        default=CARDS[0][0]
    )
    timestamp = models.DateField(auto_now_add=True)
    # Also for "owner field"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('home_logged_in')


class Item(models.Model):
    label = models.CharField(max_length=100, default="None")
    description = models.CharField(verbose_name='Description (Link Share) ', max_length=1000, default="None")
    image = models.CharField(max_length=1000, default="/static/07.png")
    type = models.CharField(
        max_length=30,
        choices=TYPES,
        default=TYPES[4][1]
    )
    note = models.CharField(max_length=1000, default="None")
    link = models.CharField(verbose_name='Link (Link Share)', max_length=1000, default="None")
    color = models.CharField(
        max_length=30,
        choices=CARDS,
        default=CARDS[0][0]
    )
    timestamp = models.DateField(auto_now_add=True)
    # Also for "owner field"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # event = models.BooleanField(verbose_name='Public Suppies Wishlist', default=False)    
    favorited = models.BooleanField(verbose_name='Favorited', default=False)
    # wishlist_user = models.BooleanField(verbose_name='Personal Equipment Tracker', default=False)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('home_logged_in')


class Theme(models.Model):
    color = models.CharField(
        max_length=30,
        choices=COLORS,
        default=COLORS[1][1]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('home_logged_in')