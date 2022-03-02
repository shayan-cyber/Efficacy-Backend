from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone= serializers.CharField(max_length=100)
    # position = serializers.CharField(max_length=100)
class ModeratorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone= serializers.CharField(max_length=100)
    position = serializers.CharField(max_length=100)


class ClubSerializer(serializers.Serializer):
    clubID = serializers.CharField(read_only=True,required=False)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=100)
    created_at = serializers.CharField()
    logoURL = serializers.CharField(max_length=300)
    fbPageURL = serializers.CharField(max_length=300)
    instagramURL = serializers.CharField(max_length=300)
    linkedinURL = serializers.CharField(max_length=300)
    moderators = ModeratorSerializer(many=True)
    followers = serializers.ListField(
        child = serializers.IntegerField()
    )


    # moderators = ContactSerializer(many=True)


class EventSerializer(serializers.Serializer):
    eventID = serializers.CharField(read_only=True,required=False)
    clubID = serializers.CharField(max_length=100,required=False,allow_blank=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    longDescription = serializers.CharField()
    duration = serializers.CharField(max_length=200)
    startTime = serializers.CharField(max_length=200)
    endTime = serializers.CharField(max_length=200)
    fbPostURL = serializers.CharField(max_length=300)
    googleFormURL = serializers.CharField(max_length=300)
    posterURL = serializers.CharField(max_length=300)
    venue = serializers.CharField(max_length=300)
    likeCount = serializers.IntegerField()
    usersWhoLiked = serializers.ListField(
        child = serializers.IntegerField()
    )
    contacts = ContactSerializer(many=True)



class ClientUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    userID = serializers.CharField(read_only=True,required=False)
    email = serializers.EmailField()
    phone= serializers.CharField(max_length=100)
    scholarID = serializers.CharField(max_length=100,required=False)
    branch = serializers.CharField(max_length=100,required=False)


# class ContactSerializer(serializers.Serializer):
#     clubID = serializers.CharField()
#     name = serializers.CharField(max_length=100)
#     phone_no = serializers.CharField(max_length=10)
#     email = serializers.EmailField()
#     position = serializers.CharField(max_length=100)
    
