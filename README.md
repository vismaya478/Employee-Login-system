# Employee Login System

## Project Overview

This is a menu-driven Python application that implements an Employee Login and Access Control System. It uses exception handling to manage invalid login attempts, logging to record login activity, and a custom decorator to restrict access to selected functions.

## Features

- Employee authentication using username and password.
- Limited login attempts (maximum of 3 failed attempts).
- Custom exception handling for invalid credentials and empty inputs.
- Logging of successful and failed login attempts.
- A custom `login_required` decorator to protect restricted functions.
- Public functions that can be accessed without logging in.
- Logout functionality to reset the authentication state.

## Login Credentials

| Username | Password |
|---|---|
| quest | quest123 |

## Menu Options

1. Home
2. About
3. Login
4. Profile
5. Employee Dashboard
6. Logout
7. Exit

## Function Access

| Function | Access |
|---|---|
| `Home()` | Public |
| `About()` | Public |
| `Profile()` | Protected |
| `EmployeeDashboard()` | Protected |

The `Profile()` and `EmployeeDashboard()` functions require a successful login. The `Home()` and `About()` functions are accessible without authentication.

## Exception Handling

The application uses `try`, `except`, `else` and `finally` blocks in the login workflow.

- **try:** Validates the entered username and password.
- **except:** Handles the custom `InvalidLoginError` exception.
- **else:** Executes when the login is successful and no exception occurs.
- **finally:** Executes regardless of whether the login attempt succeeds or fails.

A custom exception named `InvalidLoginError` is used to handle invalid credentials and empty username or password inputs. The `raise` statement is used to trigger the exception when validation fails.

The system allows a maximum of three failed login attempts.

## Logging

The Python `logging` module is used to record login activity in `employee_login.log`.

- **INFO:** Records successful login.
- **WARNING:** Records failed login attempts.
- **ERROR:** Records when the maximum login attempt limit is reached.

Passwords are not recorded in the log file.

## Decorator

The custom `login_required` decorator checks whether the employee is logged in before allowing a protected function to execute.

If the employee is not logged in, an access-denied message is displayed. If the employee is logged in, the protected function is allowed to execute.

## Logout

The logout function resets the authentication state by setting `logged` to `False`. After logout, protected functions can no longer be accessed until the employee logs in again.

## How to Run

1. Make sure Python is installed.
2. Save the source code as `login.py`.
3. Open a terminal in the project folder.
4. Run the following command:

    python login.py

The log file `employee_login.log` is generated automatically when login activity is recorded.

## Technologies Used

- Python
- Exception Handling
- Logging Module
- Decorators

## Testing

The following scenarios can be tested:

- Access Home and About without logging in.
- Attempt to access Profile before login.
- Enter incorrect credentials.
- Enter empty username or password.
- Log in using the correct credentials.
- Access Profile and Employee Dashboard after login.
- Exceed the maximum number of failed login attempts.
- Logout and attempt to access protected functions again.