# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
import unittest

class FunctionalStore(unittest.TestCase):
    '''тест функциональности магазина'''

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_start(self):
         self.browser.get('http://localhost:8000')

         self.assertIn('Sport Foods', self.browser.title)
         self.fail('Закончить тест!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')