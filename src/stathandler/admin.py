from django.contrib import admin

# Register your models here.
from .models import DummyData, Committee, CommitteeStatistic



class CommitteeAdmin(admin.ModelAdmin):
    list_display = ['acronym', 'topic', 'gaPosition']
    search_fields = ['acronym', 'topic', 'gaPosition']


admin.site.register(DummyData)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeStatistic)
