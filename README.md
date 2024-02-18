# Create-GitHub-Repo-Using-Selenium

## Description

Create GitHub Repository project is a Python automation script that
utilizes Selenium to streamline the process of creating a new repository on
GitHub. By providing necessary credentials and repository details through a .env
file, the script automates the steps of logging in to a GitHub account, creating
a new repository with a README file, and retrieving the SSH URL for the newly
created repository. This project aims to simplify and expedite the repository
creation process, eliminating the need for manual intervention.

## Features

- Automated login to GitHub account.
- Creation of a new repository with a specified name.
- Addition of a README file to the newly created repository.
- Retrieval of the SSH URL for the created repository.
- Simple and intuitive setup using environment variables stored in a .env file.

## Prerequisites
1. Python and pip installed on the local machine.
2. Installation of required Python packages using the provided requirements 
   file.

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages by running:
   
    ``` pip install -r requirements.txt```
4. Fill the .env file with your GitHub Account license and the name of the 
   new repository.
5. Run the project using the controller file as below:

    ```python add_repo_controller.py```