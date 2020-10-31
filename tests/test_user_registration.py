import pytest
import helpers

from locatros.RegistrationForm import RegistrationForm
from locatros.UpperMenu import UpperMenu

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.db
def test_register_user(browser, db_cursor):
    db_cursor = db_cursor.cursor()

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


def test_user_restore_passwords(browser, db_cursor):
    # Create user with DB
    query = 'INSERT INTO oc_customer (customer_group_id, language_id, firstname, lastname, email, telephone, fax, password, salt, custom_field, ip, status, safe, token, code, date_added) VALUES (1, 1, %s, %s, %s, %s, "", %s, "", "", %s, 1, 0, "", "", NOW())'
    email = helpers.random_email()
    db_cursor.cursor().execute(query, (helpers.random_string(), helpers.random_string(), email, helpers.random_phone(), helpers.random_string(), helpers.random_phone(),))
    db_cursor.commit()
    # TODO: Implement restoring password test
