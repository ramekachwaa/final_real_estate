from .models import House,Message,Inquiry,Project,Company,Code,CodePermission
from django import forms

class CodePermissionForm(forms.ModelForm):
    class Meta:
        model = CodePermission
        fields = "__all__"
        exclude = ('accepted',)

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = "__all__"
        exclude = ('value','expire_time')

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super(HouseForm,self).__init__(*args,**kwargs)
        self.fields["img"].widget.attrs.update({'class': 'form-control'})
        self.fields["img"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["img"].widget.attrs.update({'placeholder': 'img *'})

        self.fields["type"].widget.attrs.update({'class': 'form-control'})
        self.fields["type"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["type"].widget.attrs.update({'placeholder': 'type *'})

        self.fields["location"].widget.attrs.update({'class': 'form-control'})
        self.fields["location"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["location"].widget.attrs.update({'placeholder': 'location *'})

        self.fields["address"].widget.attrs.update({'class': 'form-control'})
        self.fields["address"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["address"].widget.attrs.update({'placeholder': 'address *'})

        self.fields["status"].widget.attrs.update({'class': 'form-control'})
        self.fields["status"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["status"].widget.attrs.update({'placeholder': 'status *'})

        self.fields["area"].widget.attrs.update({'class': 'form-control'})
        self.fields["area"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["area"].widget.attrs.update({'placeholder': 'area *'})

        self.fields["beds"].widget.attrs.update({'class': 'form-control'})
        self.fields["beds"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["beds"].widget.attrs.update({'placeholder': 'beds *'})

        self.fields["bathrooms"].widget.attrs.update({'class': 'form-control'})
        self.fields["bathrooms"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["bathrooms"].widget.attrs.update({'placeholder': 'bathrooms *'})

        self.fields["garages"].widget.attrs.update({'class': 'form-control'})
        self.fields["garages"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["garages"].widget.attrs.update({'placeholder': 'garages *'})

        self.fields["price"].widget.attrs.update({'class': 'form-control'})
        self.fields["price"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["price"].widget.attrs.update({'placeholder': 'price *'})

        self.fields["description"].widget.attrs.update({'class': 'form-control'})
        self.fields["description"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["description"].widget.attrs.update({'placeholder': 'description *'})

        self.fields["amenities"].widget.attrs.update({'class': 'form-control'})
        self.fields["amenities"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["amenities"].widget.attrs.update({'placeholder': 'amenities *'})

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user_name','email','phone_number','project','content']
    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        self.fields["user_name"].widget.attrs.update({'class': 'form-control'})
        self.fields["user_name"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["user_name"].widget.attrs.update({'placeholder': 'Client Name *'})

        self.fields["content"].widget.attrs.update({'class': 'form-control'})
        self.fields["content"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["content"].widget.attrs.update({'placeholder': 'content *'})

        self.fields["email"].widget.attrs.update({'class': 'form-control'})
        self.fields["email"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["email"].widget.attrs.update({'placeholder': 'email *'})

        self.fields["phone_number"].widget.attrs.update({'class': 'form-control'})
        self.fields["phone_number"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["phone_number"].widget.attrs.update({'placeholder': 'Phone Number *'})

        self.fields["project"].widget.attrs.update({'class': 'form-control'})
        self.fields["project"].widget.attrs.update({'style': 'width:100%;'})
        self.fields["project"].widget.attrs.update({'placeholder': 'Phone Number *'})



choices1 = (('Any','Any'),('EG','EGYPT'),('ra','ras elber'),('ua','america'))
choices2 = (('Any','Any'),
            ('Building','Building'),
            ('clinic','clinic'),
            ('Food & Beverage','Food & Beverage'),
            ('Office','Office'),
            ('Retail','Retail'),
            ('Shop','Shop'),
            ('Store','Store'),
            ('Apartment','Apartment'),
            ('Chalet','Chalet'),
            ('Condo','Condo'),
            ('Duplex','Duplex'),
            ('Ground Floor','Ground Floor'),
            ('iVilla','iVilla'),
            ('Multi Family Home','Multi Family Home'),
            ('Penthouse','Penthouse'),
            ('S Villa','S Villa'),
            ('Serviced Apartment','Serviced Apartment'),
            ('Single Family Home','Single Family Home'),
            ('Sky Loft','Sky Loft'),
            ('Studio','Studio'),
            ('Townhouse','Townhouse'),
            ('Twin House','Twin House'),
            ('Villa','Villa'))
choices3 = (("Any","Any"),
            ("Ain Shokana","Ain Shokana"),
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
            ("New Zayed","New Zayed")
                )
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=50,required=False)
    locations = forms.ChoiceField(choices=choices3,required=False)
    type = forms.ChoiceField(choices=choices2,required=False)
    bedrooms = forms.IntegerField(max_value=10,min_value=1)
    bathrooms = forms.IntegerField(max_value=10,min_value=1)
    min_price = forms.IntegerField(min_value=1)
    max_price = forms.IntegerField(min_value=1)
    min_area = forms.IntegerField(min_value=1)
    max_area = forms.IntegerField(min_value=1)
    property_id = forms.IntegerField(required=False)

    def __init__(self,*args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)
        self.fields["keyword"].widget.attrs.update({'placeholder': 'Enter Keyword...'})
        self.fields["keyword"].widget.attrs.update({'class': 'form-control'})
        self.fields["locations"].widget.attrs.update({'placeholder': 'All Locations'})
        self.fields["locations"].widget.attrs.update({'class': 'form-control'})
        self.fields["type"].widget.attrs.update({'placeholder': 'Type'})
        self.fields["bedrooms"].widget.attrs.update({'style': 'width:200px;'})
        self.fields["bedrooms"].widget.attrs.update({'placeholder': 'Bedrooms'})
        self.fields["bathrooms"].widget.attrs.update({'placeholder': 'Bathrooms'})
        self.fields["bathrooms"].widget.attrs.update({'style': 'width:200px;'})
        self.fields["min_price"].widget.attrs.update({'placeholder': 'min_price'})
        self.fields["max_price"].widget.attrs.update({'placeholder': 'max_price'})
        self.fields["min_area"].widget.attrs.update({'placeholder': 'min_area'})
        self.fields["max_area"].widget.attrs.update({'placeholder': 'max_area'})
        self.fields["property_id"].widget.attrs.update({'placeholder': 'Property ID'})

        self.fields["type"].widget.attrs.update({'class': 'form-control'})
        self.fields["bedrooms"].widget.attrs.update({'class': 'form-control'})
        self.fields["bedrooms"].widget.attrs.update({'id': 'beds'})
        self.fields["bathrooms"].widget.attrs.update({'class': 'form-control'})
        self.fields["bathrooms"].widget.attrs.update({'id': 'bathrooms'})
        self.fields["min_price"].widget.attrs.update({'class': 'form-control'})
        self.fields["min_price"].widget.attrs.update({'id': 'min_price'})
        self.fields["max_price"].widget.attrs.update({'class': 'form-control'})
        self.fields["max_price"].widget.attrs.update({'id': 'max_price'})
        self.fields["min_area"].widget.attrs.update({'class': 'form-control'})
        self.fields["min_area"].widget.attrs.update({'id': 'min_area'})
        self.fields["max_area"].widget.attrs.update({'class': 'form-control'})
        self.fields["max_area"].widget.attrs.update({'id': 'max_area'})
        self.fields["property_id"].widget.attrs.update({'class': 'form-control'})

        self.fields["keyword"].widget.attrs.update({'style': 'width:250px;margin:15px 10px'})
        self.fields["locations"].widget.attrs.update({'style': 'width:150px;margin:15px 10px'})
        self.fields["type"].widget.attrs.update({'style': 'width:150px;margin:15px 10px'})
        self.fields["bedrooms"].widget.attrs.update({'style': 'width:155px;margin:15px 10px'})
        self.fields["bathrooms"].widget.attrs.update({'style': 'width:155px;margin:15px 10px'})
        self.fields["min_price"].widget.attrs.update({'style': 'width:150px;margin:15px 10px'})
        self.fields["max_price"].widget.attrs.update({'style': 'width:150px;margin:15px 10px'})
        self.fields["min_area"].widget.attrs.update({'style': 'width:150px;margin:15px 10px'})
        self.fields["max_area"].widget.attrs.update({'style': 'width:150px;margin:15px 10px'})
        self.fields["property_id"].widget.attrs.update({'style': 'width:200px;margin:15px 10px'})

        self.fields['keyword'].label = ""
        self.fields['locations'].label = ""
        self.fields['type'].label = ""
        self.fields['bedrooms'].label = ""
        self.fields['min_price'].label = ""
        self.fields['max_price'].label = ""
        self.fields['min_area'].label = ""
        self.fields['max_area'].label = ""
        self.fields['property_id'].label = ""
        self.fields['bathrooms'].label = ""


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["buyer_or_seller","first_name",
                  "last_name","email",
                  "phone_number","location",
                  "type","max_price",
                  "min_size","beds",
                  "bathrooms"]
    def __init__(self,*args,**kwargs):
        super(InquiryForm,self).__init__(*args,**kwargs)
        self.fields["buyer_or_seller"].widget.attrs.update({'class': 'form-control'})
        self.fields["buyer_or_seller"].widget.attrs.update({'style': 'width:210%;margin:0 48%;'})
        self.fields["buyer_or_seller"].widget.attrs.update({'placeholder': 'I am a'})
        self.fields['buyer_or_seller'].label = "Buyer or Seller"

        self.fields["first_name"].widget.attrs.update({'class': 'form-control'})
        self.fields["first_name"].widget.attrs.update({'style': 'width:50%;margin:0 48%;width:200px;height:50px;'})
        self.fields["first_name"].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['first_name'].label = ""

        self.fields["last_name"].widget.attrs.update({'class': 'form-control'})
        self.fields["last_name"].widget.attrs.update({'style': 'position:absolute;top:77px;left:220px;margin:0 48%;width:200px;height:50px;'})
        self.fields["last_name"].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['last_name'].label = ""

        self.fields["email"].widget.attrs.update({'class': 'form-control'})
        self.fields["email"].widget.attrs.update({'style': 'width:50%;margin:0 48%;width:200px;height:50px;'})
        self.fields["email"].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['email'].label = ""

        self.fields["phone_number"].widget.attrs.update({'class': 'form-control'})
        self.fields["phone_number"].widget.attrs.update({'style': 'position:absolute;top:143px;left:220px;margin:0 48%;width:200px;height:50px;'})
        self.fields["phone_number"].widget.attrs.update({'placeholder': 'Mobile Number'})
        self.fields['phone_number'].label = ""

        self.fields["location"].widget.attrs.update({'class': 'form-control'})
        self.fields["location"].widget.attrs.update({'style': 'width:210%;margin:0 48%;'})
        self.fields["location"].widget.attrs.update({'placeholder': 'location'})
        self.fields['location'].label = "Location"

        self.fields["type"].widget.attrs.update({'class': 'form-control'})
        self.fields["type"].widget.attrs.update({'style': 'width:210%;margin:0 48%;'})
        self.fields["type"].widget.attrs.update({'placeholder': 'type'})
        self.fields['type'].label = "Property Type"

        self.fields["max_price"].widget.attrs.update({'class': 'form-control'})
        self.fields["max_price"].widget.attrs.update({'style': 'width:50%;margin:0 48%;width:200px;height:50px;'})
        self.fields["max_price"].widget.attrs.update({'placeholder': 'Max Price'})
        self.fields['max_price'].label = ""

        self.fields["min_size"].widget.attrs.update({'class': 'form-control'})
        self.fields["min_size"].widget.attrs.update({'style': 'position:absolute;top:365px;left:220px;margin:0 48%;width:200px;height:50px;'})
        self.fields["min_size"].widget.attrs.update({'placeholder': 'Min Size'})
        self.fields['min_size'].label = ""

        self.fields["beds"].widget.attrs.update({'class': 'form-control'})
        self.fields["beds"].widget.attrs.update({'style': 'width:50%;margin:0 48%;width:200px;height:50px;'})
        self.fields["beds"].widget.attrs.update({'placeholder': 'Number of beds'})
        self.fields['beds'].label = ""

        self.fields["bathrooms"].widget.attrs.update({'class': 'form-control'})
        self.fields["bathrooms"].widget.attrs.update({'style': 'position:absolute;top:433px;left:220px;margin:0 48%;width:200px;height:50px;'})
        self.fields["bathrooms"].widget.attrs.update({'placeholder': 'Number of baths'})
        self.fields['bathrooms'].label = ""


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude =('number_of_units',)
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.fields["name"].widget.attrs.update({'class': 'form-control'})
        self.fields["name"].widget.attrs.update({'style': 'width:30%;margin:0 48%;'})
        self.fields["name"].widget.attrs.update({'placeholder': 'Project name'})
        self.fields['name'].label = "Name"

        self.fields["company"].widget.attrs.update({'class': 'form-control'})
        self.fields["company"].widget.attrs.update({'style': 'width:30%;margin:0 48%;'})
        self.fields["company"].widget.attrs.update({'placeholder': 'company name'})
        self.fields['company'].label = "company"

        self.fields["type"].widget.attrs.update({'class': 'form-control'})
        self.fields["type"].widget.attrs.update({'style': 'width:30%;margin:0 48%;'})
        self.fields["type"].widget.attrs.update({'placeholder': 'project type'})
        self.fields['type'].label = "type"

        self.fields["location"].widget.attrs.update({'class': 'form-control'})
        self.fields["location"].widget.attrs.update({'style': 'width:30%;margin:0 48%;'})
        self.fields["location"].widget.attrs.update({'placeholder': 'project location'})
        self.fields['location'].label = "location"


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(CompanyForm,self).__init__(*args,**kwargs)
        self.fields["name"].widget.attrs.update({'class': 'form-control'})
        self.fields["name"].widget.attrs.update({'style': 'width:30%;margin:0 48%;'})
        self.fields["name"].widget.attrs.update({'placeholder': 'Company name'})
        self.fields['name'].label = "Name"


        self.fields["location"].widget.attrs.update({'class': 'form-control'})
        self.fields["location"].widget.attrs.update({'style': 'width:30%;margin:0 48%;'})
        self.fields["location"].widget.attrs.update({'placeholder': 'Company location'})
        self.fields['location'].label = "location"


