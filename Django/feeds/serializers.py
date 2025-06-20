from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer

class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer()

    class Meta:
        model = Feed # Feed라는 모델이라는 직렬화 할 것이다.
        fields = "__all__" # Feed의 모든 field를 직렬화 할 것이다. 
        depth = 1 