import os
import pytest
import mysql.connector

from locators import *
from helpers import random_email, random_phone, random_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

BASE_URL = "http://192.168.1.89"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action='store_true')
    parser.addoption("--close", action='store_true')


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    close = request.config.getoption("--close")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("~/Downloads/drivers/chromedriver"))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.expanduser("~/Downloads/drivers/geckodriver"))
    else:
        raise ValueError("{} is not supported argument for browser!".format(browser))

    if close:
        request.addfinalizer(driver.quit)

    if maximize:
        driver.maximize_window()

    driver.get(BASE_URL)
    return driver


@pytest.fixture(scope="session")
def db_con(request):
    connection = mysql.connector.connect(
        user='bn_opencart',
        password='',
        host='127.0.0.1',
        database='bitnami_opencart',
        port='3306'
    )
    request.addfinalizer(connection.close)
    return connection


@pytest.fixture
def new_customer(browser, db_con):
    # Open Register Form
    browser.find_element(*MY_ACCOUNT).click()
    browser.find_element(*REGISTER_LINK).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(REGISTER_FORM))
    email = random_email()

    # Fill register form and submit
    browser.find_element(*REGISTER_FORM_FIRSTNAME).send_keys("test_" + random_string(5))
    browser.find_element(*REGISTER_FORM_LASTNAME).send_keys("test_" + random_string(5))
    browser.find_element(*REGISTER_FORM_EMAIL).send_keys(email)
    browser.find_element(*REGISTER_FORM_TELEPHONE).send_keys(random_phone())
    browser.find_element(*REGISTER_FORM_PASSWORD).send_keys("12345678")
    browser.find_element(*REGISTER_FORM_CONFIRM_PASSWORD).send_keys("12345678")
    browser.find_element(*REGISTER_FORM_AGREE_POLICY).click()
    browser.find_element(*REGISTER_FORM_CONTINUE).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(SUCCESS_REGISTER_HEADER))
    return email
