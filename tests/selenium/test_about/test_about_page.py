import unittest
from selenium import webdriver
import page

class AboutPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get("http://nicolesmith.nyc")
        self.driver.get("http://127.0.0.1:4747/about")
        self.about_page = page.AboutPage(self.driver)

    ######## HEADER STUFF ########

    def test_title_on_about_page(self):
        assert self.about_page.is_title_matches(), "about page title doesn't match"

    def test_click_get_quote(self):
        assert self.about_page.click_quote_button(), "link to contact page is broken"

    def test_click_home_button(self):
        assert self.about_page.click_home_button(), "home button does not go to homepage"

    @unittest.skip("Needs fixing.")
    def test_click_about_link(self):
        assert self.about_page.click_projects_link(), "about link does not go to about page"

    @unittest.skip("Needs fixing.")
    def test_click_projects_link(self):
        assert self.about_page.click_projects_link(), "projects link does not go to projects page"

    @unittest.skip("Needs fixing.")
    def test_click_services_link(self):
        assert self.about_page.click_projects_link(), "services link does not go to services page"

    ######## PAGE SPECIFIC STUFF ########

    def test_click_resume(self):
        return self.about_page.click_resume(), "link to resume is broken"

    def test_click_resumator(self):
        return self.about_page.click_resumator(), "link to resumator is broken"

    def test_click_contact_me(self):
        return self.about_page.click_contact_me(), "link to contact me page is broken in FAQ"

    def test_click_html5up_backlink(self):
        return self.about_page.click_html5up_backlink(), "backlink to html5up in FAQ is broken"

    ######## FOOTER STUFF ########

    def test_click_github(self):
        assert self.about_page.click_github_button(), "link to github is broken"

    def test_click_linkedin(self):
        assert self.about_page.click_linkedin_button(), "link to linkedin is broken"

    def test_click_gplus(self):
        assert self.about_page.click_gplus_button(), "link to google plus is broken"

    def test_click_twitter(self):
        assert self.about_page.click_twitter_button(), "link to twitter is broken"

    def test_click_html5up(self):
        assert self.about_page.click_html5up_link(), "link to html5up template owner is broken"

    def test_copyright_on_about_page(self):
        assert self.about_page.is_copyright_matches(), "about page has wrong copyright"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()