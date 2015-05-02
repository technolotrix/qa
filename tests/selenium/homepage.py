import unittest
from selenium import webdriver
import page

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://nicolesmith.nyc")
        
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



"""
class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://nicolesmith.nyc")

    def test_title(self):
        self.assertIn("Hello", self.driver.title)

    def test_links(self):

        for url in self.driver.find_elements_by_tag_name('a'):
            self.driver.click(url)

    def tearDown(self):
        self.driver.close()
"""