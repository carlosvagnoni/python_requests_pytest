import json

import requests

from tests.api.endpoints.routes import Routes


class UserEndPoints:
    """
    Handles user-related API endpoints by encapsulating HTTP requests using RestAssured.

    This class provides methods to perform CRUD (Create, Read, Update, Delete) operations on user data.
    """

    @staticmethod
    def create_user(payload):
        """
        Creates a new user via POST request.
        """
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(Routes.post_url, headers=headers, json=payload.__dict__)
        return response

    @staticmethod
    def read_user(username):
        """
        Retrieves user details via GET request.
        """
        url = Routes.get_url.format(username=username)
        response = requests.get(url)
        return response

    @staticmethod
    def update_user(username, payload):
        """
        Updates user information via PUT request.
        """
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        url = Routes.update_url.format(username=username)
        response = requests.put(url, headers=headers, json=payload.__dict__)
        return response

    @staticmethod
    def delete_user(username):
        """
        Deletes a user via DELETE request.
        """
        url = Routes.delete_url.format(username=username)
        response = requests.delete(url)
        return response
