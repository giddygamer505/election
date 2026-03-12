import os
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from django.urls import reverse
from unittest import skip

class visit_web(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_people_see_candidates(self):
        #people use the web-app "Election"
        self.browser.get(self.live_server_url)

        #They see a big "Election" text
        header = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertIn('Election',header.text)
        

        #They see the first candidate name as a link (Jose Carlo)
        first_candidate = self.browser.find_element(By.TAG_NAME,'a')
        self.assertEqual('Jose Carlo',first_candidate.text)
        time.sleep(1)

        #Someone interest so he click Jose's link
        first_candidate.click()
        time.sleep(1)


        

