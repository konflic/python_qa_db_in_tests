import pytest
import mysql.connector

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action='store_true')
    parser.addoption("--close", action='store_true')
    parser.addoption("--base_url", default='http://localhost')


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    close = request.config.getoption("--close")
    base_url = request.config.getoption("--base_url")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    else:
        raise ValueError("{} is not supported argument for browser!".format(browser))

    if close:
        request.addfinalizer(driver.close)

    if maximize:
        driver.maximize_window()

    driver.get(base_url)
    return driver


@pytest.fixture
def db_connection(request):
    connection = mysql.connector.connect(
        user='bn_opencart',
        password='',
        host='127.0.0.1',
        database='bitnami_opencart',
        port='3306'
    )
    request.addfinalizer(connection.close)
    return connection
