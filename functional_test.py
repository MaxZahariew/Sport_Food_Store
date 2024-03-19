# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class FunctionalStore(unittest.TestCase):
    '''тест функциональности магазина'''

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_start(self):
         self.browser.get('http://localhost:8000')

         self.assertIn('Sport Food', self.browser.title)
         self.fail('Закончить тест!')

    def test_go_admin_home(self):
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)
        bytton_my_profile = self.browser.find_element(By.ID, "my_prof")
        bytton_my_profile.click()
        time.sleep(1)
        bytton_admin_panel = self.browser.find_element(By.ID, "admin_go")
        bytton_admin_panel.click()
        time.sleep(1)
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/admin/login/?next=/admin/')


if __name__ == '__main__':
    unittest.main(warnings='ignore')