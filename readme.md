# Grindr Access

## Overview

`grindrUser.py` is a Python module that provides a set of functions to interact with the Grindr API. Grindr is a popular social networking and dating app. This module allows you to perform various actions, such as logging in, retrieving user profiles, sending taps, getting user information, and more.

## Usage

To use `grindrUser.py`, you should follow these steps:

1. Import the module:

    ```python
    from grindrUser import grindrUser
    ```

2. Create an instance of the `grindrUser` class:

    ```python
    user = grindrUser()
    ```

3. Log in to your Grindr account using your email and password:

    ```python
    user.login("your_email@example.com", "your_password")
    ```

4. Use the provided methods to interact with the Grindr API. Here are some of the available methods:

   - `getProfiles(lat, lon)`: Retrieve user profiles near a specific location.

   - `getTaps()`: Get the list of taps received.

   - `tap(profileId, type)`: Send a tap to a user with the specified profile ID and type.

   - `getProfile(profileId)`: Get the profile information of a user with the specified profile ID.

   - `getProfileStatuses(profileIdList)`: Get the status of multiple profiles using their IDs.

   - `getAlbum(profileId)`: Get the album information of a user with the specified profile ID.

   - `sessions(email)`: Get session data or renew an existing session using an email.

   - `generatePlainAuth()`: Generate plain authentication information.

## Example

Here's an example of how to use the module to retrieve user profiles:

```python
from grindrUser import grindrUser

# Create an instance of the grindrUser class
user = grindrUser()

# Log in to your Grindr account
user.login("your_email@example.com", "your_password")

# Get user profiles near a specific location (e.g., latitude 123.456 and longitude 789.012)
profiles = user.getProfiles(123.456, 789.012)

# Print the response
print(profiles)
```
You can also refer to the example.py file for usage and implementation examples.

## To-Do

- [ ] Integrate an XMPP client for real-time messaging.
- [ ] Document Grindr API.

## Notes

- Make sure to keep your Grindr credentials (email and password) secure and do not share them.

- The `genericRequest`, `paths`, and `utils` modules are used by `grindrUser.py`. Ensure that they are properly configured and available in your Python environment.

- The module provides basic functionality for interacting with the Grindr API. You can extend it or build additional features as needed.

## Disclaimer

Please use this module responsibly and in compliance with Grindr's terms of service and guidelines. Unauthorized use or misuse of the module may violate Grindr's policies and could result in account suspension or legal action. Use this module at your own risk.
