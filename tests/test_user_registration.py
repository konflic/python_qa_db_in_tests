import pytest
import helpers

from locatros.RegistrationForm import RegistrationForm
from locatros.UpperMenu import UpperMenu
from locatros.LoginForm import LoginForm
from locatros.MyAccountPage import MyAccountPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.db
def test_register_user(browser, db_connection):
    db_cursor = db_connection.cursor()

    # Open Register Form
    browser.find_element(*UpperMenu.MY_ACCOUNT).click()
    browser.find_element(*UpperMenu.REGISTER_LINK).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(RegistrationForm.IT))

    # Fill register form and submit
    firstname = helpers.random_string()
    lastname = helpers.random_string()
    email = helpers.random_email()
    phone = helpers.random_phone()
    password = helpers.random_string()

    browser.find_element(*RegistrationForm.FIRSTNAME).send_keys(firstname)
    browser.find_element(*RegistrationForm.LASTNAME).send_keys(lastname)
    browser.find_element(*RegistrationForm.EMAIL).send_keys(email)
    browser.find_element(*RegistrationForm.TELEPHONE).send_keys(phone)
    browser.find_element(*RegistrationForm.PASSWORD).send_keys(password)
    browser.find_element(*RegistrationForm.CONFIRM_PASSWORD).send_keys(password)
    browser.find_element(*RegistrationForm.AGREE_POLICY).click()
    browser.find_element(*RegistrationForm.CONTINUE).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(RegistrationForm.SUCCESS_REGISTER_HEADER))

    # Add verification that user was created in database
    db_cursor.execute("SELECT customer_id FROM oc_customer WHERE email = %s", (email,))
    data = db_cursor.fetchall()
    assert data, "Could not find any data about user with email: {} in database".format(email)

    customer_id = data[0][0]
    db_cursor.execute("SELECT * FROM oc_customer_ip WHERE customer_id = %s", (customer_id,))
    assert  db_cursor.fetchall(), "Did not find ip entry for user with cunstomer_id: {}".format(customer_id)


@pytest.mark.db
def test_user_restore_passwords(browser, db_connection):
    # Create user with DB
    user_email = helpers.create_random_user(db_connection)
    # Open Login Form
    browser.find_element(*UpperMenu.MY_ACCOUNT).click()
    browser.find_element(*UpperMenu.LOGIN_LINK).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(LoginForm.LOGIN_BTN))
    # Fill in and submit Login
    browser.find_element(*LoginForm.EMAIL).send_keys(user_email)
    browser.find_element(*LoginForm.PASSWORD).send_keys("test") # predefined password for test users
    browser.find_element(*LoginForm.LOGIN_BTN).click()
    # Verify some element of logged in user
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(MyAccountPage.EDIT_YOU_ACCOUNT_INFO))
