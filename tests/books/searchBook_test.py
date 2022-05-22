from pages.books.searchBook_page import SearchBookPage
from utilities.testStatus import TestStatus
from base.webdriverfactory import WebDriverFactory
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SearchBookTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        dicParams = dict(oneTimeSetUp)

        self.sbp = SearchBookPage(dicParams['driver'],dicParams['titleToSearch'])
        self.ts = TestStatus(self.driver)


    #Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(order=1)
    def test_validSearchBook(self):
        initialList = self.sbp.saveinitialList()

        self.sbp.enterBookName(self.sbp.titleToSearch)
        self.sbp.clickFoundBook(self.sbp.titleToSearch)

        result1 = self.sbp.verifyDetailSuccessful()
        self.ts.mark(result1, "Detail verified")
        self.sbp.backButtonClick()
        result2 = self.sbp.verifyListBookDisplayed(initialList)
        self.ts.markFinal("test_validSearchBook", result2, "The list of books is displayed successfully")
