from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from services.add_repository import add_new_repository
from utils.constants import PageLoadConfig
from services.login import login_to_github_account
from services.display_repositories import (show_github_repos)


def setup_chrome_driver():
    """Helper function that will define a Chrome driver and WebDriverWait.

    Returns:
         dict: Dictionary of Chrome driver and WebDriverWait
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, PageLoadConfig.WAIT_TIMEOUT)
    return {"driver": driver, "wait": wait}


def main():
    """The Entry point of Creating a new repository for the given GitHub
    account.
    """
    driver_setup = setup_chrome_driver()
    driver = driver_setup.get("driver")
    wait = driver_setup.get("wait")
    login_to_github_account(
        driver=driver, wait=wait
    )
    show_github_repos(driver=driver)
    add_new_repository(driver=driver, wait=wait)


if __name__ == "__main__":
    main()
