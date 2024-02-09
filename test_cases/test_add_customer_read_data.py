import random
import string
import allure
from allure_commons.types import AttachmentType

from page_objects.add_customer_page import Add_customer
from page_objects.login_page import Login_page
from utilities import excel_methods
from utilities.logger import Log_generator


class Test_add_customer:
    excel_file_path = ("D:\\ct_17_batch_revision\\Pytest_Framework_By_Tushar_Sir\\Pytest_params_DDt\\Test_Data"
                       "\\test_data.xlsx")
    email = excel_methods.read_data(excel_file_path,        "read_data", 2, 2)
    password = excel_methods.read_data(excel_file_path,     "read_data", 3, 2)
    first_name = excel_methods.read_data(excel_file_path,   "read_data", 4, 2)
    last_name = excel_methods.read_data(excel_file_path,    "read_data", 5, 2)
    company = excel_methods.read_data(excel_file_path,      "read_data", 6, 2)
    comment = excel_methods.read_data(excel_file_path,      "read_data", 7, 2)
    dob = excel_methods.read_data(excel_file_path,          "read_data", 8, 2)
    male = excel_methods.read_data(excel_file_path,         "read_data", 9, 2)
    female = excel_methods.read_data(excel_file_path,       "read_data", 10, 2)
    value = excel_methods.read_data(excel_file_path,        "read_data", 11, 2)
    check = excel_methods.read_data(excel_file_path,        "read_data", 12, 2)
    uncheck = excel_methods.read_data(excel_file_path,      "read_data", 13, 2)
    Check = excel_methods.read_data(excel_file_path,        "read_data", 14, 2)
    Uncheck = excel_methods.read_data(excel_file_path,      "read_data", 15, 2)
    password_1 = excel_methods.read_data(excel_file_path,   "read_data", 16, 2)
    new_store = excel_methods.read_data(excel_file_path,    "read_data", 19, 2)
    log = Log_generator.log_gen()

    @allure.title('Test_Add_Customer_Read_Data')
    @allure.feature('Adding A New Customer By Reading Data from excel')
    @allure.story('validating add customer page')
    @allure.description('testing_add_customer_page')
    @allure.issue('TAC-001')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_customer_read_data(self, setup):
        self.log.info("Testcase test_add_customer_003 Started")
        self.log.info("Opening the Browser")
        self.driver = setup
        self.log.info("Assigning Variable to Login_page")
        self.lp = Login_page(self.driver)
        self.log.info("Assigning Variable to Add_customer_page")
        self.ac = Add_customer(self.driver)
        self.log.info("Entering Email -->" + self.email)
        self.lp.email(self.email)
        self.log.info("Entering Password -->" + self.password)
        self.lp.password(self.password)
        self.log.info("Clicking Login Button")
        self.lp.login_btn()
        if self.lp.login_verification() == "Login Passed":
            self.log.info("Login Successful")
            self.log.info("Clicking 1st Customers Button")
            self.ac.customer_btn()
            self.log.info("Clicking 2nd Customers Button")
            self.ac.customer_btn_1()
            self.log.info("Clicking on Add Customer Button")
            self.ac.add_new_customer()
            if self.ac.add_customer_verification() == "You Are on Add New Customer Page":
                self.log.info("Landed on Add New Customer Page")
                email_1 = generate_email()
                self.log.info("Entering Customer Email -->" + email_1)
                self.ac.customer_email(email_1)
                password_1 = generate_password()
                self.log.info("Entering Password -->" + password_1)
                self.ac.customer_password(self.password_1)
                self.log.info("Entering First_name -->" + self.first_name)
                self.ac.first_name(self.first_name)
                self.log.info("Entering Last_name -->" + self.last_name)
                self.ac.last_name(self.last_name)
                self.log.info("Selecting Gender -->" + self.male)
                self.ac.gender(self.male)
                self.log.info("Entering Date of Birth -->" + str(self.dob))
                self.ac.date_of_birth(str(self.dob))
                self.log.info("Entering Company Name -->" + self.company)
                self.ac.company_name(self.company)
                # self.log.info("Entering Data into New_store --> " + self.new_store)
                # self.ac.new_store(self.new_store)
                self.log.info("Clicking on Tax Button -->" + self.uncheck)
                self.ac.tax_check_box(self.uncheck)
                self.log.info("Clicking on News Letter Button")
                self.ac.news_letter()
                self.log.info("Selecting option in News Letter")
                self.ac.click_news_letter()
                self.log.info("Clicking on Customer Roles")
                self.ac.customer_roles()
                self.log.info("Selecting Option in Customer Roles")
                self.ac.click_customer_roles()
                self.log.info("Selecting Manager of Vendor -->" + self.value)
                self.ac.dropdown_manager_of_vendor(self.value)
                self.log.info("Clicking on Active Button Check Box -->" + self.Uncheck)
                self.ac.active_button(self.Uncheck)
                self.log.info("Writing the Comment -->" + self.comment)
                self.ac.admin_comment(self.comment)
                self.log.info("Clicking on Save Button")
                self.ac.save_btn()
                if self.ac.add_customer_confirmation() == "Customer was Added Successfully":
                    self.log.info("Customer Added Successfully")
                    self.log.info("Screenshot Captured Testcase 'test_add_customer_read_data' Passed")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_add_customer_read_data',
                                  attachment_type=AttachmentType.PNG)
                    self.ac.screenshot_pass_con()
                    self.log.info("Clicking on Logout Button")
                    self.lp.logout_btn()
                    self.log.info("'test_add_customer_read_data' Completed")
                    assert True
                else:
                    self.log.info("Screenshot Captured Testcase 'test_add_customer_read_data' Failed")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_add_customer_read_data',
                                  attachment_type=AttachmentType.PNG)
                    self.ac.screenshot_fail_con()
                    assert False
                assert True
            else:
                self.log.info("Screenshot Captured Testcase 'test_add_customer_read_data' Failed")
                allure.attach(self.driver.get_screenshot_as_png(),
                              name='test_add_customer_read_data_on_customer_verification_level',
                              attachment_type=AttachmentType.PNG)
                self.ac.screenshot_fail()
                assert False
            assert True
        else:
            self.log.info("Screenshot Captured login Testcase test_add_customer_read_data Failed")
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='test_add_customer_read_data_on_login_level',
                          attachment_type=AttachmentType.PNG)
            self.lp.screenshot_fail()
            assert False


def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=7))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"


def generate_password():
    first_4_char = ''.join(random.choices(string.ascii_lowercase, k=4))
    special_char = random.choice(['!', '@', '#', '$', '%', '^', '&', '*'])
    last_4_digits = ''.join(random.choices(string.digits, k=4))
    return f"{first_4_char}{special_char}{last_4_digits}"


def generate_dob():
    month = random.choice(['01', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
    day = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                         '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'])
    year = random.choice(['1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985',
                          '1986', '1987', '1988' '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996',
                          '1997', '1998', '1999', '2000', '2001', '2002'])
    return f"{month}-{day}-{year}"


def generate_gender():
    gender = random.choice(['male', 'female'])
    return f"{gender}"
