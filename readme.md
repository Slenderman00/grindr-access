# Grindr Access

## Overview

`grindr_user.py` is a Python module that provides a set of functions to interact with the Grindr API. Grindr is a popular social networking and dating app. This module allows you to perform various actions, such as logging in, retrieving user profiles, sending taps, getting user information, and more.

## Usage

To use `grindrUser.py`, you should follow these steps:

1. Import the module:

    ```python
    from grindr_user import GrindrUser
    ```

2. Create an instance of the `GrindrUser` class:

    ```python
    user = GrindrUser()
    ```

3. Log in to your Grindr account using your email and password:

    ```python
    user.login("your_email@example.com", "your_password")
    ```

4. Use the provided methods to interact with the Grindr API. Here are some of the available methods:

   - `get_profiles(lat, lon)`: Retrieve user profiles near a specific location.

   - `get_taps()`: Get the list of taps received.

   - `tap(profileId, type)`: Send a tap to a user with the specified profile ID and type.

   - `get_profile(profileId)`: Get the profile information of a user with the specified profile ID.

   - `get_profileStatuses(profileIdList)`: Get the status of multiple profiles using their IDs.

   - `get_album(profileId)`: Get the album information of a user with the specified profile ID.

   - `sessions(email)`: Get session data or renew an existing session using an email.

   - `generate_plain_auth()`: Generate plain authentication information.

## Example

Here's an example of how to use the module to retrieve user profiles:

```python
from grindr_user import GrindrUser

# Create an instance of the GrindrUser class
user = GrindrUser()

# Log in to your Grindr account
user.login("your_email@example.com", "your_password")

# Get user profiles near a specific location (e.g., latitude 123.456 and longitude 789.012)
profiles = user.get_profiles(123.456, 789.012)

# Print the response
print(profiles)
```
You can also refer to the example.py file for usage and implementation examples.

## To-Do

- [ ] gen_l_dev_info should be consistent over multiple requests.
- [ ] Integrate an XMPP client for real-time messaging.
- [ ] Document Grindr API.

## Notes

- Make sure to keep your Grindr credentials (email and password) secure and do not share them.

- The `generic_request`, `paths`, and `utils` modules are used by `grindr_user.py`. Ensure that they are properly configured and available in your Python environment.

- The module provides basic functionality for interacting with the Grindr API. You can extend it or build additional features as needed.

## Disclaimer

Please use this module responsibly and in compliance with Grindr's terms of service and guidelines. Unauthorized use or misuse of the module may violate Grindr's policies and could result in account suspension or legal action. Use this module at your own risk.
