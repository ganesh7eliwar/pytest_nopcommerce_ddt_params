from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Add_customer:
    news_letter_ = ("/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div["
                    "1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]")
    customer_roles_ = ("/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/"
                       "div[2]/div/div[1]/div/div")
    vendor_manager_ = ("/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div["
                       "1]/div[2]/div[11]/div[2]/select[1]")

    customers_button_by_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    add_new_button_by_xpath = "//a[@class='btn btn-primary']"
    email_by_xpath = "//input[@id='Email']"
    password_by_xpath = "//input[@id='Password']"
    first_name_by_xpath = "//input[@id='FirstName']"
    last_name_by_xpath = "//input[@id='LastName']"
    gender_male_by_xpath = "//input[@id='Gender_Male']"
    gender_female_by_xpath = "//input[@id='Gender_Female']"
    click_date_by_xpath = "//span[@class='k-icon k-i-calendar']"
    date_of_birth_date_by_xpath = "//input[@id='DateOfBirth']"
    company_name_by_xpath = "//input[@id='Company']"
    tax_exempt_by_xpath = "//input[@id='IsTaxExempt']"
    news_letter_by_xpath = news_letter_
    customer_roles_by_xpath = customer_roles_
    manager_of_vendor_by_xpath = vendor_manager_
    active_status_by_xpath = "//input[@id='Active']"
    admin_comment_by_xpath = "//textarea[@id='AdminComment']"
    save_button_by_xpath = "//button[@name='save']"
    add_a_new_customer_by_xpath = "//h1[@class='float-left']"
    customers_button_2_by_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    click_new_letter_by_xpath = "//li[normalize-space()='Test store 2']"
    click_customer_roles_by_xpath = "//li[contains(text(),'Vendors')]"
    click_manager_of_vendor_by_xpath = "//*[@id='VendorId']"
    add_customer_confirmation_by_xpath = "//div[@class='alert alert-success alert-dismissable']"
    dropdown_manager_of_vendor_by_xpath = "//select[@id='VendorId']"
    new_store_by_xpath = "//input[@id='customer_attribute_1']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def customer_btn(self):
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, self.customers_button_by_xpath)))
            self.driver.find_element(By.XPATH, self.customers_button_by_xpath).click()
        except NoSuchElementException:
            pass

    def customer_btn_1(self):
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, self.customers_button_2_by_xpath)))
            self.driver.find_element(By.XPATH, self.customers_button_2_by_xpath).click()
        except NoSuchElementException:
            pass

    def add_new_customer(self):
        self.driver.find_element(By.XPATH, self.add_new_button_by_xpath).click()

    def customer_email(self, email):
        self.driver.find_element(By.XPATH, self.email_by_xpath).send_keys(email)

    def customer_password(self, password):
        self.driver.find_element(By.XPATH, self.password_by_xpath).send_keys(password)

    def first_name(self, name):
        self.driver.find_element(By.XPATH, self.first_name_by_xpath).send_keys(name)

    def last_name(self, lst_name):
        self.driver.find_element(By.XPATH, self.last_name_by_xpath).send_keys(lst_name)

    def gender(self, gender):
        if gender == "male":
            self.driver.find_element(By.XPATH, self.gender_male_by_xpath).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH, self.gender_female_by_xpath).click()

    def date_of_birth(self, dob):
        self.driver.find_element(By.XPATH, self.date_of_birth_date_by_xpath).send_keys(dob)

    def company_name(self, com_name):
        self.driver.find_element(By.XPATH, self.company_name_by_xpath).send_keys(com_name)

    # def new_store(self, status):
    #     self.driver.find_element(By.XPATH, self.new_store_by_xpath).send_keys(status)

    def tax_check_box(self, status):
        if status == "check":
            self.driver.find_element(By.XPATH, self.tax_exempt_by_xpath).click()
        elif status == "uncheck":
            pass

    def news_letter(self):
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, self.news_letter_by_xpath)))
            self.driver.find_element(By.XPATH, self.news_letter_by_xpath).click()
        except NoSuchElementException:
            pass

    def click_news_letter(self):
        self.driver.find_element(By.XPATH, self.click_new_letter_by_xpath).click()

    def customer_roles(self):
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, self.customer_roles_by_xpath)))
            self.driver.find_element(By.XPATH, self.customer_roles_by_xpath).click()
        except NoSuchElementException:
            pass

    def click_customer_roles(self):
        self.driver.find_element(By.XPATH, self.click_customer_roles_by_xpath).click()

    def dropdown_manager_of_vendor(self, value):
        Select(self.driver.find_element(By.XPATH, self.dropdown_manager_of_vendor_by_xpath)).select_by_visible_text(
            value)

    def active_button(self, status):
        if status == "Check":
            self.driver.find_element(By.XPATH, self.active_status_by_xpath).click()
        elif status == "Uncheck":
            pass

    def admin_comment(self, comment):
        self.driver.find_element(By.XPATH, self.admin_comment_by_xpath).send_keys(comment)

    def save_btn(self):
        self.driver.find_element(By.XPATH, self.save_button_by_xpath).click()

    def add_customer_verification(self):
        try:
            self.driver.find_element(By.XPATH, self.add_a_new_customer_by_xpath)
            return "You Are on Add New Customer Page"
        except NoSuchElementException:
            return "Unable to Load Page"

    def screenshot_fail(self):
        self.driver.save_screenshot("..\\screenshots\\add_customer_read_data\\test_add_customer_003_fail.png")

    def screenshot_pass_con(self):
        self.driver.save_screenshot("..\\screenshots\\add_customer_confirmation\\test_add_customer_pass.png")

    def screenshot_fail_con(self):
        self.driver.save_screenshot("..\\screenshots\\add_customer_confirmation\\test_add_customer_fail.png")

    def add_customer_confirmation(self):
        try:
            self.driver.find_element(By.XPATH, self.add_customer_confirmation_by_xpath)
            return "Customer was Added Successfully"
        except NoSuchElementException:
            return "Operation Failed"
