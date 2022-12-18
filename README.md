Welcome to 454 group website project - Open Table Grub Hub.

To install:

1. pip install -r requirements.txt (you may want to do this in a virtual environment there are many dependencies)
2. You may need to install additional stuff for geopy (found here https://pypi.org/project/geopy/) -- https://gdal.org/ is GDAL install guide this is the main dependency for geopy, but I made some chages to the settings which should mean you don't have to have trouble here, nothing was needed when setting this up on windows.
3. put .env file submitted to blackboard in OpenGrubHub_Web directory. This contains my API key. This wouldn't be necessary to hide in production (and in fact is not able to be when using googles API, it is visible in html when making the post request) becuase google allows you to restrict API keys to certain IPs, but, for you to test this I would need to then have to have a webserver running with a static IP which I have neither. So, I am hiding my API key because for now anyone can use it to make reqeusts. 
4. from the OpenGrubHub_Web directory, run the command python manage.py makemigrations then python manage.py migrate -- these commands setup our database from the models we have created.
4. from the OpenGrubHub_Web directory, run the command python manage.py runserver
5. To demonstrate things you may want to start by making a restaurant then a customer, this will allow you to test the other functionalities - comments and reservations.
6. Please send atgump@syr.edu an email if there are any issues.