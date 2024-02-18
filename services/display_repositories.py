from utils.constants import AccountLicense, GitHubUtils


def show_github_repos(driver):
    """Helper function to navigate and display the GitHub account repositories.

    Args:
        driver:The WebDriver instance used to interact with the browser.
    """
    driver.get(GitHubUtils.GITHUB_REPOSITORIES.format(
        ACCOUNT_USERNAME=AccountLicense.ACCOUNT_USERNAME)
    )
