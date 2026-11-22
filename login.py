import logging

logging.basicConfig(
    filename="employee_login.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logged = False
failed_attempts = 0
max_attempts = 3


class InvalidLoginError(Exception):
    pass


def Login():
    global logged, failed_attempts

    if failed_attempts >= max_attempts:
        print("Maximum login attempts reached.")
        logging.error("Maximum login attempts reached")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        if username == "" or password == "":
            raise InvalidLoginError("Username or password cannot be empty.")

        if username == "quest" and password == "quest123":
            logged = True
            print("Login successful!")
            logging.info("Successful login")
        else:
            raise InvalidLoginError("Invalid username or password.")

    except InvalidLoginError as e:
        failed_attempts += 1
        print(e)
        logging.warning("Failed login attempt")

    else:
        print("Welcome, employee!")

    finally:
        print("Process completed.")

    if failed_attempts >= max_attempts:
        print("Maximum login attempts reached. Login is blocked.")
        logging.error("Maximum login attempts reached")


def login_required(func):
    def wrapper():
        if logged:
            func()
        else:
            print("Access denied. Please login first.")
    return wrapper


def Home():
    print("Welcome to the Home page.")


def About():
    print("Employee Login System")


@login_required
def Profile():
    print("Welcome to your Profile.")


@login_required
def EmployeeDashboard():
    print("Welcome to the Employee Dashboard.")


def Logout():
    global logged

    if logged:
        logged = False
        print("Logged out successfully.")
    else:
        print("You are not logged in.")


while True:
    print("\n----- Employee Login System -----")
    print("1. Home")
    print("2. About")
    print("3. Login")
    print("4. Profile")
    print("5. Employee Dashboard")
    print("6. Logout")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Home()

    elif choice == "2":
        About()

    elif choice == "3":
        Login()

    elif choice == "4":
        Profile()

    elif choice == "5":
        EmployeeDashboard()

    elif choice == "6":
        Logout()

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")