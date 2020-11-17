# Welcome to the documentation of the restaurant api

# Overview

# Register

## Restaurants
To register a restaurant to the api, send a **post** request to the */restaurant/* url.  
The post request should look something like this:  
```json
{
    "restaurant_name": "Dr4kk0nnys Cooking",
    "owner_name": "Dr4kk0nnys",
    "address": "Street, Number, Neighborhood",
    "phone_number": "+00 00 00000-0000",
}
```
***Note***: The api won't be expecting any kind of token or id, since it's a registration and the user won't have any of those yet.  
The response will look like this:  
```json
{
    // TODO
}
```

## Clients

# Update

## Restaurants
To update a restaurant info, send a **put** request to the */restaurant/* url.  
The put request should look something like this:  
```json
{
    "restaurant_name": "Dr4kk0nnys Cooking",
    "owner_name": "Dr4kk0nnys",
    "address": "Street, Number, Neighborhood",
    "phone_number": "+00 00 00000-0000",
    "token_id": "skdjfjhj23h1jkbkj213b4knf9d87asf9d8fhajfkjh3jk2h4jk34jk2h34k2njk1gh28iu",
}
```
The response will look like this:
```json
{
    // TODO
}
```


## Clients

# Delete
To delete a restaurant, send a **delete** request to the */restaurant/* url.  
The delete request should look like this:
```json
{
    "token_id": "djsafh2jk1h32j13h12u3j98013u1u2nj3kj1b23hjv1bv39sd8f0as89fa8ysdhfajfb34j23h4"
}
```
The response should look like this:
```json
{
    // TODO
}
```

# Rate Limit

# Requests

# Urls

# Responses
This is very important, because every time you do a call to the restaurant-register api, you'll receive this very same object.  

*method*
```json
{

}
```

*response*
```json
{
    "success": "true",
    "method": "create",
    "info": {
        "restaurant_name": "Dr4kk0nnys Cooking.",
        "owner_name": "Dr4kk0nnys",
        "address": "Street, street, number, neighborhood",
        "phone_number": "+00 00 00000-0000",
    },

}
```
