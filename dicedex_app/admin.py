from django.contrib import admin

from .models import Link, Item, Theme, Member, Dog, Facility

# Register your models here.
admin.site.register(Link)
admin.site.register(Item)
admin.site.register(Theme)
# admin.site.register(Member)
# admin.site.register(Dog)
admin.site.register(Facility)

# Step 2: Configure MemberAdmin with search_fields
class MemberAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'status', 'expiration']  # Make these fields searchable

admin.site.register(Member, MemberAdmin)

# Step 1: Configure DogAdmin with autocomplete_fields
class DogAdmin(admin.ModelAdmin):
    autocomplete_fields = ['member']  # Use autocomplete for the ForeignKey to Member

admin.site.register(Dog, DogAdmin)



# admin.site.register(Gundam)

