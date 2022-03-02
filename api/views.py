from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import EventSerializer, ClubSerializer, ContactSerializer
from . firestore import (
    addEvent,
    getEvents,
    addClub,
    getClubs,
    editClubDetails,
    editEvent,
    getEventDetails,
    getClubDetails,
    addContact,
    getContacts
    
    )





@api_view(['POST'])
def all_events(request): 
    print(request.data)
    events =getEvents(request.data)
    serializer = EventSerializer(events, many=True)
    return Response( serializer.data, status=200)


    
@api_view(['POST'])
def add_event(request):
    data = request.data
    serializer = EventSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        addEvent(serializer.data)
        
        print(serializer.data)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def add_club(request):
    data = request.data
    serializer = ClubSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        addClub(serializer.data)
        print(serializer.data)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def all_clubs(request):
    clubs = getClubs()
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data, status=200)




@api_view(['POST'])
def edit_event(request, id):
    data = request.data
    message = editEvent(data,id)
    return Response(message)



@api_view(['POST'])
def event_details(request, id):
    event = getEventDetails(id)

    if event['status'] == 200:
        serializer = EventSerializer(event['data'])
        return Response(serializer.data, status=200)
    else:
        return Response(event['message'], status=event['status'])



@api_view(['POST'])
def club_details(request, id):
    club = getClubDetails(id)

    if club['status'] == 200:
        serializer = ClubSerializer(club['data'])
        return Response(serializer.data, status=200)
    else:
        return Response(club['message'], status=club['status'])
@api_view(['POST'])
def edit_club(request, id):
    data = request.data
    message = editClubDetails(data,id)
    return Response(message)


@api_view(['POST'])
def add_contact(request):
    data = request.data
    serializer = ContactSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        resp = addContact(serializer.data)
       
         
        return Response({"message":resp['message']}, status=resp['status'])
    else:
        return Response({"message":"something went wrong"} , status=400)

@api_view(['POST'])
def get_contacts(request):
    try:
        data = request.data
        print(data)
        print(getContacts(data))
        contacts = getContacts(data)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=200)

        
    except:
        return Response({"message":"something went wrong"} , status=400)


@api_view(['GET'])
def api_details(request):
    
    data = {
            "endpoints":{

                "api/all-events":{
                    "method":"POST",
                    "description":"Get all events",
                    "parameters":{
                        
                        "optional":True,
                        "query":"List of clubIDs/ empty list to get all events",
                        

                    }
                },
                "api/add-event":{
                    "method":"POST",
                    "description":"Add event",
                    "parameters":{
                        
                        "optional":False,
                        "query":["clubID", "name","description", "longDescription","duration", "startTime", "endTime","fbPostURL", "googleFormURL", "posterURL", "venue","likeCount", "usersWhoLiked", "contacts"  ]

                    },
                    "example":
                    {
                    "clubID":"ASCK1xjj7qseUmBvLiBc",
                    "name":"Event Onesdsd",
                    "description":"lorem ipsum",
                    "longDescription":"lorem ipsum ipsum",
                    "duration":"du",
                    "startTime":"st",
                    "endTime":"et",
                    "fbPostURL":"fb",
                    "googleFormURL":"gf",
                    "posterURL":"pu",
                    "venue":"vu",
                    "likeCount":5,
                    "contacts":[{
                        "name":"shayan",
                        "email":"deb@gmail.com",
                        "phone":"9365456645"
                    }],
                    "usersWhoLiked":[]
                        
                    }
                    

                },
                "api/add-club":{
                    "method":"POST",
                    "description":"Add club",
                    "parameters":{
                        
                        "optional":False,
                        "query":[ "name","description", "image", "created_at", "logoURL", "fbPageURL", "instagramURL", "linkedinURL", "moderators", "followers"]

                    },
                    "example":{
                        "name":"club1",
                        "description":"lorem ipsum",
                        "image":"chungus.img.com",
                        "created_at":"2020-01-01",
                        "logoURL":"chungus.img.com",
                        "fbPageURL":"fb",
                        "instagramURL":"ig",
                        "linkedinURL":"li",
                        "moderators":[
                            {
                            "name":"shayan",
                            "email":"deb@gmail.com",
                            "phone":"9365456645",
                            "position":"leader"
                            }
                        ],
                        "followers":[1,2,3]

                    }

                },
                "api/all-clubs":{
                    "method":"POST",
                    "description":"Get all clubs",
                },
                "api/edit-event/<eventID>":{
                    "method":"POST",
                    "description":"Edit event",
                    "parameters":{
                        "optional":False,
                        "query":"all-fields"
                    }
                },
                "api/edit-club/<clubID>":{
                    "method":"POST",
                    "description":"Edit event",
                    "parameters":{
                        "optional":False,
                        "query":"all-fields"
                    }
                },
                "api/event-details/<eventID>":{
                    "method":"POST",
                    "description":"Get event details",
                },
                "api/club-details/<clubID>":{
                    "method":"POST",
                    "description":"Get club details",
                },
                "api/add-contact":{
                    "method":"POST",
                    "description":"Add contact",
                    "parameters":{
                        "optional":False,
                        "query":["clubID", "name","email","phone"]
                    }
                },
                "api/get-contacts":{
                    "method":"POST",
                    "description":"Get all contacts",
                }



            }
        }
    
    return Response(data , status=200)