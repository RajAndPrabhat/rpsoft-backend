from django.contrib import admin
from .models import Lead, OurWork, Slider, ClientReview, OurService, OurTech

# Register your models here.
@admin.register(Lead)
class LeadModel(admin.ModelAdmin):
    list_display=["id","name","emai_id","phone","message","source","is_active","is_deleted", "created_at","updated_at"]

@admin.register(OurWork)
class OurWorkModel(admin.ModelAdmin):
    list_display=["id","name","image","is_active","is_deleted", "created_at","updated_at"]

@admin.register(Slider)
class SliderModel(admin.ModelAdmin):
    list_display=["id","name","image","title","description","is_active","is_deleted", "created_at","updated_at"]

@admin.register(ClientReview)
class SliderModel(admin.ModelAdmin):
    list_display=["id","client_name","review","is_active","is_deleted", "created_at","updated_at"]

@admin.register(OurService)
class OurServiceModel(admin.ModelAdmin):
    list_display=["id","service_name","service_image","service_description","is_active","is_deleted", "created_at","updated_at"]

@admin.register(OurTech)
class OurTechModel(admin.ModelAdmin):
    list_display=["id","tech_name","tech_image","is_active","is_deleted", "created_at","updated_at"]