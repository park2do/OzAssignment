from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model: Review
        fileds = "__all__"
           
