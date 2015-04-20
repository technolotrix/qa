from selenium.webdriver.common.by import By


class HomePageLocators(object):
    pass   

class AboutPageLocators(object):

    GET_RESUME_BUTTON = (By.CSS_SELECTOR, '#main > header > ul > li > a')
    GET_HTML5UP_BACKLINK = (By.CSS_SELECTOR, '#main > section.wrapper.style4.container > div > section > p:nth-child(19) > a')
    GET_CONTACT_ME_LINK = (By.CSS_SELECTOR, '#main > section.wrapper.style4.container > div > section > p:nth-child(15) > a')


class PageHeaderLocators(object):

    GET_QUOTE_BUTTON = (By.CSS_SELECTOR, '#nav > ul > li:nth-child(2) > a')
    GET_HOME_BUTTON = (By.CSS_SELECTOR, '#logo > a')
    GET_HOVER_NAV = (By.CSS_SELECTOR, '#nav > ul > li.submenu.opener > a')
    GET_ABOUT_LINK = (By.CSS_SELECTOR, '#nav > ul > li.submenu.opener > ul > li:nth-child(1) > a')
    GET_SERVICES_LINK = (By.CSS_SELECTOR, '#nav > ul > li.submenu.opener > ul > li:nth-child(2) > a')
    GET_PROJECTS_LINK = (By.CSS_SELECTOR, '#nav > ul > li.submenu.opener > ul > li:nth-child(3) > a')


class PageFooterLocators(object):

    GET_GITHUB_BUTTON = (By.CSS_SELECTOR, '#footer > ul.icons > li:nth-child(4) > a')
    GET_LINKEDIN_BUTTON = (By.CSS_SELECTOR, '#footer > ul.icons > li:nth-child(2) > a')
    #GET_COPYRIGHT = (By.CSS_SELECTOR, '#footer > ul.copyright > li:nth-child(1)')
    GET_HTML5UP_LINK = (By.CSS_SELECTOR, '#footer > ul.copyright > li:nth-child(2) > a') # link to website template
    GET_TWITTER_BUTTON = (By.CSS_SELECTOR, '#footer > ul.icons > li:nth-child(1) > a')
    GET_GPLUS_BUTTON = (By.CSS_SELECTOR, '#footer > ul.icons > li:nth-child(3) > a')