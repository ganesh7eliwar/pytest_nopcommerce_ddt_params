import allure
from allure_commons.types import AttachmentType

from page_objects.login_page import Login_page
from utilities.logger import Log_generator


class Test_user_login:
    logs = Log_generator.log_gen()

    @allure.title('Test_User_Login_Params')
    @allure.feature('Login Through Params')
    @allure.story('validating login with multiple parameters')
    @allure.description('testing_login_functionality')
    @allure.issue('ABC-005')
    @allure.link(url="--> https://admin-demo.nopcommerce.com", name="--> nop_commerce")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_params(self, setup, data_for_login):
        self.logs.info("Testcase 'test_login_with_params' Started")
        self.logs.info("Opening the Browser")
        self.driver = setup
        self.logs.info("Assigning Variable to Login Page")
        self.lp = Login_page(self.driver)
        self.logs.info("Entering Email from Params -->" + data_for_login[0])
        self.lp.email(data_for_login[0])
        self.logs.info("Entering Password from Params -->" + data_for_login[1])
        self.lp.password(data_for_login[1])
        self.logs.info("Clicking on Login Button")
        self.lp.login_btn()
        testcase_status_list = []
        if self.lp.login_verification() == "Login Passed":
            self.logs.info("Login Successful")
            self.logs.info("Entered into 'outer if block'")
            if data_for_login[2] == "pass":
                self.logs.info("Entered into 'inner if block' of 'outer if block' -->" + data_for_login[2])
                self.logs.info("Appending the list")
                testcase_status_list.append("pass")
                self.logs.info("Capturing Screenshot for Allure Report")
                allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_params_passed',
                              attachment_type=AttachmentType.PNG)
                self.logs.info("Clicking on logout Button")
                self.lp.logout_btn()
            # elif data_for_login[2] == "fail":
            #     self.logs.info("Entered into 'inner elif bloc of 'outer if block' -->" + data_for_login[2])
            #     self.logs.info("Appending the list")
            #     testcase_status_list.append("fail")
        elif self.lp.login_verification() == "Login Failed":
            self.logs.info("Login Unsuccessful")
            self.logs.info("Entered into 'outer elif' block")
            if data_for_login[2] == "fail":
                self.logs.info("Entered into 'inner if block' of 'outer elif block' -->" + data_for_login[2])
                self.logs.info("Appending the list")
                testcase_status_list.append("pass")
                self.logs.info("Capturing Screenshot for Allure Report")
                allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_params_failed',
                              attachment_type=AttachmentType.PNG)
            # elif data_for_login[2] == "pass":
            #     self.logs.info("Entered into 'inner elif block' of 'outer elif block' -->" + data_for_login[2])
            #     self.logs.info("Appending the list")
            #     testcase_status_list.append("fail")
        self.logs.info("Printing the list")
        print(testcase_status_list)
        if "pass" in testcase_status_list:
            self.logs.info("Testcase 'test_login_with_params' has Passed")
            assert True
        else:
            self.logs.info("Testcase 'test_login_with_params' has Failed")
            assert False
        self.logs.info("Testcase 'test_login_with_params' has Completed")
