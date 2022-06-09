
# Production URL
https://questionbox-team-lightning.herokuapp.com/



# LOGIN

- ### Request

POST auth/token/login/

{

"username": "sample",

"password": "badpassword"

}

- ***### response***

200 OK

{"auth_token": "5b38dca181098a048cf97faf44352d2df4cd042e"}

- ***# LOGOUT***
- ***### request***

Requires Authentication

POST auth/token/logout/

- ***## response***

HTTP_204_NO_CONTENT

# **QUESTION ENDPOINTS**

## **Request - Returns all questions that have been asked up to this point.**

GET /questions/

## **Request -Returns a specific question.**

GET /questions/<int:pk>/

## **Request** -Adds a new question

POST /questions/

## **Request** -Update part of an existing question

PUT /questions/<int:pk>/

## Request -Updates a question that already exists.

PATCH /questions/<int:pk>/

## **Request** -Delete an existing question

DELETE /questions/<int:pk>/

## **Request** -Returns list of users favorited questions

GET /questions/<int:question_pk>/favorites

## **Request - Returns a list of questions for specific user.**

GET /user/<int:creator_pk>/questions

## **Request -Returns a list of answers to a specific question.**

GET  questions/<int:question_pk>/answers

# **Answer Endpoints**

## **Request**

POST api/questions/<int:question_pk>/answers

## **Request - return answers to a question that a specific user has made.**

POST api/user/<int:responder_pk>/answers/<int:answer_pk>

## **Request - Updates a answer to specific question.**

PATCH api/questions/<int:questions_pk>/answers/<int:answer_pk>

# **User Endpoints**

## **Request -Returns questions that a specific user has asked.**

GET api/user/<int:creator_pk>/questions

## **Request -Returns the favorites of a specific user.**

GET api/user/<int:user_pk>/favorites