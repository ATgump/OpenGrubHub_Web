Welcome to 454 group website project - Open Table Grub Hub.

To install:

1. pip install -r requirements.txt
2. You may need to install additional stuff for the geopy (found here https://pypi.org/project/geopy/) -- https://gdal.org/ is GDAL install guide this is the main dependency for geopy, but I made some chages to the settings which should mean you don't have to have trouble here but haven't tested installing on a fresh system. 
3. put .env file submitted to blackboard in OpenGrubHub_Web directory
4. from OpenGrubHub_Web directory, python manage.py runserver
5. To demonstrate things you may want to start by making a restaurant then a customer, this will allow you to test the other functionalities - comments and reservations.
