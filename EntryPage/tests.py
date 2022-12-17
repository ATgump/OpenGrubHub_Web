from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from testing_tools.selenium_test_case import SeleniumTestCase
import time

from selenium.webdriver.common.by import By
User = get_user_model()

## Selenium Test Case for User login
class UserLoginFormTests(SeleniumTestCase):
    def test_authentication_form(self):
        # Create a user to login with
        user = User.objects.create_user(
            email="test@user.com", password="12345"
        )

        # Go to the login page
        self.driver.get(self.live_server_url + "/login/")

        # Find HTML elements
        email_input = self.driver.find_element(By.ID,"id_username")
        password_input = self.driver.find_element(By.ID,"id_password")
        login_button = self.driver.find_element(By.ID,"btn-login")

        # TEST: wrong EMAIL correct PASSWORD
        email_input.send_keys("wrong@user.com")
        password_input.send_keys("12345")
        login_button.click()
        
        
        email_input = self.driver.find_element(By.ID,"id_username")
        password_input = self.driver.find_element(By.ID,"id_password")
        login_button = self.driver.find_element(By.ID,"btn-login")
        # RESPONSE
        time.sleep(1)

        # TEST: correct EMAIL wrong PASSWORD
        email_input.clear()
        email_input.send_keys(user.email)
        password_input.clear()
        password_input.send_keys("wrongpass")
        login_button.click()
        # RESPONSE
        time.sleep(1)


        # TEST: VALID LOGIN

        email_input = self.driver.find_element(By.ID,"id_username")
        password_input = self.driver.find_element(By.ID,"id_password")
        login_button = self.driver.find_element(By.ID,"btn-login")
        password_input.clear()
        password_input.send_keys("12345")
        login_button.click()
        # Wait for request
        time.sleep(0.5)
        # Check that the user is logged in
        self.assertEqual(self.driver.current_url, self.live_server_url + "/memberhome/")