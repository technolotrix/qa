import unittest
from selenium import webdriver
import page

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get("http://nicolesmith.nyc")
        self.driver.get("http://127.0.0.1:4747")
        self.homepage = page.HomePage(self.driver)

    ######## HEADER STUFF ########

    def test_title_on_homepage(self):
        assert self.homepage.is_title_matches(), "Home page title doesn't match"

    def test_click_get_quote(self):
        assert self.homepage.click_quote_button(), "link to contact page is broken"

    def test_click_home_button(self):
        assert self.homepage.click_home_button(), "home button does not go to homepage"

    @unittest.skip("Needs fixing.")
    def test_click_about_link(self):
        assert self.homepage.click_projects_link(), "About link does not go to about page"

    @unittest.skip("Needs fixing.")
    def test_click_projects_link(self):
        assert self.homepage.click_projects_link(), "projects link does not go to projects page"

    @unittest.skip("Needs fixing.")
    def test_click_services_link(self):
        assert self.homepage.click_projects_link(), "services link does not go to services page"

    ######## PAGE SPECIFIC STUFF ########

    

    ######## FOOTER STUFF ########

    def test_click_github(self):
        assert self.homepage.click_github_button(), "link to github is broken"

    def test_click_linkedin(self):
        assert self.homepage.click_linkedin_button(), "link to linkedin is broken"

    def test_click_gplus(self):
        assert self.homepage.click_gplus_button(), "link to google plus is broken"

    def test_click_twitter(self):
        assert self.homepage.click_twitter_button(), "link to twitter is broken"

    def test_click_html5up(self):
        assert self.homepage.click_html5up_link(), "link to html5up template owner is broken"

    def test_copyright_on_homepage(self):
        assert self.homepage.is_copyright_matches(), "Home page has wrong copyright"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()