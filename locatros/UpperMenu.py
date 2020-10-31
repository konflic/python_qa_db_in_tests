from selenium.webdriver.common.by import By


class UpperMenu:
    MY_ACCOUNT = (By.XPATH, "//a[@title='My Account']")
    REGISTER_LINK = (By.XPATH, "//ul//a[text()='Register']")
    LOGIN_LINK = (By.XPATH, "//ul//a[text()='Login']")
