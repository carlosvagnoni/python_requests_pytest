class User:
    """
    Represents a user entity for interaction with the API.
    This class models user data including their ID, username, name, email, password, phone, and user status.
    """

    def __init__(self):
        self.id = 0
        self.username = ""
        self.firstname = ""
        self.lastname = ""
        self.email = ""
        self.password = ""
        self.phone = ""
        self.user_status = 0

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_firstname(self):
        return self.firstname

    def set_firstname(self, firstname):
        self.firstname = firstname

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_user_status(self):
        return self.user_status

    def set_user_status(self, user_status):
        self.user_status = user_status
