from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import random
import string
# Create your models here.


def get_rand_string(length):
	letters = string.ascii_lowercase
	res = ''.join(random.choice(letters) for i in range(length))
	return res

choices2 = (('Any', 'Any'),
                ('Building', 'Building'),
                ('Clinic', 'Clinic'),
                ('Food & Beverage', 'Food & Beverage'),
                ('Office', 'Office'),
                ('Retail', 'Retail'),
                ('Shop', 'Shop'),
                ('Store', 'Store'),
                ('Apartment', 'Apartment'),
                ('Chalet', 'Chalet'),
                ('Condo', 'Condo'),
                ('Duplex', 'Duplex'),
                ('Ground Floor', 'Ground Floor'),
                ('iVilla', 'iVilla'),
                ('Multi Family Home', 'Multi Family Home'),
                ('Penthouse', 'Penthouse'),
                ('S Villa', 'S Villa'),
                ('Serviced Apartment', 'Serviced Apartment'),
                ('Single Family Home', 'Single Family Home'),
                ('Sky Loft', 'Sky Loft'),
                ('Studio', 'Studio'),
                ('Townhouse', 'Townhouse'),
                ('Twin House', 'Twin House'),
                ('Villa', 'Villa'))
choices3 = (("Ain Shokana","Ain Shokana"),
                ("Ain Sokhna","Ain Sokhna"),
                ("Alexandria","Alexandria"),
                ("East Cairo","East Cairo"),
                ("Mostakbal City","Mostakbal City"),
                ("New Cairo","New Cairo"),
                ("New Capital","New Capital"),
                ("North Coast","North Coast"),
                ("Sheik Zayed","Sheik Zayed"),
                ("West Cairo","West Cairo"),
                ("6th of October","6th of October"),
                ("New Zayed","New Zayed"))

class Amenity(models.Model):
    status_choices = (
        (_("Balcony"), _("Balcony")),
        (_("Cable TV"), _("Cable TV")),
        (_("Internet"), _("Internet")),
        (_("Tennis Courts"), _("Tennis Courts")),
        (_("Parking"), _("Parking")),
    )
    name = models.CharField(max_length=100,choices=status_choices,verbose_name=_("name"))
    def __str__(self):
        return f"{self.name}"

class Image_of_house(models.Model):
    img = models.ImageField(upload_to="images")
    house = models.ForeignKey("House",on_delete=models.CASCADE,related_name="other_imgs")
    def __str__(self):
        return f"image({self.img})"
"""
class Agent(models.Model):
    name = models.CharField(_("name"),max_length=50)
    age = models.IntegerField(_("age"),)
    email = models.EmailField(_("email"),null=True,blank=True)
    phone = models.CharField(_("phone"),max_length=50,null=True,blank=True)
    skype = models.CharField(_("skype"),null=True,blank=True,max_length=100)
    img = models.ImageField(_("img"),null=True,blank=True,upload_to="images")
    def __str__(self):
        return f"agent ({self.name})"
"""
class House(models.Model):
    status_choices = (
        (_("sale"), _("sale")),
        (_("rent"), _("rent")),
    )

    img = models.ImageField(_("img"),upload_to="images")
    type = models.CharField(max_length=50,choices=choices2,default="Apartment")
    address = models.CharField(_("address"),max_length=50)
    location = models.CharField(max_length=50,choices=choices3,null=True,blank=True)
    status = models.CharField(_("status"),max_length=100,choices=status_choices)
    area = models.IntegerField(_("area"),)
    beds = models.IntegerField(_("beds"),)
    bathrooms = models.IntegerField(_("bathrooms"),)
    garages = models.IntegerField(_("garages"),)
    price = models.IntegerField(_("price"),)
    #agent = models.ForeignKey(Agent,on_delete=models.CASCADE,verbose_name=_("agent"))
    description = models.TextField(_("description"),)
    amenities = models.ManyToManyField(Amenity,verbose_name=_("amenities"))
    company = models.ForeignKey('Company',on_delete=models.CASCADE,blank=True,null=True)
    project = models.ForeignKey('Project',on_delete=models.CASCADE,blank=True,null=True)
    number_of_installments = models.IntegerField(default=1)
    time_of_delivery = models.DateTimeField(null=True,blank=True)
    in_advance_price = models.IntegerField(default=0)
    def __str__(self):
        return f"House ({self.id})==>{self.price}EGP"




class Company(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500,choices=choices3,default='Ain Shokana')
    logo = models.ImageField(upload_to="images",default='houses/real_estate_logo.jpg')
    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    name = models.CharField(max_length=500)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    type = models.CharField(max_length=50, choices=choices2, default="Apartment")
    location = models.CharField(max_length=500, choices=choices3,default='Ain Shokana')
    number_of_units = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"



class Message(models.Model):
    user_name = models.CharField(max_length=50,verbose_name=_("user_name"))
    content = models.TextField(verbose_name=_("content"))
    email = models.EmailField(verbose_name=_("email"))
    #agent = models.ForeignKey(Agent,on_delete=models.CASCADE,verbose_name=_("agent"),null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=30,null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"message from agent({self.user_name})"

class Inquiry(models.Model):
    choices1 = (('buyer','buyer'),
                ('seller','seller'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.all()[0].id)
    buyer_or_seller = models.CharField(max_length=20,choices=choices1,default='buyer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=50, choices=choices3, null=True, blank=True,default='Ain Shokana')
    type = models.CharField(max_length=50, choices=choices2, default="Apartment")
    max_price = models.IntegerField()
    min_size = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

class footer_text(models.Model):
    address = models.CharField(max_length=100,default='Head Office | Building 259, 2nd Sector, North 90th St. New Cairo, Cairo - Egypt.')
    phone = models.CharField(max_length=50,default='Phone . contact@example.com')
    email = models.CharField(max_length=50,default='Email . +54 356 945234')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class about(models.Model):
    first_paragraph = models.CharField(max_length=100,default='We Do Great Design For Creative Folks')
    img1 = models.ImageField(upload_to="images",null=True,blank=True)
    name1 = models.CharField(max_length=50,default='red winners')
    img2 = models.ImageField(upload_to="images",null=True,blank=True)
    since_when = models.CharField(max_length=50,default='Since 2017')
    description1 = models.TextField(default="Enter description 1 here")
    description1 = models.TextField(default="Enter description 2 here")
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
"""
Admin
    Team Leader
        Team member(sales)

"""
class Admin(models.Model):
    pass
class Team_leader(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    codes = models.ManyToManyField('Code',blank=True,null=True)
    def __str__(self):
        return f"team leader ({self.user})"
class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    codes = models.ManyToManyField('Code',blank=True,null=True)
    leader = models.ForeignKey(Team_leader,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"member ({self.user})"
class Team(models.Model):
    pass
    #name = models.CharField(max_length=50)
    #leader = models.ForeignKey(Team_leader,on_delete=models.CASCADE)
    #members = models.ManyToManyField('Member',blank=True,null=True)


def get_default_my_code():
    return get_rand_string(16)
class Code(models.Model):

    value = models.CharField(max_length=50,default=get_default_my_code)
    project = models.OneToOneField(Project,on_delete=models.CASCADE)
    members = models.ManyToManyField(Member,null=True,blank=True)
    time_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    expire_time = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f"({self.project})'s code"

class CodePermission(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    leader = models.ForeignKey(Team_leader,on_delete=models.CASCADE)
    code = models.OneToOneField(Code,on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"({self.code})'s code Permission"