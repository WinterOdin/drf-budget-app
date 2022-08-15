## Django budget app
### important!
Due to beeing overly curious I've used auth method that I didn't use before... You know if the task is done incorrectly at least I learned something new, but this bitted me back. The tests, how do I test with **auth0**? I don't know.(If you know, let me on the secret) If you want to see me using pytest and typing go [here](https://github.com/WinterOdin/weather-data-parser/blob/main/tests.py).

Docker files shoudl be written correctly, I dind't test them. I don't have a space  on C for docker on my private computer and **you can't** install it anywhere else as it is mention on official [github](https://github.com/WinterOdin/weather-data-parser/blob/main/tests.py)

## So what works?
Everything else, not from UI level tho. Due to time constraints I didn't implement evrything on the frontend so for example, filtration (django-filter) it works but directly on the endpoint.

## How to run it
create env, activate it and install dependencies
```
pip install -r requirements.txt
```
create your own super user (to create some dummy data in django admin)
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
#### Why do I need super user
Basically I didn't know if the categories should be custom. I've based my judgment on other app called [wanderlog](https://wanderlog.com/home). They provide their own categories meaning user can't set up custom ones. I've used this app on every trip and I didn't had isse with that so far.

### Running 
- log into djano admin
- create some custom categories
- log out from the admin
- go to http://127.0.0.1:8000/

Here you can create your account or log in via google. It works, after you are logged in create your first wallet and add first entry.

### Api
```
http://127.0.0.1:8000/api/
http://127.0.0.1:8000/swagger/
```
### What is used 
 - DRF
 - Django
 - Django Filter
 - Auth0
 - Swagger
 - ChartJs
 - JQ/JS

### Extra
 - custom range filter for admin view
 - swagger 


### Additional info 
If you feel that code presented here isn't enough I can provide some samples from django based custom shop. App is still running on sqlite not on postgres just for simplicity
