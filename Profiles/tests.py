from django.test import TestCase
from Profiles.models import User,CustomerProfile,RestaurantProfile

# models test
## test a user creation
class UserTest(TestCase):

    def create_user_c(self, is_customer=True, email="testemail@gmail.com",username="testUN"):
        return User.objects.create(is_customer=is_customer, email=email, username=username)
    def create_user_r(self, is_customer=False,email="testemail2@gmail.com", username="testUN2"):
        return User.objects.create(is_customer=is_customer, email=email, username=username)

    def test_user_creation(self):
        w = self.create_user_c()
        w2 = self.create_user_r()
        self.assertTrue(isinstance(w, User))
        self.assertTrue(isinstance(w2, User))
        self.assertEqual(w.__str__(), w.username)

class CustomerTest(TestCase):
    def create_customer(self, is_customer=True, email="testemail@gmail.com",username="testUN",date_of_birth = "7/20/1997"):
        user = User.objects.create(is_customer=is_customer, email=email, username=username)
        user.customer_profile.date_of_birth = date_of_birth
        return user

    def test_customer_creation(self):
        w = self.create_customer()
        self.assertTrue(isinstance(w, User))
        self.assertTrue(isinstance(w.customer_profile,CustomerProfile))
        self.assertEqual(w.customer_profile.get_absolute_url(),f"/profiles/customer/{w.id}")

## test restaurant creation
class RestaurantTest(TestCase):
    @classmethod
    def create_restaurant(self, is_customer=False, email="testemail@gmail.com",username="testUN",restaurant_name = "mcdonalds", restaurant_address = "123 Test Address Drive", geolocation="90,17"):
        user = User.objects.create(is_customer=is_customer, email=email, username=username)
        user.restaurant_profile.restaurant_name = restaurant_name
        user.restaurant_profile.restaurant_address = restaurant_address
        user.restaurant_profile.geolocation = geolocation
        user.save()
        return user
    @classmethod
    def create_restaurant_no_un(self, is_customer=False, email="test2email@gmail.com",restaurant_name = "mcdonalds", restaurant_address = "123 Test Address Drive", geolocation="90,17"):
        user = User.objects.create(is_customer=is_customer, email=email)
        user.restaurant_profile.restaurant_name = restaurant_name
        user.restaurant_profile.restaurant_address = restaurant_address
        user.restaurant_profile.geolocation = geolocation
        user.save()
        return user
    def test_restaurant_query_set(self):
        from django_google_maps.fields import GeoPt
        w1 = self.create_restaurant()
        w2 = self.create_restaurant(email="test2@gmail.com")
        w3 = self.create_restaurant(email="test3@gmail.com")
        gp = GeoPt(90,17)
        query_set = User.objects.filter(is_customer=False,is_superuser=False)
        self.assertEqual(query_set[2].email,"test3@gmail.com")
        self.assertEqual(query_set[2].username,"testUN")
        self.assertEqual(query_set[2].restaurant_profile.restaurant_name,"mcdonalds")
        self.assertEqual(query_set[2].restaurant_profile.restaurant_address,"123 Test Address Drive")
        self.assertEqual(len(query_set),3)
    def test_restaurant_creation(self):
        w = self.create_restaurant()
        self.assertTrue(isinstance(w, User))
        self.assertTrue(isinstance(w.restaurant_profile,RestaurantProfile))
    def test_get_absolute_url(self):
        w = self.create_restaurant()
        self.assertEqual(w.restaurant_profile.get_absolute_url(),f"/profiles/restaurant/{w.id}")