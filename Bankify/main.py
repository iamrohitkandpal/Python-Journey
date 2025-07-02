import json
import random
import string
from pathlib import Path


class Bankify:
    database = "Bankify/data.json"
    data = []

    @classmethod
    def initialize(cls):
        try:
            Path(cls.database).parent.mkdir(parents=True, exist_ok=True)
            if Path(cls.database).exists():
                with open(cls.database, "r") as fs:
                    cls.data = json.load(fs)
            else:
                with open(cls.database, "w") as fs:
                    json.dump([], fs, indent=4)
                cls.data = []
        except Exception as err:
            print(f"An exception occurred during initialization: {err}")
            cls.data = []

    @classmethod
    def __update(cls):
        try:
            with open(cls.database, "w") as fs:
                json.dump(cls.data, fs, indent=4)
            print("Details Updated Successfully.")
        except Exception as error:
            print(f"Error Updating Details: {error}")

    @classmethod
    def __accountNumber(cls):
        while True:
            alpha = random.choices(string.ascii_letters, k=3)
            numeric = random.choices(string.digits, k=4)
            spchar = random.choices("!@#$%^&*", k=1)
            account = alpha + numeric + spchar
            random.shuffle(account)
            account_num = "".join(account)
            # Ensure the account number is unique
            if not any(user["account"] == "BNY" + account_num for user in cls.data):
                return account_num

    def createAccount(self):
        print("\n\n" + "=" * 50)
        print(f"{'Create New Account ':^50}")
        print("=" * 50)
        try:
            details = {
                "name": input("Enter your name: "),
                "email": input("Enter your email: "),
                "age": int(input("Enter your age: ")),
                "pin": int(input("Enter a 4-digit PIN: ")),
                "account": "BNY" + Bankify.__accountNumber(),
                "balance": 0.0,
            }
            if details["age"] < 18 or len(str(details["pin"])) != 4:
                print(
                    "Please Try Again: Age must be 18 or older, and PIN must be 4 digits."
                )
            else:
                print("\n\nAccount Created Successfully!")
                print(f"Account Number: {details['account']}")
                print(f"Account PIN: {details['pin']}")
                print("\nRemember your account number and PIN.")

                Bankify.data.append(details)
                Bankify.__update()

        except ValueError as e:
            print(
                f"Invalid input: {e}. Please enter valid numeric values for age and PIN."
            )
            self.createAccount()

    def checkDetails(self):
        print("\n\n" + "=" * 50)
        print(f"{' Check Account Details ':^50}")
        print("=" * 50)
        try:
            account = input("Enter your account number: ")
            pin = int(input("Enter your PIN: "))

            userData = [
                i for i in Bankify.data if i["account"] == account and i["pin"] == pin
            ]

            if not userData:
                print("\nInvalid account number or PIN.\n")
            else:
                user = userData[0]
                print("\n" + "=" * 50)
                print(f"{' Account Details ':^50}")
                print("=" * 50)
                print(f"{'Name':<20} | {user['name']}")
                print(f"{'Email':<20} | {user['email']}")
                print(f"{'Age':<20} | {user['age']}")
                print(f"{'Account Number':<20} | {user['account']}")
                print(f"{'Balance':<20} | ${user['balance']:.2f}")
                print("=" * 50 + "\n")

        except ValueError:
            print("Invalid PIN. Please enter a numeric PIN.")
            self.checkDetails()

    def depositMoney(self):
        print("\n\n" + "=" * 50)
        print(f"{'Deposit Money ':^50}")
        print("=" * 50)
        try:
            account = input("Enter your account number: ")
            pin = int(input("Enter your PIN: "))

            userData = [
                i for i in Bankify.data if i["account"] == account and i["pin"] == pin
            ]

            if not userData:
                print("\nInvalid account number or PIN.\n")
            else:
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Please enter a valid amount.")
                elif amount > 10000:
                    print("You can only deposit up to 10000 at a time.")
                else:
                    userData[0]["balance"] += amount
                    Bankify.__update()
                    print("\n\nDeposit successful!")
                    print(
                        f"Deposited ${amount:.2f} || New balance: ${userData[0]['balance']:.2f}\n"
                    )
        except ValueError:
            print(
                "Invalid input. Please enter valid numeric values for PIN and amount."
            )
            self.depositMoney()

    def withdrawMoney(self):
        print("\n\n" + "=" * 50)
        print(f"{'Withdraw Money ':^50}")
        print("=" * 50)
        try:
            account = input("Enter your account number: ")
            pin = int(input("Enter your PIN: "))

            userData = [
                i for i in Bankify.data if i["account"] == account and i["pin"] == pin
            ]

            if not userData:
                print("\nInvalid account number or PIN.\n")
            else:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Please enter a valid amount.")
                elif amount > userData[0]["balance"]:
                    print("Insufficient funds.")
                else:
                    userData[0]["balance"] -= amount
                    Bankify.__update()
                    print("\n\nWithdrawal successful!")
                    print(
                        f"Withdrew ${amount:.2f} || New balance: ${userData[0]['balance']:.2f}\n"
                    )
        except ValueError:
            print(
                "Invalid input. Please enter valid numeric values for PIN and amount."
            )
            self.withdrawMoney()

    def updateDetails(self):
        print("\n\n" + "=" * 50)
        print(f"{'Update Account Details ':^50}")
        print("=" * 50)
        try:
            account = input("Enter your account number: ")
            pin = int(input("Enter your PIN: "))

            userData = [
                i for i in Bankify.data if i["account"] == account and i["pin"] == pin
            ]

            if not userData:
                print("\nInvalid account number or PIN.\n")
            else:
                user = userData[0]
                print("\n" + "=" * 50)
                print(f"{' Update Details ':^50}")
                print("=" * 50)
                print(f"{'Name':<20} | {user['name']}")
                print(f"{'Email':<20} | {user['email']}")
                print(f"{'Age':<20} | {user['age']}")
                print(f"{'Account Number':<20} | {user['account']}")
                print(f"{'Balance':<20} | ${user['balance']:.2f}")
                print("=" * 50 + "\n")

                user["name"] = (
                    input("Enter New Name (Leave for No Change): ") or user["name"]
                )
                user["email"] = (
                    input("Enter New Email (Leave for No Change): ") or user["email"]
                )
                user["pin"] = int(
                    input("Enter New PIN (Leave for No Change): ") or user["pin"]
                )

                if user["pin"] < 1000 or user["pin"] > 9999:
                    raise ValueError("PIN must be a 4-digit number.")

                Bankify.__update()
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid values.")
            self.updateDetails()

    def deleteAccount(self):
        print("\n\n" + "=" * 50)
        print(f"{'Delete Account ':^50}")
        print("=" * 50)
        try:
            account = input("Enter your account number: ")
            pin = int(input("Enter your PIN: "))

            userData = [
                i for i in Bankify.data if i["account"] == account and i["pin"] == pin
            ]

            if not userData:
                print("\nInvalid account number or PIN.\n")
            else:
                confirm = input("Are you sure you want to delete your account? (Yes/No): ").strip().lower()
                if confirm != "yes":
                    print("Account deletion cancelled.")
                    return
                Bankify.data.remove(userData[0])
                Bankify.__update()
                print("\nAccount deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a numeric PIN.")
            self.deleteAccount()

# Initialize the data after the class is defined
Bankify.initialize()

# Main program
user = Bankify()
print("Welcome to Bankify!")
print("Please choose an option:")
print("1. Create Account")
print("2. Check Details")
print("3. Deposit Money")
print("4. Withdraw Money")
print("5. Update Details")
print("6. Delete Account")
print("7. Exit")

try:
    choice = int(input("Enter your choice (1-7): "))
    if choice == 1:
        user.createAccount()
    elif choice == 2:
        user.checkDetails()
    elif choice == 3:
        user.depositMoney()
    elif choice == 4:
        user.withdrawMoney()
    elif choice == 5:
        user.updateDetails()
    elif choice == 6:
        user.deleteAccount()
    elif choice == 7:
        print("Exiting. Thank you for using Bankify!")
    else:
        print("Invalid choice. Please select a valid option.")
except ValueError:
    print("Invalid input. Please enter a number between 1 and 7.")
