import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="class")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        browser = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def wait():
    time.sleep(1)
