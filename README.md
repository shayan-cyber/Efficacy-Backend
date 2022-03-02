
## API Reference

#### Get API details

```http
  GET /api/api-details/
```


#### Get all events

```http
  GET /api/all-events/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `ClubList` | `List/Array` | **Optional**. List of clubIDs/ empty list to get all events |

#### Add event

```http
  GET /api/add-event/
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

```http
  GET /api/add-club/
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

```http
  GET /api/all-clubs/
```


#### Edit event

```http
  GET /api/edit-event/<eventID>
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

```http
  GET /api/edit-club/<clubID>
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

```http
  GET /api/club-details/<clubID>
```


#### Get event details

```http
  GET /api/event-details/<eventID>
```
