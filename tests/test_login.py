import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import setup_teardown


# Login
@pytest.mark.usefixtures("setup_teardown")
class TestLogin:
    def test_login(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_element(By.XPATH, "*//span[@class='title']").is_displayed()
