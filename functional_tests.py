from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000/')
        print(self.browser.title)  # 输出页面标题
        # 显式等待直到页面标题包含 'To-Do'
        WebDriverWait(self.browser, 10).until(
            EC.title_contains('To-Do')
        )
        
      # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title),"browser title was " + self.browser.title
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()