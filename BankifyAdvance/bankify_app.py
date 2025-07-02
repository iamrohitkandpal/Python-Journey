import streamlit as st
import json
import random
import string
from pathlib import Path
import re

class Bankify:
    database = "Database/data.json"
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
            st.error(f"An error occurred during initialization: {err}")
            cls.data = []

    @classmethod
    def __update(cls):
        try:
            with open(cls.database, "w") as fs:
                json.dump(cls.data, fs, indent=4)
            return True
        except Exception as error:
            st.error(f"Error updating database: {error}")
            return False

    @classmethod
    def __accountNumber(cls):
        while True:
            alpha = random.choices(string.ascii_letters, k=3)
            numeric = random.choices(string.digits, k=4)
            spchar = random.choices("!@#$%^&*", k=1)
            account = alpha + numeric + spchar
            random.shuffle(account)
            account_num = "".join(account)
            if not any(user["account"] == "BNY" + account_num for user in cls.data):
                return account_num

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def create_account():
    st.subheader("Create New Account")
    with st.form("create_account_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        pin = st.text_input("4-digit PIN", type="password")
        submit = st.form_submit_button("Create Account")

        if submit:
            if not name:
                st.error("Name is required")
            elif not validate_email(email):
                st.error("Please enter a valid email address")
            elif age < 18:
                st.error("You must be at least 18 years old")
            elif not pin.isdigit() or len(pin) != 4:
                st.error("PIN must be a 4-digit number")
            else:
                details = {
                    "name": name,
                    "email": email,
                    "age": int(age),
                    "pin": int(pin),
                    "account": "BNY" + Bankify.__accountNumber(),
                    "balance": 0.0,
                }
                Bankify.data.append(details)
                if Bankify.__update():
                    st.success(f"Account created successfully! Account Number: {details['account']}")
                    st.info("Please save your account number and PIN.")

def check_details():
    st.subheader("Check Account Details")
    with st.form("check_details_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        submit = st.form_submit_button("Check Details")

        if submit:
            if not account or not pin:
                st.error("Please fill in all fields")
            elif not pin.isdigit():
                st.error("PIN must be numeric")
            else:
                user_data = [i for i in Bankify.data if i["account"] == account and i["pin"] == int(pin)]
                if not user_data:
                    st.error("Invalid account number or PIN")
                else:
                    user = user_data[0]
                    st.markdown("### Account Details")
                    st.write(f"**Name**: {user['name']}")
                    st.write(f"**Email**: {user['email']}")
                    st.write(f"**Age**: {user['age']}")
                    st.write(f"**Account Number**: {user['account']}")
                    st.write(f"**Balance**: ${user['balance']:.2f}")

def deposit_money():
    st.subheader("Deposit Money")
    with st.form("deposit_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Amount to Deposit", min_value=0.0, step=0.01)
        submit = st.form_submit_button("Deposit")

        if submit:
            if not account or not pin or not amount:
                st.error("Please fill in all fields")
            elif not pin.isdigit():
                st.error("PIN must be numeric")
            elif amount <= 0:
                st.error("Please enter a valid amount")
            elif amount > 10000:
                st.error("Maximum deposit amount is $10,000")
            else:
                user_data = [i for i in Bankify.data if i["account"] == account and i["pin"] == int(pin)]
                if not user_data:
                    st.error("Invalid account number or PIN")
                else:
                    user_data[0]["balance"] += amount
                    if Bankify.__update():
                        st.success(f"Deposited ${amount:.2f} successfully! New balance: ${user_data[0]['balance']:.2f}")

def withdraw_money():
    st.subheader("Withdraw Money")
    with st.form("withdraw_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Amount to Withdraw", min_value=0.0, step=0.01)
        submit = st.form_submit_button("Withdraw")

        if submit:
            if not account or not pin or not amount:
                st.error("Please fill in all fields")
            elif not pin.isdigit():
                st.error("PIN must be numeric")
            elif amount <= 0:
                st.error("Please enter a valid amount")
            else:
                user_data = [i for i in Bankify.data if i["account"] == account and i["pin"] == int(pin)]
                if not user_data:
                    st.error("Invalid account number or PIN")
                elif amount > user_data[0]["balance"]:
                    st.error("Insufficient funds")
                else:
                    user_data[0]["balance"] -= amount
                    if Bankify.__update():
                        st.success(f"Withdrew ${amount:.2f} successfully! New balance: ${user_data[0]['balance']:.2f}")

def update_details():
    st.subheader("Update Account Details")
    with st.form("update_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        new_name = st.text_input("New Name (leave blank to keep current)")
        new_email = st.text_input("New Email (leave blank to keep current)")
        new_pin = st.text_input("New PIN (leave blank to keep current)", type="password")
        submit = st.form_submit_button("Update Details")

        if submit:
            if not account or not pin:
                st.error("Please enter account number and PIN")
            elif not pin.isdigit():
                st.error("PIN must be numeric")
            else:
                user_data = [i for i in Bankify.data if i["account"] == account and i["pin"] == int(pin)]
                if not user_data:
                    st.error("Invalid account number or PIN")
                else:
                    user = user_data[0]
                    if new_name:
                        user["name"] = new_name
                    if new_email and validate_email(new_email):
                        user["email"] = new_email
                    elif new_email:
                        st.error("Please enter a valid email address")
                        return
                    if new_pin:
                        if new_pin.isdigit() and len(new_pin) == 4:
                            user["pin"] = int(new_pin)
                        else:
                            st.error("New PIN must be a 4-digit number")
                            return
                    if Bankify.__update():
                        st.success("Account details updated successfully!")

def delete_account():
    st.subheader("Delete Account")
    with st.form("delete_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        confirm = st.checkbox("I confirm I want to delete my account")
        submit = st.form_submit_button("Delete Account")

        if submit:
            if not account or not pin:
                st.error("Please enter account number and PIN")
            elif not pin.isdigit():
                st.error("PIN must be numeric")
            elif not confirm:
                st.error("Please confirm account deletion")
            else:
                user_data = [i for i in Bankify.data if i["account"] == account and i["pin"] == int(pin)]
                if not user_data:
                    st.error("Invalid account number or PIN")
                else:
                    Bankify.data.remove(user_data[0])
                    if Bankify.__update():
                        st.success("Account deleted successfully!")

def main():
    Bankify.initialize()
    st.title("Bankify - Banking Application")
    
    menu = [
        "Create Account",
        "Check Details",
        "Deposit Money",
        "Withdraw Money",
        "Update Details",
        "Delete Account"
    ]
    
    choice = st.sidebar.selectbox("Select Operation", menu)
    
    if choice == "Create Account":
        create_account()
    elif choice == "Check Details":
        check_details()
    elif choice == "Deposit Money":
        deposit_money()
    elif choice == "Withdraw Money":
        withdraw_money()
    elif choice == "Update Details":
        update_details()
    elif choice == "Delete Account":
        delete_account()

if __name__ == "__main__":
    main()