import unittest
from selenium import webdriver
import page

class Footer(object):

    def setUp(self, page_url, driver):
        self.driver = driver
        #self.driver.get("http://nicolesmith.nyc")
        self.page_url = "http://127.0.0.1:4747/{0}".format(page_url)
        self.driver.get(self.page_url)
        self.footer = page.FooterPage(self.driver)

    ######## FOOTER STUFF ########

    def test_click_github(self):
        assert self.footer.click_github_button(), "link to github is broken"

    def test_click_linkedin(self):
        assert self.footer.click_linkedin_button(), "link to linkedin is broken"

    def test_click_gplus(self):
        assert self.footer.click_gplus_button(), "link to google plus is broken"

    def test_click_twitter(self):
        assert self.footer.click_twitter_button(), "link to twitter is broken"

    def test_click_html5up(self):
        assert self.footer.click_html5up_link(), "link to html5up template owner is broken"

    def test_copyright_on_about_page(self):
        assert self.footer.is_copyright_matches(), "about page has wrong copyright"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()