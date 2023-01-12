from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only= True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchList',)
        


class WatchListSerializer(serializers.ModelSerializer):
    #adding custom serializer fields, Also we can add validation like same as below have done 
    # len_name = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many = True,read_only = True)
    platform = serializers.CharField(source = 'platform.name')
    class Meta:
        model = WatchList
        fields = '__all__'
        
    # def get_len_name(self,object):
    #     length = len(object.name)
    #     return length

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many = True,read_only = True) #its for showing every data of watch list(refer drf website)
    # watchlist = serializers.StringRelatedField(many = True)
    class Meta:
        model = StreamPlatform
        fields ='__all__'

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('name is too short!')
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     #validation: Reference (DRF official website, Validation serializers)
    
#     def validate(self,data): #data because total object validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name and description should not be same!')
#         return data
    
    #field level individual validation
    # def validate_name(self,value):#value because field validation
    #     if len(value) < 2:
    #         raise serializers.ValidationError('name is too short!')
    #     return value