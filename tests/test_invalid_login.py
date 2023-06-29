import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import setup_teardown


# Login
@pytest.mark.usefixtures("setup_teardown")
class TestInvalidLogin:
    def test_invalid_login(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce123")
        driver.find_element(By.ID, "login-button").click()
        assert driver.find_elements(By.XPATH, "//div[@class='error-message-container error']")
