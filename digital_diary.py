# ================= DIGITAL DIARY APPLICATION =================
# Features Added:
# 1. Login System
# 2. New User Registration
# 3. Open Diary
# 4. Add Diary Entry
# 5. Edit Diary Entry
# 6. Delete Diary Entry
# 7. Search By Date
# 8. Search By Title
# 9. Change Password
# 10. Entry Counter
# 11. Login Time
# 12. File Handling using JSON
# 13. Exception Handling
# 14. Logout System
# =============================================================

import json
from datetime import datetime


class Diary:

    users = {}
    entries = {}
    current_user = None

    # ================= LOAD DATA =================

    def load_data(self):

        try:
            with open("users.json", "r") as f:
                Diary.users = json.load(f)
        except:
            Diary.users = {"Rohit": "12345"}

        try:
            with open("entries.json", "r") as f:
                Diary.entries = json.load(f)
        except:
            Diary.entries = {
                "Rohit": [
                    {
                        "date": "15-05-2026",
                        "title": "College",
                        "content": "Attended Python and SQL classes."
                    }
                ]
            }

    # ================= SAVE DATA =================

    def save_data(self):

        with open("users.json", "w") as f:
            json.dump(Diary.users, f, indent=4)

        with open("entries.json", "w") as f:
            json.dump(Diary.entries, f, indent=4)

    # ================= LOGIN =================

    def login(self):

        print("\n========== LOGIN ==========")

        username = input("Enter Username: ")

        if username not in Diary.users:
            print("Invalid Username")
            return

        password = input("Enter Password: ")

        if Diary.users[username] == password:

            Diary.current_user = username

            print("Login Successful")
            print(f"Login Time : {datetime.now()}")

        else:
            print("Wrong Password")

    # ================= REGISTER =================

    def create_new_user(self):

        print("\n========== CREATE NEW USER ==========")

        username = input("Enter Username: ")

        if username in Diary.users:
            print("Username Already Exists")
            return

        password = input("Create Password: ")

        Diary.users[username] = password

        self.save_data()

        print("User Created Successfully")

    # ================= OPEN DIARY =================

    def open_diary(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        print(f"\n========== {Diary.current_user}'s DIARY ==========")

        if Diary.current_user not in Diary.entries:
            print("No Diary Entries Found")
            return

        count = 0

        for i in Diary.entries[Diary.current_user]:

            count += 1

            print("\n-----------------------------------")
            print(f"Date    : {i['date']}")
            print(f"Title   : {i['title']}")
            print(f"Content : {i['content']}")

        print("\nTotal Entries :", count)

    # ================= ADD ENTRY =================

    def add_content(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        print("\n========== ADD DIARY ENTRY ==========")

        date = input("Enter Date (DD-MM-YYYY): ")
        title = input("Enter Title: ")
        content = input("Enter Content: ")

        data = {
            "date": date,
            "title": title,
            "content": content
        }

        if Diary.current_user in Diary.entries:

            Diary.entries[Diary.current_user].append(data)

        else:

            Diary.entries[Diary.current_user] = [data]

        self.save_data()

        print("Diary Entry Added Successfully")

    # ================= EDIT ENTRY =================

    def edit_content(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        if Diary.current_user not in Diary.entries:
            print("No Entries Found")
            return

        date = input("Enter Date To Edit: ")

        for i in Diary.entries[Diary.current_user]:

            if i['date'] == date:

                print("\nCurrent Title :", i['title'])
                print("Current Content :", i['content'])

                ch = input("Edit Title? (yes/no): ")

                if ch.lower() == "yes":

                    new_title = input("Enter New Title: ")
                    i['title'] = new_title

                ch = input("Edit Content? (yes/no): ")

                if ch.lower() == "yes":

                    new_content = input("Enter New Content: ")
                    i['content'] = new_content

                self.save_data()

                print("Diary Updated Successfully")
                return

        print("Date Not Found")

    # ================= DELETE ENTRY =================

    def delete_entry(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        if Diary.current_user not in Diary.entries:
            print("No Entries Found")
            return

        date = input("Enter Date To Delete Entry: ")

        for i in Diary.entries[Diary.current_user]:

            if i['date'] == date:

                Diary.entries[Diary.current_user].remove(i)

                self.save_data()

                print("Diary Entry Deleted Successfully")
                return

        print("Date Not Found")

    # ================= SEARCH BY DATE =================

    def search_date(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        date = input("Enter Date To Search: ")

        if Diary.current_user in Diary.entries:

            for i in Diary.entries[Diary.current_user]:

                if i['date'] == date:

                    print("\n========== ENTRY FOUND ==========")

                    print(f"Date    : {i['date']}")
                    print(f"Title   : {i['title']}")
                    print(f"Content : {i['content']}")

                    return

        print("No Entry Found")

    # ================= SEARCH BY TITLE =================

    def search_title(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        title = input("Enter Title To Search: ").lower()

        found = False

        if Diary.current_user in Diary.entries:

            for i in Diary.entries[Diary.current_user]:

                if title in i['title'].lower():

                    print("\n========== ENTRY FOUND ==========")

                    print(f"Date    : {i['date']}")
                    print(f"Title   : {i['title']}")
                    print(f"Content : {i['content']}")

                    found = True

        if not found:
            print("No Matching Title Found")

    # ================= CHANGE PASSWORD =================

    def change_password(self):

        if not Diary.current_user:
            print("Please Login First")
            return

        old = input("Enter Old Password: ")

        if Diary.users[Diary.current_user] == old:

            new = input("Enter New Password: ")

            Diary.users[Diary.current_user] = new

            self.save_data()

            print("Password Changed Successfully")

        else:
            print("Wrong Old Password")

    # ================= LOGOUT =================

    def logout(self):

        if Diary.current_user:

            print(f"{Diary.current_user} Logged Out Successfully")

            Diary.current_user = None

        else:
            print("No User Logged In")


# ================= MAIN FUNCTION =================

def main():

    obj = Diary()

    obj.load_data()

    while True:

        print("\n========== DIGITAL DIARY APPLICATION ==========")

        print("1. Login")
        print("2. Create New User")
        print("3. Open Diary")
        print("4. Add Diary Entry")
        print("5. Edit Diary Entry")
        print("6. Delete Diary Entry")
        print("7. Search Diary By Date")
        print("8. Search Diary By Title")
        print("9. Change Password")
        print("10. Logout")
        print("11. Exit")

        try:

            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                obj.login()

            elif choice == 2:
                obj.create_new_user()

            elif choice == 3:
                obj.open_diary()

            elif choice == 4:
                obj.add_content()

            elif choice == 5:
                obj.edit_content()

            elif choice == 6:
                obj.delete_entry()

            elif choice == 7:
                obj.search_date()

            elif choice == 8:
                obj.search_title()

            elif choice == 9:
                obj.change_password()

            elif choice == 10:
                obj.logout()

            elif choice == 11:

                print("Thank You")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Enter Numbers Only")


if __name__ == "__main__":
    main()
