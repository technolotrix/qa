import unittest
from selenium import webdriver
import page
from footer.test_footer import Footer
from header.test_header import Header

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://nicolesmith.nyc")
        #self.driver.get("http://127.0.0.1:4747")
        self.homepage = page.HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

class HeaderTests(unittest.TestCase, Header):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get("http://nicolesmith.nyc")

        self.test_pages = ["/about", "/", "contact", "/resumator" "/projects", "/services"]

    ######## HEADER STUFF ########

    def test_header(self):

        for url in self.test_pages:
            yield Header, url, self.driver

    def tearDown(self):
        self.driver.close()

class FooterTests(unittest.TestCase, Footer):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get("http://nicolesmith.nyc")

        self.test_pages = ["/about", "/", "contact", "/resumator" "/projects", "/services"]

    ######## FOOTER STUFF ########

    def test_footer(self):

        for url in self.test_pages:
            yield Footer, url, self.driver

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()