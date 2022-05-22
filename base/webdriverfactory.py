"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import traceback
from selenium import webdriver
import os


class WebDriverFactory():

    def __init__(self, browser, titleToSearch, baseUrl, dirDriver):
        """
        Inits WebDriverFactory class

        :param browser:
        :returns None
        """
        self.browser = browser
        self.titleToSearch = titleToSearch
        self.baseUrl = baseUrl
        self.dirDriver = dirDriver
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/..../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return:
            'WebDriver Instance'
        """
        #baseUrl = "https://demoqa.com/books"

        if self.browser == "iexplorer":
            # Set internet explorer driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            currentDir = os.getcwd()
            subPath = currentDir[0 : currentDir.find('\QA_Automation_Test_Wefox')]
            path = subPath+self.dirDriver
            driver = webdriver.Chrome(path + "\\chromedriver.exe")
        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for an Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver

    def getTitleToSearch(self):
        return self.titleToSearch