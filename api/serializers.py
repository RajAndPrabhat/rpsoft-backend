from rest_framework import serializers
from .models import Lead, OurWork, Slider, ClientReview, OurService, OurTech

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields=["id","name","emai_id","phone","message","source","is_active","is_deleted", "created_at","updated_at"]

class OurWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurWork
        fields=["id","name","image","is_active","is_deleted", "created_at","updated_at"]

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slider
        fields=["id","name","image","title","description","is_active","is_deleted", "created_at","updated_at"]


class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClientReview
        fields=["id","client_name","review","is_active","is_deleted", "created_at","updated_at"]

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurService
        fields=["id","service_name","service_image","service_description","is_active","is_deleted", "created_at","updated_at"]

class OurTechSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurTech
        fields=["id","tech_name","tech_image","is_active","is_deleted", "created_at","updated_at"]