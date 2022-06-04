
**# LOGIN**

**### Request**

POST auth/token/login/

{

"username": "sample",

"password": "badpassword"

}

**### response**

200 OK

{"auth_token": "5b38dca181098a048cf97faf44352d2df4cd042e"}

**# LOGOUT**

**### request**

Requires Authentication

POST auth/token/logout/

**## response**

HTTP_204_NO_CONTENT