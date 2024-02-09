from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Login_page:

    email_by_xpath = "//input[@id='Email']"
    password_by_xpath = "//input[@id='Password']"
    login_button_by_xpath = "//button[@type='submit']"
    logout_button_by_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def email(self, email):
        self.driver.find_element(By.XPATH, self.email_by_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_by_xpath).send_keys(email)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.password_by_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_by_xpath).send_keys(password)

    def login_btn(self):
        self.driver.find_element(By.XPATH, self.login_button_by_xpath).click()

    def login_verification(self):
        try:
            self.driver.find_element(By.XPATH, self.logout_button_by_xpath)
            return "Login Passed"
        except NoSuchElementException:
            return "Login Failed"

    def logout_btn(self):
        self.driver.find_element(By.XPATH, self.logout_button_by_xpath).click()

    def screenshot_fail(self):
        self.driver.save_screenshot(".\\screenshots\\login_page\\Login Testcase test_user_login_params_failed.png")

    def screenshot_pass(self):
        self.driver.save_screenshot(".\\screenshots\\login_page\\Login Testcase test_user_login_params_passed.png")
