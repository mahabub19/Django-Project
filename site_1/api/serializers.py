from rest_framework import serializers
from media.models import post,type,review
from users.models import profile


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=type
        fields = '__all__'

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=False)
    class Meta:
        model= review
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(many=False)
    post_type = TypeSerializer(many=True)
    feedback = serializers.SerializerMethodField() 
    
    class Meta:
        model = post
        fields = '__all__'
    
    def get_feedback(self,obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews,many = True)
        return serializer.data 