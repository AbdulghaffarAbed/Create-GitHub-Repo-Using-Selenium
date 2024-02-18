import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import GitHubUtils


def add_new_repository(driver, wait):
    """Helper function to add a new repository to the GitHub account.

      Args:
          driver:The WebDriver instance used to interact with the browser.
          wait: The WebDriverWait.
      """
    new_repo_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/div/a'))
    )
    new_repo_button.click()
    repository_name = wait.until(
        EC.visibility_of_element_located((
            By.XPATH, "//input[@aria-label='Repository']"))
    )
    repository_name.send_keys(GitHubUtils.NEW_REPO_NAME)
    add_readme_checkbox = wait.until(EC.visibility_of_element_located((
        By.XPATH, '//*[@id=":r9:"]')))
    add_readme_checkbox.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    create_repo_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@class='types__StyledButton-sc-ws60qy-0 hjrJiQ']")))
    create_repo_button.click()
    time.sleep(2)
    code_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@class='types__StyledButton-sc-ws60qy-0 jyJtuN']")))
    code_button.click()
    time.sleep(2)

    # Extract the SSH URL for cloning the repository
    ssh_clone_url = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//input[@class='form-control input-monospace input-sm"
             " color-bg-subtle']"))).get_attribute('value')

    print("SSH Clone URL:", ssh_clone_url)
