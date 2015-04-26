from django.contrib import admin

# Register your models here.
from .models import DummyData, Committee, CommitteeStatistic

admin.site.register(DummyData)
admin.site.register(Committee)
admin.site.register(CommitteeStatistic)
