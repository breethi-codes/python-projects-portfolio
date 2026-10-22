# ================= PASSWORD MANAGER =================
# Features Added:
# 1. User Login & Registration
# 2. Store Passwords
# 3. View All Passwords
# 4. Search By Website
# 5. Update Password
# 6. Delete Password
# 7. Password Generator
# 8. Password Strength Checker
# 9. Change Master Password
# 10. JSON File Storage
# 11. Login Time
# 12. Logout System
# 13. Exception Handling
# ====================================================

import json
import random
import string
from datetime import datetime


class Manager:

    current_user = None
    users = {}
    passwords = {}

    # ================= LOAD DATA =================

    def load_data(self):

        try:
            with open("users.json", "r") as f:
                Manager.users = json.load(f)
        except:
            Manager.users = {"Rohit": "12345"}

        try:
            with open("passwords.json", "r") as f:
                Manager.passwords = json.load(f)
        except:
            Manager.passwords = {
                "Rohit": [
                    {
                        "website": "Instagram",
                        "username": "rohit_123",
                        "password": "insta@123"
                    },
                    {
                        "website": "Gmail",
                        "username": "rohit@gmail.com",
                        "password": "gmail@123"
                    }
                ]
            }

    # ================= SAVE DATA =================

    def save_data(self):

        with open("users.json", "w") as f:
            json.dump(Manager.users, f, indent=4)

        with open("passwords.json", "w") as f:
            json.dump(Manager.passwords, f, indent=4)

    # ================= LOGIN =================

    def login(self):

        print("\n========== LOGIN ==========")

        username = input("Enter Username: ")

        if username not in Manager.users:
            print("Invalid Username")
            return

        password = input("Enter Password: ")

        if Manager.users[username] == password:

            Manager.current_user = username

            print("Login Successful")
            print(f"Login Time : {datetime.now()}")

        else:
            print("Wrong Password")

    # ================= CREATE USER =================

    def create_user(self):

        print("\n========== CREATE USER ==========")

        username = input("Enter Username: ")

        if username in Manager.users:
            print("Username Already Exists")
            return

        password = input("Create Password: ")

        Manager.users[username] = password

        self.save_data()

        print("User Created Successfully")

    # ================= STORE PASSWORD =================

    def add_password(self):

        if not Manager.current_user:
            print("Please Login First")
            return

        print("\n========== STORE PASSWORD ==========")

        website = input("Enter Website Name: ")
        username = input("Enter Website Username: ")

        if Manager.current_user in Manager.passwords:

            for i in Manager.passwords[Manager.current_user]:

                if website == i['website'] and username == i['username']:

                    print("Password Already Stored")
                    return

        password = input("Enter Password: ")

        data = {
            "website": website,
            "username": username,
            "password": password
        }

        if Manager.current_user in Manager.passwords:

            Manager.passwords[Manager.current_user].append(data)

        else:

            Manager.passwords[Manager.current_user] = [data]

        self.save_data()

        print("Password Stored Successfully")

    # ================= VIEW PASSWORDS =================

    def view_all(self):

        if not Manager.current_user:
            print("Please Login First")
            return

        if Manager.current_user not in Manager.passwords:

            print("No Passwords Stored")
            return

        print(f"\n========== {Manager.current_user}'s PASSWORDS ==========")

        count = 0

        for i in Manager.passwords[Manager.current_user]:

            count += 1

            print("\n----------------------------------")
            print(f"Website : {i['website']}")
            print(f"Username: {i['username']}")
            print(f"Password: {i['password']}")

        print("\nTotal Passwords Stored :", count)

    # ================= SEARCH WEBSITE =================

    def search_by_website(self):

        if not Manager.current_user:
            print("Please Login First")
            return

        website = input("Enter Website Name: ")

        if Manager.current_user in Manager.passwords:

            for i in Manager.passwords[Manager.current_user]:

                if website.lower() == i['website'].lower():

                    print("\n========== PASSWORD FOUND ==========")

                    print(f"Website : {i['website']}")
                    print(f"Username: {i['username']}")
                    print(f"Password: {i['password']}")

                    return

        print("Website Not Found")

    # ================= UPDATE PASSWORD =================

    def update_password(self):

        if not Manager.current_user:
            print("Please Login First")
            return

        website = input("Enter Website To Update: ")

        if Manager.current_user in Manager.passwords:

            for i in Manager.passwords[Manager.current_user]:

                if website.lower() == i['website'].lower():

                    username = input("Enter New Username: ")
                    password = input("Enter New Password: ")

                    i['username'] = username
                    i['password'] = password

                    self.save_data()

                    print("Password Updated Successfully")
                    return

        print("Website Not Found")

    # ================= DELETE PASSWORD =================

    def delete_password(self):

        if not Manager.current_user:
            print("Please Login First")
            return

        website = input("Enter Website To Delete: ")

        if Manager.current_user in Manager.passwords:

            for i in Manager.passwords[Manager.current_user]:

                if website.lower() == i['website'].lower():

                    Manager.passwords[Manager.current_user].remove(i)

                    self.save_data()

                    print("Password Deleted Successfully")
                    return

        print("Website Not Found")

    # ================= PASSWORD GENERATOR =================

    def generate_password(self):

        print("\n========== PASSWORD GENERATOR ==========")

        try:

            length = int(input("Enter Password Length: "))

            chars = string.ascii_letters + string.digits + "@#$&"

            password = ""

            for i in range(length):

                password += random.choice(chars)

            print("Generated Password :", password)

        except:
            print("Invalid Input")

    # ================= PASSWORD STRENGTH =================

    def password_strength(self):

        password = input("Enter Password To Check Strength: ")

        if len(password) >= 8:

            if any(i.isdigit() for i in password) and any(
                    i.isupper() for i in password):

                print("Strong Password")

            else:
                print("Medium Password")

        else:
            print("Weak Password")

    # ================= CHANGE MASTER PASSWORD =================

    def change_master_password(self):

        if not Manager.current_user:
            print("Please Login First")
            return

        old = input("Enter Old Password: ")

        if Manager.users[Manager.current_user] == old:

            new = input("Enter New Password: ")

            Manager.users[Manager.current_user] = new

            self.save_data()

            print("Master Password Changed Successfully")

        else:
            print("Wrong Old Password")

    # ================= LOGOUT =================

    def logout(self):

        if Manager.current_user:

            print(f"{Manager.current_user} Logged Out Successfully")

            Manager.current_user = None

        else:
            print("No User Logged In")


# ================= MAIN FUNCTION =================

def main():

    obj = Manager()

    obj.load_data()

    while True:

        print("\n========== PASSWORD MANAGER ==========")

        print("1. Login")
        print("2. Create New User")
        print("3. Store New Password")
        print("4. View All Passwords")
        print("5. Search By Website")
        print("6. Update Password")
        print("7. Delete Password")
        print("8. Generate Password")
        print("9. Password Strength Checker")
        print("10. Change Master Password")
        print("11. Logout")
        print("12. Exit")

        try:

            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                obj.login()

            elif choice == 2:
                obj.create_user()

            elif choice == 3:
                obj.add_password()

            elif choice == 4:
                obj.view_all()

            elif choice == 5:
                obj.search_by_website()

            elif choice == 6:
                obj.update_password()

            elif choice == 7:
                obj.delete_password()

            elif choice == 8:
                obj.generate_password()

            elif choice == 9:
                obj.password_strength()

            elif choice == 10:
                obj.change_master_password()

            elif choice == 11:
                obj.logout()

            elif choice == 12:

                print("Thank You")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Enter Numbers Only")


if __name__ == "__main__":
    main()
