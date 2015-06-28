from django.contrib import admin

# Register your models here.
from .models import Committee, CommitteeStatistic



class CommitteeAdmin(admin.ModelAdmin):
    # This defines what the Committee Model should look like in the Django Admin
    list_display = ['acronym', 'topic', 'gaPosition']
    search_fields = ['acronym', 'topic', 'gaPosition']



# The following lines are responsible for making the Model Data that's inside the database available in the Django admin

admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeStatistic)
