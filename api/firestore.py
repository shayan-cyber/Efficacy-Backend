
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 
# Your Firestore Json credentials Goes here
# 

import json

FIREBASE_PRIVATE_KEY ='YOUR_CREDENTIALS_JSON'

cred = credentials.Certificate(FIREBASE_PRIVATE_KEY)
firebase_admin.initialize_app(cred)


db = firestore.client()


def addEvent(event):
    try:
        clubID= event['clubID']
    except:
        clubID = None

    print(clubID)
    event_id =db.collection('Events').add(event)[1].id
    if clubID:
        club = db.collection('Clubs').document(clubID).get()
        # print("club" + club)
        if club.exists:
            db.collection('Clubs').document(clubID).collection('Events').document(event_id).set(event)
    


def getEvents(clubList):
    events = []

    if clubList:
        print("yes")
        for i in clubList['clubList']:
            events_list =db.collection('Clubs').document(i).collection('Events').get()
            for i in events_list:
                data_dict = i.to_dict()
                data_dict['eventID'] = str(i.id)
                events.append(data_dict)      
    else:
        clubs = db.collection('Clubs').get()  
        for doc in clubs:
            events_list = db.collection('Events').get()
            for i in events_list:
                data_dict = i.to_dict()
                data_dict['eventID'] = str(i.id)
                events.append(data_dict)
                    
    return events



def addClub(club):
    db.collection('Clubs').add(club)



def getClubs():
    clubs = db.collection('Clubs').get()
    clubList = []
    for doc in clubs:
        print(doc.id)
        data_dict = doc.to_dict()
        data_dict['clubID'] = str(doc.id)
        clubList.append(data_dict)
    return clubList




def editEvent(data,eventID):
    
    try:
        event = db.collection('Events').document(eventID).get()
        print(eventID)
    
        event_data = event.to_dict()
        clubID = event_data['clubID']
        print(clubID)
       
        if clubID:
            club_event =db.collection('Clubs').document(clubID).collection('Events').document(eventID)
            print(club_event.get().to_dict())
            club_event.update(data)
            print("done")
            # db.collection('Clubs').document(clubID).collection('Events').document(eventID).update(data)
        db.collection('Events').document(eventID).update(data)
        return {"message":"Successfully edited event"}
    except:
        return {"message":"Error editing event"}



def getEventDetails(eventID):
    try:
        event = db.collection('Events').document(eventID).get()
        data_dict = event.to_dict()
        data_dict['eventID'] = str(event.id)
        return {"data":data_dict, "status":200}
    except:
        return {"message":"Error getting event details","status":404}


def getClubDetails(clubID):
    try:
        club = db.collection('Clubs').document(clubID).get()
        data_dict = club.to_dict()
        data_dict['clubID'] = str(club.id)
        return {"data":data_dict, "status":200}
    except:
        return {"message":"Error getting club details","status":404}

def editClubDetails(data,clubID):
    try:
        club = db.collection('Clubs').document(clubID).get()
        data_dict = club.to_dict()
        data_dict['clubID'] = str(club.id)
        db.collection('Clubs').document(clubID).update(data)
        return {"data":data_dict, "status":200}
    except:
        return {"message":"Error editing club details","status":404}




def addContact(contact):
    print("here:")
    print(contact['clubID'])
    print(getClubDetails(contact['clubID'])['status'])
    if getClubDetails(contact['clubID'])['status'] == 200:
        db.collection('Contacts').add(contact)
        return {"message":"Successfully added contact", "status":201}
    else:
        return {"message":"Error adding contact", "status":404}



    # db.collection('Contacts').add(contact)

def getContacts(data):
    if data:
        contacts = db.collection('Contacts').where('clubID','==',data['clubID']).get()
        contactList = []
        print(contacts)
        for doc in contacts:
            data_dict = doc.to_dict()
            data_dict['contactID'] = str(doc.id)
            contactList.append(data_dict)
        return contactList
    else:
        contacts = db.collection('Contacts').get()
        contactList = []
        for doc in contacts:
            data_dict = doc.to_dict()
            data_dict['contactID'] = str(doc.id)
            contactList.append(data_dict)
        return contactList




