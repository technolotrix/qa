import unittest
from selenium import webdriver
import page

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get("http://nicolesmith.nyc")
        self.driver.get("http://127.0.0.1:4747")

    def test_title_on_homepage(self):
        main_page = page.HomePage(self.driver)
        assert main_page.is_title_matches(), "homepage title doesn't match."

    def test_click_get_quote(self):
        main_page = page.HomePage(self.driver)
        main_page.click_quote_button()
        assert main_page.is_title_matches(), "contact page is broken"
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()