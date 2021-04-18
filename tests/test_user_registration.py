from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://192.168.1.89"
MY_ACCOUNT = (By.XPATH, "//a[@title='My Account']")
REGISTER_LINK = (By.XPATH, "//ul//a[text()='Register']")
REGISTER_FORM_HEADER = (By.XPATH, "//h1[text()='Register Account']")
REGISTER_FORM = (By.CSS_SELECTOR, "form.form-horizontal")
REGISTER_FORM_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
REGISTER_FORM_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#input-email")
REGISTER_FORM_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#input-password")
REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
REGISTER_FORM_AGREE_POLICY = (By.CSS_SELECTOR, "input[name='agree']")
REGISTER_FORM_CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")
SUCCESS_REGISTER_HEADER = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
CONTINUE_TO_ACCOUNT = (By.XPATH, "//div[class='buttons']//a[text()='Continue']")


def test_register_user(browser):
    browser.get(BASE_URL)

    # Open Register Form
    browser.find_element(*MY_ACCOUNT).click()
    browser.find_element(*REGISTER_LINK).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(REGISTER_FORM))

    # Fill register form and submit
    browser.find_element(*REGISTER_FORM_FIRSTNAME).send_keys("Testfirst")
    browser.find_element(*REGISTER_FORM_LASTNAME).send_keys("Testlast")
    browser.find_element(*REGISTER_FORM_EMAIL).send_keys("testlast@mail.test")
    browser.find_element(*REGISTER_FORM_TELEPHONE).send_keys("89992223344")
    browser.find_element(*REGISTER_FORM_PASSWORD).send_keys("12345678")
    browser.find_element(*REGISTER_FORM_CONFIRM_PASSWORD).send_keys("12345678")
    browser.find_element(*REGISTER_FORM_AGREE_POLICY).click()
    browser.find_element(*REGISTER_FORM_CONTINUE).click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located(SUCCESS_REGISTER_HEADER))
