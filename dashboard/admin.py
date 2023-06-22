from django.contrib import admin
from .models import SectorType, Society

# Register your models here.
@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'society_name', 'state', 'district', 'registration_date')

@admin.register(SectorType)
class SectorTypeAdmin(admin.ModelAdmin):
    list_display = ('sector_id', 'sector_name')