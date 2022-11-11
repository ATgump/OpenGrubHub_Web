# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from testing_tools.selenium_test_case import SeleniumTestCase
import time
from .models import ReservationModel
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime

class ReservationFormTests(SeleniumTestCase):
    def test_reservation_form(self):
        # Go to the login page
        self.driver.get(self.live_server_url + "/reservation/create/")

        # # Find HTML elements
        first_name_input = self.driver.find_element(By.ID,"id_first_name")
        last_name_input = self.driver.find_element(By.ID,"id_last_name")
        email_input= self.driver.find_element(By.ID,"id_email")
        time_input = Select(self.driver.find_element(By.ID,"id_time"))
    
        date_input= self.driver.find_element(By.ID,"id_date")
        table_size_input= Select(self.driver.find_element(By.ID,"id_table_size"))
        phone_number_input= self.driver.find_element(By.ID,"id_phone_number")
        high_seat_input= Select(self.driver.find_element(By.ID,"id_high_seat"))
        submit_button = self.driver.find_element(By.ID,"btn-submit")

        ##TEST NORMAL RESERVATION

        first_name_input.send_keys("Avery")
        #time.sleep(2)
        last_name_input.send_keys("Gump")
        #time.sleep(2)
        email_input.send_keys("averygmp@gmail.com")
        #time.sleep(2)
        time_input.select_by_visible_text("6:45 PM")
        #time.sleep(2)
        date_input.send_keys("07/20/22")
        #time.sleep(2)
        table_size_input.select_by_visible_text("6")
       # time.sleep(2)
        phone_number_input.send_keys("+12125552368")
       # time.sleep(2)
        high_seat_input.select_by_visible_text("Yes")
       # time.sleep(2)
        submit_button.click()
        time.sleep(3)
        try:
            reservation = ReservationModel.objects.get(id=1)
            self.assertEqual(reservation.first_name,"Avery")
            self.assertEqual(reservation.last_name,"Gump")
            self.assertEqual(reservation.email,"averygmp@gmail.com")
            self.assertEqual(reservation.time,datetime.time(6,45))
            self.assertEqual(reservation.date,datetime.date(2022,7,20))
            self.assertEqual(reservation.table_size,6)
            self.assertEqual(reservation.phone_number,"+12125552368")
            self.assertEqual(reservation.high_seat,True)
        except:
            print("!!!!!!!!!The reservation did not get saved to DB.!!!!!!!!!!!")

        
        #time.sleep(20)
        #self.assertEqual(self.driver.current_url, self.live_server_url + "/memberhome/")