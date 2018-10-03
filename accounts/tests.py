from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import reverse
from selenium.webdriver.firefox.webdriver import WebDriver

from .models import User


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        User.objects.create_user('some123@mail.ru', '1234qwer')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('login')))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('some123@mail.ru')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('1234qwer')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, reverse('index')))

    def test_make_request(self):
        self.selenium.get('http://127.0.0.1:8000/user/make_request/')
        username_input = self.selenium.find_element_by_name('phone_number')
        username_input.send_keys('+380676666666')
        password_input = self.selenium.find_element_by_name('text')
        password_input.send_keys('1234')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        self.assertEqual(self.selenium.current_url, 'http://127.0.0.1:8000/user/requests_list/')
