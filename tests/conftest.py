import pytest
from base.webdriverfactory import WebDriverFactory
from base.basepage import BasePage
from pages.books.searchBook_page import SearchBookPage

@pytest.fixture()
def setUp():
    print("Running method level setUp")

    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, titleToSearch, baseURL):
#def oneTimeSetUp(request, browser, titleToSearch, baseURL, dirDriver):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser, titleToSearch, baseURL)
    driver = wdf.getWebDriverInstance()
    titleToSearch = wdf.getTitleToSearch()

    # add 'driver' attribute to the class under test -->
    if request.cls is not None:
        request.cls.driver = driver

    yield {
        'driver': driver,
        'titleToSearch': titleToSearch
         }

    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--titleToSearch")
    parser.addoption("--baseUrl")
    parser.addoption("--dirDriver")

#The scope we can put by module, or in this case we're going to test by session
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def titleToSearch(request):
    return request.config.getoption("--titleToSearch")

@pytest.fixture(scope="session")
def baseURL(request):
    return request.config.getoption("--baseUrl")

@pytest.fixture(scope="session")
def dirDriver(request):
    return request.config.getoption("--dirDriver")