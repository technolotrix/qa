from selenium.element import BasePageElement
from selenium.locators import PageHeaderLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def is_title_matches(self):
        return "Hello, world!" in self.driver.title

    def click_quote_button(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_QUOTE_BUTTON)
        element.click()
        return "/contact" in self.driver.current_url

    def hover_over_nav(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_HOVER_NAV)
        return ""

    def click_home_button(self):
        pass