# Project Explanation


The entire application Urls is within the app `project`.

`Users` App is for Signin, Singup flows and to update User basic details
`music` App is to record user's responses to images and history.

`views.py` contains the whole logic of the APIs .
`serializers.py` contains the logic to convert complex data types like queryset to json

# Assumptions
1. User once can add only one music file.
2. when the user adds the music it is by default private.
3. If the user selects it as the public music file it is displayed to all the other users too.
4. If the user selects to the access to protected users then the user should provide the mail id's. If the user with the mail id presents then it is displayed to the user too else the audio file is not shared with the user.


Documentation below.

### Make a virtual environment

    Recommended python version -----> 3.9.X (The LATEST STABLE RELEASE)
    python -m venv myvenv

### Run the virtual enviroment

    myvenv\Scripts\activate.bat

### Install all dependencies

    pip install  -r requirements.txt

### Migrate

    python manage.py migrate
    
### Run the App
    
    python manage.py runserver

# REST API

The REST API to the  app is described below.


### Create the user

   Create the user with email and password
   
### GET Request
    GET /api/create/
    
It renders to the usercreation form, byproviding valid details user will be created.

## User Login

  User with already having account can be login with credentials.
  
### GET Request
    GET /api/login/

It renders the user login page . By valid credentials user will be logged in.

### PATCH Request

`PATCH /api/users/2/`

---------------------------

## Upload the music files

### GET Request

    GET /api/music/

It renders the music upload form

### POST Request

    POST /api/music/

## Response

    {
        "success": true,
        "message": "Music file successfully uploaded"   
    }

-----------------------------

## Play music

### GET Request

    GET /api/playmusic/

To get the music files all the private, public and protected shared files


### POST Request

    POST /api/playmusic/play/

in get request on clicking the music file it automatically plays the selected music file from the GET Request
