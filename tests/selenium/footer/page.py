from element import BasePageElement

from locators import PageFooterLocators

from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class FooterPage(BasePage):

    def is_copyright_matches(self):
        return "Lauren Nicole Smith 2015" in self.driver.page_source

    def click_github_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_GITHUB_BUTTON)
        element.click()
        return "https://github.com/technolotrix" in self.driver.current_url

    def click_linkedin_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_LINKEDIN_BUTTON)
        element.click()
        return "https://www.linkedin.com/in/nicolelns" in self.driver.current_url

    def click_twitter_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_TWITTER_BUTTON)
        element.click()
        return "" in self.driver.current_url

    def click_gplus_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_GPLUS_BUTTON)
        element.click()
        return "" in self.driver.current_url

    def click_html5up_link(self):
        element = self.driver.find_element(*PageFooterLocators.GET_HTML5UP_LINK)
        element.click()
        return "http://html5up.net" in self.driver.current_url