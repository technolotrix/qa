from element import BasePageElement
from locators import MainPageLocators

class SearchTitleElement(BasePageElement):

    locator = 'title'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    search_title_element = SearchTitleElement()

    def is_title_matches(self):
        return "Hello, world!" in self.driver.title

    def click_quote_button(self):
        element = self.driver.find_element(*MainPageLocators.GET_QUOTE_BUTTON)
        element.click()
        return "Contact Page" in self.driver.title


class AboutPage(BasePage):

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source