from selenium.webdriver.common.by import By


class RegistrationForm:
    IT = (By.CSS_SELECTOR, "form.form-horizontal")
    HEADER = (By.XPATH, "//h1[text()='Register Account']")
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    AGREE_POLICY = (By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")
    SUCCESS_REGISTER_HEADER = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    CONTINUE_TO_ACCOUNT = (By.XPATH, "//div[class='buttons']//a[text()='Continue']")
