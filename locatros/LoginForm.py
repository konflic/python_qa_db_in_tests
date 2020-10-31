from selenium.webdriver.common.by import By


class LoginForm:
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[value='Login']")
