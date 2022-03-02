
## API Reference
# API Link: "https://efficacy2back.herokuapp.com/"

#### Get API details

```https
  GET /api/api-details/
```


#### Get all events

```https
  POST /api/all-events/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `ClubList` | `List/Array` | **Optional**. List of clubIDs/ empty list to get all events |

#### Add event

```https
  POST /api/add-event/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`      | `json` | **Required**. clubID, name, description, longDescription, duration, startTime, endTime, fbPostURL, googleFormURL, posterURL, venue, likeCount, usersWhoLiked, contacts  |

##### example: 
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


#### Add club

```https
  POST /api/add-club/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`      | `json` | **Required**. name, description, image, startTime, created_at, logoURL, fbPageURL, instagramURL, linkedinURL, moderators, followers |


##### example:

                      {
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


#### Get all clubs

```https
  POST /api/all-clubs/
```


#### Edit event

```https
  POST /api/edit-event/<eventID>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`      | `json` | **Required**. clubID, name, description, longDescription, duration, startTime, endTime, fbPostURL, googleFormURL, posterURL, venue, likeCount, usersWhoLiked, contacts  |

##### example: 
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

#### Edit club

```https
  POST /api/edit-club/<clubID>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`      | `json` | **Required**. name, description, image, startTime, created_at, logoURL, fbPageURL, instagramURL, linkedinURL, moderators, followers |


##### example:

                      {
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



#### Get club details

```https
  POST /api/club-details/<clubID>
```


#### Get event details

```https
  POST /api/event-details/<eventID>
```
