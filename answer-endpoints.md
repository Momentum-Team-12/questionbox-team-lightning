# Answer Endpoints

## Authenticated Users - create an answer for a specific question

### Request

```json
POST api/questions/<int:question_pk>/answers

{

    "response": "placeholder text, place response within quotes"
}
```

### Response

```json
201 Created

{
  "id": 5,
  "responder": "testuser",
  "question": "This is a question",
  "response": "placeholder text, place response within quotes",
  "accepted": false,
  "created_at": "2022-06-09T14:13:57.793811Z",
  "modified_on": "2022-06-09T14:13:57.793841Z"
}
```

## Get a list of answers associated with a specific question, accessible to unauthenticated users

### Request

```
GET api/questions/<int:question_pk>/answers
```

### Response

```json
200 OK

{
  "id": 5,
  "responder": "testuser",
  "question": "This is a question",
  "response": "placeholder text, place response within quotes",
  "accepted": false,
  "created_at": "2022-06-09T14:13:57.793811Z",
  "modified_on": "2022-06-09T14:13:57.793841Z"
}
```

## View specific answer for a question

### Request

```
GET api/questions/<int:question_pk>/answers/<int:pk>
```

### Response

```json
200 OK

{
  "id": 5,
  "responder": "testuser",
  "question": "This is a question",
  "response": "placeholder text, place response within quotes",
  "accepted": false,
  "created_at": "2022-06-09T14:13:57.793811Z",
  "modified_on": "2022-06-09T14:13:57.793841Z"
}
```

## Authenticated Users - update a specific answer

### Request

```json
PATCH api/questions/<int:question_pk>/answers/<int:pk>

{
	"response": "hey this response updated"
}
```

### Response

```json
200 OK

{
  "id": 5,
  "responder": "testuser",
  "question": "This is a question",
  "response": "hey this response updated",
  "accepted": false,
  "created_at": "2022-06-09T14:13:57.793811Z",
  "modified_on": "2022-06-09T19:14:03.614691Z"
}
```

## Authenticated Users - deletea specific answer

### Request

```json
DELETE api/questions/<int:question_pk>/answers/<int:pk>

{

}
```

### Response

```json
204 No Content

{

}
```

## Authenticated Question Creator - select a specific answer as accepted for their question

### Request

```json
PATCH   api/questions/<int:question_pk>/answers/<int:pk>/accept

{
    "accepted": true
}
```

### Response

```json
200 OK

{
    "accepted": true
}
```

## See answers for a specific user

### Request

```
GET api/user/<int:responder_pk>/answers
```

### Response

```json
200 OK

{
  "id": 5,
  "responder": "testuser",
  "question": "This is a question",
  "response": "placeholder text, place response within quotes",
  "accepted": false,
  "created_at": "2022-06-09T14:13:57.793811Z",
  "modified_on": "2022-06-09T14:13:57.793841Z"
},
{
"id": 11,
    "responder": "testuser",
    "question": "This is a question",
	"response": "yes yes",
	"accepted": false,
	"created_at": "2022-06-09T19:25:28.473378Z",
	"modified_on": "2022-06-09T19:25:28.473414Z"
}
```

## Allow a question creator to select an answer as accepted, default value is set to false.

### Request

```json
POST /api/questions/<int:question_pk>/answers/<int:pk>/accept

{
    "accepted": true
}
```

### Response

```json
200 OK

{
  "accepted": true,
},

```
