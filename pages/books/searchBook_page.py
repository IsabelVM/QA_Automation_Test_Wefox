import utilities.custom_logger as cl
from utilities.util import Util
import logging
from base.basepage import BasePage
import time
from selenium.webdriver.common.keys import Keys
from base.webdriverfactory import WebDriverFactory

class SearchBookPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def     __init__(self, driver,titleToSearch):
        #we're calling the init method of superclass and we are providing the driver
        super().__init__(driver)
        self.driver = driver
        self.titleToSearch = titleToSearch


    # Locators
    _searchBox = "searchBox"
    _book = "see-book-Programming JavaScript Applications"
    _labelISBN = "//div[@id='ISBN-wrapper']//label[contains(text(),'9781491950296')]"
    #_table = "//div[@class='rt-tbody'"
    _books = "//div[contains(@class,'rt-td')]//div[contains(@class,'action-buttons')]"

    def saveinitialList(self):
        initialList  = self.getElementList(self._books, "xpath")
        initialTextsList = self.createListTexts(initialList)
        return initialTextsList

    def enterBookName(self,Name):
        messageElement = self.waitForElement(locator=self._searchBox, locatorType="id")
        result = self.isElementDisplayed(locator=self._searchBox, locatorType="id", element=messageElement)

        if result:
            time.sleep(5)
            self.cleanField(self._searchBox, "id")
            self.sendKeys(Name, self._searchBox, "id")
            self.sendKeys(Keys.RETURN, self._searchBox, "id")

    def clickFoundBook(self, NameBook):
        messageElement = self.waitForElement(locator=self._book, locatorType="id")
        result = self.isElementDisplayed(locator=self._book, locatorType="id", element=messageElement)
        if result:
            self.log.info("Book Founded >>> " + self._book)
            self.elementClick(self._book, locatorType="id")

    def clickSearchBox(self):
        if self.verifyPageTitle("ToolsQA"):
            self.elementClick(self._searchBox, locatorType="id")

    def searchBook(self, book=""):
        self.clickSearchBox()
        self.enterBook(book)

    def verifyDetailSuccessful(self):
        result = self.isElementPresent(self._labelISBN, "xpath")
        return result

    def backButtonClick(self):
        self.driver.back()

    def verifyListBookDisplayed(self, initialList=""):
        self.refresh()
        lastList = self.getElementList(self._books, "xpath")
        lastTextsList = self.createListTexts(lastList)
        result = self.util.VerifyListMatch(initialList,lastTextsList)
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("ToolsQA")
