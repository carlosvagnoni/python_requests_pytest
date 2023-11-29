"""
Module Description: This file contains a test suite for API endpoints related to user management. It utilizes the
pytest framework to run parameterized tests using Excel data for various user-related operations.

Functions:
- test_post_user_ddt: Sends a POST request to create a user using data from an Excel sheet.
- test_get_user_by_username: Sends a GET request to retrieve user data by username using Excel data for parameters.
- test_delete_user_by_username: Sends a DELETE request to remove a user by username using Excel data.
"""

import logging
import pytest
import logging.config
from tests.api.endpoints.user_endpoints import UserEndPoints
from tests.api.payload.user import User
from tests.api.utilities.excel_helper import get_excel_data

logging.config.fileConfig('logging.conf')


@pytest.fixture(scope="module")
def logger():
    log = logging.getLogger(__name__)
    return log


@pytest.mark.run(order=5)
@pytest.mark.parametrize(
    "user_id, username, firstname, lastname, user_email, password, phone_number",
    get_excel_data("Userdata.xlsx", "Sheet1")
)
def test_post_user_ddt(logger, user_id, username, firstname, lastname, user_email, password, phone_number):
    logger.info("DDTest: Create User")

    user_payload = User()
    user_payload.set_id(user_id)
    user_payload.set_username(username)
    user_payload.set_firstname(firstname)
    user_payload.set_lastname(lastname)
    user_payload.set_email(user_email)
    user_payload.set_password(password)
    user_payload.set_phone(phone_number)

    response = UserEndPoints.create_user(user_payload)

    assert response.status_code == 200
    response_json = response.json()
    assert int(response_json['message']) == user_payload.get_id()


@pytest.mark.run(order=6)
@pytest.mark.parametrize(
    "user_id, username",
    [(row[0], row[1]) for row in get_excel_data("Userdata.xlsx", "Sheet1")]
)
def test_get_user_by_username_ddt(logger, user_id, username):
    logger.info("DDTest: Read User")
    response = UserEndPoints.read_user(username)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json['username'] == username
    assert int(response_json['id']) == user_id


@pytest.mark.run(order=7)
@pytest.mark.parametrize(
    "username",
    [data[1] for data in get_excel_data("Userdata.xlsx", "Sheet1")]
)
def test_delete_user_by_username_ddt(logger, username):
    logger.info("DDTest: Delete User")
    response = UserEndPoints.delete_user(username)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json['message'] == username
