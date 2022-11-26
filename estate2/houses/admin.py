from django.contrib import admin
from .models import Amenity,House,Image_of_house,Message,Inquiry,Company,Project,footer_text,about,Code
from .models import Member,Team,Admin,Team_leader,CodePermission
# Register your models here.
admin.site.register(Amenity)
admin.site.register(House)
admin.site.register(Image_of_house)
admin.site.register(Message)
admin.site.register(Inquiry)
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(footer_text)
admin.site.register(about)
admin.site.register(Code)

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Admin)
admin.site.register(Team_leader)
admin.site.register(CodePermission)

