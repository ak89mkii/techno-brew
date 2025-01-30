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

# TDI Demo Choices:

STATUS = (
    ('Accepted', 'Accepted'),
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
)

BREED = (
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Pokemon', 'Pokemon'),
    ('Robot', 'Robot'),
)

F_TYPE = (
    ('Government', 'Government'),
    ('Public', 'Public'),
    ('Private', 'Private'),
    ('Death Star', 'Death Star'),
)




# class Link(models.Model):
#     # description = models.CharField(verbose_name='Description', max_length=1000, default="None")
#     # link = models.CharField(verbose_name='Link', max_length=1000, default="None")
#     color = models.CharField(
#         max_length=30,
#         choices=CARDS,
#         default=CARDS[0][0]
#     )
#     timestamp = models.DateField(auto_now_add=True)
#     # Also for "owner field"
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.label

#     def get_absolute_url(self):
#         return reverse('home_logged_in')


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
        return self.description

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

    # This changes the displayed text of the objects in Django admin to the declared field (label).
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
    

# TDI Demo Classes:

# Member Class:
class Member(models.Model):
    # Contact | Base Information (18):
    last_name = models.CharField(max_length=100, default="None")
    first_name = models.CharField(max_length=100, default="None")
    address_street = models.CharField(max_length=1000, default="None")
    city = models.CharField(max_length=1000, default="None")
    state = models.CharField(max_length=1000, default="None")
    zip = models.CharField(max_length=1000, default="None")
    country = models.CharField(max_length=1000, default="None")
    country_code = models.CharField(max_length=5, default="USA")
    region = models.CharField(max_length=1000, default="None")
    phone_primary = models.CharField(max_length=1000, default="None")
    phone_mobile = models.CharField(max_length=1000, default="None")
    email = models.CharField(max_length=100, default="None")
    age_18_plus = models.BooleanField(verbose_name='18 <= Old', default=False)    
    e_newsletter = models.BooleanField(verbose_name='E. Newsletter', default=False)    
    in_house = models.BooleanField(verbose_name='In-House', default=False)    
    registration_p = models.BooleanField(verbose_name='Registration (Prorated)', default=False)    
    registration_n_y = models.BooleanField(verbose_name='Registration (Next Year)', default=False)    
    remove_mailing_list = models.BooleanField(verbose_name='Remove from Mailing List', default=False)    
    no_facility_request = models.BooleanField(verbose_name="Don't Send Facility Requests", default=False)   
    # Membership Information (13):
    # References "Facility" Class.
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)
    owner_id = models.CharField(max_length=1000, default="None")
    web_username = models.CharField(max_length=100, default="None")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    member_since = models.DateField(default="2025-01-01")
    member_status = models.CharField(
        max_length=30,
        choices=STATUS,
        default=STATUS[0][0]
    )
    member_expires = models.DateField(default="2025-01-01")
    evaluator_id = models.CharField(max_length=1000, default="None")
    dsrh_id = models.CharField(max_length=1000, default="None")
    test_score = models.FloatField(max_length=100000, default="None")
    wrong_questions = models.IntegerField(default="None")
    new = models.BooleanField(verbose_name='New Member', default=False)  
    ren = models.BooleanField(verbose_name='Renewed Member', default=False)  
    sent_dvd = models.BooleanField(verbose_name='TWT DVD Sent?', default=False)  
    # Input and Editing Info:
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    timestamp = models.DateField(auto_now_add=True)

    # This changes the displayed text of the objects in Django admin to the declared field (label).
    def __str__(self):
        return f"Last Name: {self.last_name} | First Name: {self.first_name} | Owner ID: {self.owner_id}"

    def get_absolute_url(self):
        return reverse('home_logged_in')


# Dog Class (9):

class Dog(models.Model):
    # References "Member" Class.
    # The "related_name" attribute provides a reverse realtionship from a related model back to the model that holds the ForeignKey, OneToOneField, or ManyToManyField.
    d_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='dogs')
    dog_id = models.CharField(max_length=100, default="None")    
    breed = models.CharField(
        max_length=30,
        choices=BREED,
        default=BREED[0][0]
    )
    dog_name = models.CharField(max_length=100, default="None")
    title = models.CharField(max_length=100, default="None")
    # References "Member" Class.
    modified_on = models.DateTimeField(auto_now=True)
    # modified_on = models.DateTimeField(default="2025-01-01")
    last_printed = models.DateTimeField(default="2025-01-01")
    hrf_date = models.DateField(default="2025-01-01")
    # References "Member" Class.
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # This changes the displayed text of the objects in Django admin to the declared field (label).
    def __str__(self):
        return f"Dog Name: {self.dog_name} | Dog ID: {self.dog_id}"

    def get_absolute_url(self):
        return reverse('home_logged_in')


# Facilities Class (8):

class Facility(models.Model):
    facility_name = models.CharField(max_length=100, default="None")    
    description = models.CharField(max_length=1000, default="None")    
    type = models.CharField(
        max_length=30,
        choices=F_TYPE,
        default=F_TYPE[0][0]
    )    
    address_street = models.CharField(max_length=100, default="None")
    city = models.CharField(max_length=100, default="None")    
    state = models.CharField(max_length=100, default="None")    
    zip = models.CharField(max_length=100, default="None")    
    contact = models.CharField(max_length=100, default="None") 
    phone = models.CharField(max_length=100, default="None")    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)

    # This changes the displayed text of the objects in Django admin to the declared field (facility_name).
    def __str__(self):
        return self.facility_name

    def get_absolute_url(self):
        return reverse('home_logged_in')
   
    



