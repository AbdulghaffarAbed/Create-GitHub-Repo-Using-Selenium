"""Constants used in the Logic"""
import os
from dotenv import load_dotenv

CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(CURRENT_DIR_PATH, "../.env"))


class AccountLicense:
    """Account license contains the required license to log in to the GitHub
    account from the .env file values"""
    ACCOUNT_USERNAME = os.getenv("ACCOUNT_EMAIL")
    ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")


class GitHubUtils:
    """Paths to access GitHub features"""
    LOGIN_URL = "https://github.com/login"
    NEW_REPO_NAME = os.getenv("NEW_REPO_NAME")
    GITHUB_REPOSITORIES = (
        "https://github.com/{ACCOUNT_USERNAME}?tab=repositories")


class PageLoadConfig:
    """PageLoadConfig contains the wait time for the page to be loaded"""
    WAIT_TIMEOUT = 20
