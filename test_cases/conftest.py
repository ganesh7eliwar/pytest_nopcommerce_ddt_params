import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture
def setup(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        print("Test Run --> Chrome Browser")
        driver = webdriver.Chrome()
    elif browser == 'edge':
        print("Test Run --> Edge Browser")
        driver = webdriver.Edge()
    elif browser == 'firefox':
        print("Test Run --> Firefox Browser")
        driver = webdriver.Firefox()
    else:
        print("Test Run --> Headless Browser")
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "pass"),
    ("admin@yourstore.com", "admin1", "fail"),
    ("admin@yourstore.com1", "admin", "fail"),
    ("admin@yourstore.com1", "admi1n", "fail")
])
def data_for_login(request):
    return request.param
