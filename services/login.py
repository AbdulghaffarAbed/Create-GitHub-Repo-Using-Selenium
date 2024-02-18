"""Login to Google Account Script"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import AccountLicense, GitHubUtils


def login_to_github_account(driver, wait):
    """Helper function that is responsible for login to a specific GitHub
    account using the information provided to the .env file.

    Args:
        driver: The WebDriver instance used to interact with the browser.
        wait: The WebDriverWait.
    """
    # Open GitHub login page

    driver.get(GitHubUtils.LOGIN_URL)

    # Wait for the login page to load
    time.sleep(2)

    username_field = wait.until(
        EC.visibility_of_element_located((By.ID, "login_field"))
    )
    username_field.send_keys(AccountLicense.ACCOUNT_USERNAME)

    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_field.send_keys(AccountLicense.ACCOUNT_PASSWORD)

    login_button = wait.until(
        EC.visibility_of_element_located((By.NAME, "commit"))
    )
    login_button.click()
