# Automated API Testing with Python, Requests, and Pytest
![Static Badge](https://img.shields.io/badge/Python-logo?style=for-the-badge&logo=python&logoColor=rgb(255%2C%20221%2C%2084)&labelColor=rgb(61%2C%20121%2C%20170)&color=rgb(22%2C%2027%2C%2034))
![Static Badge](https://img.shields.io/badge/Requests-logo?style=for-the-badge&logo=requests&logoColor=rgb(255%2C%20192%2C%200)&labelColor=rgb(192%2C%200%2C%200)&color=rgb(22%2C%2027%2C%2034))
![Static Badge](https://img.shields.io/badge/Pytest-logo?style=for-the-badge&logo=pytest&logoColor=rgb(0%2C%20160%2C%20228)&labelColor=white&color=rgb(22%2C%2027%2C%2034))

This project offers a framework and tools for automated API testing using Python, Requests, and Pytest, following Data-Driven Testing (DDT) best practices and employing the Service Object Model design pattern.

## Testing Swagger Petstore User Management Endpoints 🧪

This suite of tests is focused on validating and testing CRUD (Create, Read, Update, Delete) operations related to user management within the Swagger Petstore API (Base URL: https://petstore.swagger.io). Specifically, the tests interact with the following endpoints:

- Create User (POST): Endpoint URL: https://petstore.swagger.io/v2/user
- Get User (GET): Endpoint URL: https://petstore.swagger.io/v2/user/{username}
- Update User (PUT): Endpoint URL: https://petstore.swagger.io/v2/user/{username}
- Delete User (DELETE): Endpoint URL: https://petstore.swagger.io/v2/user/{username}

These tests are designed to ensure the functionality and correctness of these user management endpoints provided by the Swagger Petstore API. They interact with the defined URLs in the Routes class to perform comprehensive testing of user-related functionalities.

## Table of Contents 📑
- [Requirements](#requirements)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Test Execution](#test-execution)
- [Contact](#contact)

## <a id="requirements">Requirements 📋</a>

- Python 3.10.11
- Requests 2.31.0
- Pytest 7.4.3
- Faker 20.1.0
- Openpyxl 3.1.2
- allure-pytest 2.13.2

## <a id="folder-structure">Folder Structure 📂</a>

- **logging.conf:** Configuration file for logging setup.
- **requirements.txt:** File listing required Python packages for the project.
- **run.bat:** Script file specifically designed for execution in Windows environments.

### Directory "test_data"

- **Userdata.xlsx:** Excel file containing user data used in testing.

### Directory "tests/api"

#### Directory "endpoints"

- **routes.py:** Defines URLs for CRUD operations related to user management.
- **user_endpoints.py:** Encapsulates HTTP requests for user-related API endpoints.

#### Directory "payload"

- **user.py:** Class representing user data for API operations.

#### Directory "test"

- **ddt_user_test.py:** Implements Data-Driven Testing (DDT) for users.
- **user_test.py:** Contains test methods to perform CRUD operations on user endpoints using generated/fake data.

#### Directory "utilities"

- **excel_helper.py:** Handles Excel file operations.

## <a id="installation">Installation 🛠️</a>

1. Clone this repository:

    ```bash
    git clone https://github.com/carlosvagnoni/python_requests_pytest.git
    cd python_requests_pytest
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## <a id="configuration">Configuration ⚙️</a>

- Userdata.xlsx can be modified to add any necessary data. The file accepts an arbitrary amount of data, accommodating any quantity of entries.

## <a id="test-execution">Test Execution ▶️</a>

Run all the tests:

```bash
pytest --alluredir=test_results/report_allure
```

Open report:

```bash
allure serve test_results/report_allure
```

**NOTE:**

- Set up the respective environment variables beforehand.
- On Windows environments, you can directly execute the `run.bat` file.

## <a id="contact">Contact 📧</a>

If you have any questions or suggestions, feel free to contact me through my social media accounts.

Thank you for your interest in this project!
