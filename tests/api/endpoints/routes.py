class Routes:
    """
    Defines URLs for CRUD operations related to user management in the pet store API.

    Swagger URL --> https://petstore.swagger.io

    Create user (Post): https://petstore.swagger.io/v2/user
    Get user (Get): https://petstore.swagger.io/v2/user/{username}
    Update user (Put): https://petstore.swagger.io/v2/user/{username}
    Delete user (Delete): https://petstore.swagger.io/v2/user/{username}
    """

    # Base URL for the pet store API
    base_url = "https://petstore.swagger.io/v2"

    # User module endpoints
    post_url = f"{base_url}/user"
    get_url = f"{base_url}/user/{{username}}"
    update_url = f"{base_url}/user/{{username}}"
    delete_url = f"{base_url}/user/{{username}}"
