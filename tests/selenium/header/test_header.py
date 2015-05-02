import unittest
from selenium import webdriver
import page

class Header(object):

    def setUp(self, page_url, driver):
        self.driver = driver
        self.driver.get("http://nicolesmith.nyc")
        #self.page_url = "http://127.0.0.1:4747/{0}".format(page_url)
        self.driver.get(self.page_url)
        self.header = page.HeaderPage(self.driver)

    ######## HEADER STUFF ########

    def test_click_get_quote(self):
        assert self.header.click_quote_button(), "link to contact page is broken"

    def test_click_home_button(self):
        assert self.header.click_home_button(), "home button does not go to homepage"

    @unittest.skip("Needs fixing.")
    def test_click_about_link(self):
        assert self.header.click_projects_link(), "about link does not go to about page"

    @unittest.skip("Needs fixing.")
    def test_click_projects_link(self):
        assert self.header.click_projects_link(), "projects link does not go to projects page"

    @unittest.skip("Needs fixing.")
    def test_click_services_link(self):
        assert self.header.click_projects_link(), "services link does not go to services page"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()