import allure
from allure_commons.types import AttachmentType

from page_objects.login_page import Login_page
from utilities import excel_methods
from utilities.logger import Log_generator


class Test_login_ddt:
    excel_file_path = ("D:\\ct_17_batch_revision\\Pytest_Framework_By_Tushar_Sir\\Pytest_params_DDt\\Test_Data"
                       "\\test_data.xlsx")
    logs = Log_generator.log_gen()

    @allure.title('Test_User_Login_DDT')
    @allure.feature('Login Through DDT')
    @allure.story('validating login with ddt')
    @allure.description('testing_login_functionality')
    @allure.issue('ABC-006')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_login_ddt(self, setup):
        self.logs.info("Testcase 'test_user_login_ddt' has Started")
        self.driver = setup
        self.logs.info('Opening the Browser')
        self.lp = Login_page(self.driver)
        self.rows = excel_methods.no_of_rows(self.excel_file_path, "login_data")
        print("\nnumber of rows in excel sheet are -->" + str(self.rows))
        testcase_status_list = []
        for r in range(2, self.rows + 1):
            self.email = excel_methods.read_data(self.excel_file_path, "login_data", r, 2)
            self.password = excel_methods.read_data(self.excel_file_path, "login_data", r, 3)
            self.expected_result = excel_methods.read_data(self.excel_file_path, "login_data", r, 4)
            # print("row_number       --> " + str(r))
            # print("email            --> " + self.email)
            # print("password         --> " + self.password)
            # print("expected_result  --> " + self.expected_result)
            self.logs.info("Entering Email -->" + self.email)
            self.lp.email(self.email)
            self.logs.info("Entering Password -->" + self.password)
            self.lp.password(self.password)
            self.logs.info("Clicking on Login Button")
            self.lp.login_btn()
            if self.lp.login_verification() == "Login Passed":
                excel_methods.write_data(self.excel_file_path, "login_data", r, 5, "pass")
                self.logs.info("Login Successful")
                self.logs.info("Entered into 'outer if block'")
                if self.expected_result == "pass":
                    self.logs.info("Entered into 'inner if block' of 'outer if block' -->" + self.expected_result)
                    self.logs.info("Appending the list")
                    testcase_status_list.append("pass")
                    self.logs.info("Capturing Screenshot for Allure Report")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_ddt_passed',
                                  attachment_type=AttachmentType.PNG)
                    self.logs.info("Clicking on logout Button")
                    self.lp.logout_btn()
                elif self.expected_result == "fail":
                    self.logs.info("Entered into 'inner elif bloc of 'outer if block' -->" + self.expected_result)
                    self.logs.info("Appending the list")
                    testcase_status_list.append("fail")
            elif self.lp.login_verification() == "Login Failed":
                excel_methods.write_data(self.excel_file_path, "login_data", r, 5, "fail")
                self.logs.info("Login Unsuccessful")
                self.logs.info("Entered into 'outer elif' block")
                if self.expected_result == "fail":
                    self.logs.info("Entered into 'inner if block' of 'outer elif block' -->" + self.expected_result)
                    self.logs.info("Appending the list")
                    testcase_status_list.append("pass")
                    self.logs.info("Capturing Screenshot for Allure Report")
                    allure.attach(self.driver.get_screenshot_as_png(), name='test_user_login_ddt_failed',
                                  attachment_type=AttachmentType.PNG)
                elif self.expected_result == "pass":
                    self.logs.info("Entered into 'inner elif block' of 'outer elif block' -->" + self.expected_result)
                    self.logs.info("Appending the list")
                    testcase_status_list.append("fail")
            self.logs.info("Printing the list")
        print(testcase_status_list)
        if "fail" in testcase_status_list:
            self.logs.info("Testcase 'test_user_login_ddt' has Failed")
            assert False
        else:
            self.logs.info("Testcase 'test_user_login_ddt' has Passed")
            assert True
        self.logs.info("Testcase 'test_user_login_ddt' has Completed")
