from element import BasePageElement

from locators import PageHeaderLocators

from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HeaderPage(BasePage):

    def click_quote_button(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_QUOTE_BUTTON)
        element.click()
        return "/contact" in self.driver.current_url

    def hover_over_nav(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_HOVER_NAV)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click_home_button(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_HOME_BUTTON)
        element.click()
        return "/" in self.driver.current_url

    def click_projects_link(self):
        self.hover_over_nav()
        element = self.driver.find_element(*PageHeaderLocators.GET_PROJECTS_LINK)
        element.click()
        return "/projects" in self.driver.current_url

    def click_services_link(self):
        self.hover_over_nav()
        element = self.driver.find_element(*PageHeaderLocators.GET_SERVICES_LINK)
        element.click()
        return "/services" in self.driver.current_url

    def click_about_link(self):
        self.hover_over_nav()
        element = self.driver.find_element(*PageHeaderLocators.GET_ABOUT_LINK)
        element.click()
        return "/about" in self.driver.current_url