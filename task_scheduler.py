# ================= TASK SCHEDULER APPLICATION =================
# Features Added:
# 1. User Login & Registration
# 2. Add Task
# 3. View Tasks
# 4. Update Task
# 5. Delete Task
# 6. Pending Tasks
# 7. Completed Tasks
# 8. Search Task
# 9. Priority Levels
# 10. Due Date
# 11. Task Statistics
# 12. JSON File Storage
# 13. Logout System
# 14. Exception Handling
# ===============================================================

import json
from datetime import datetime


class Task:

    users = {}
    tasks = {}
    current_user = None

    # ================= LOAD DATA =================

    def load_data(self):

        try:

            with open("users.json", "r") as f:

                Task.users = json.load(f)

        except:

            Task.users = {
                "Rohit": "12345"
            }

        try:

            with open("tasks.json", "r") as f:

                Task.tasks = json.load(f)

        except:

            Task.tasks = {
                "Rohit": [
                    {
                        "id": 1,
                        "task": "Study Python",
                        "status": "Pending",
                        "priority": "High",
                        "due_date": "25-05-2026"
                    },
                    {
                        "id": 2,
                        "task": "Practice Python",
                        "status": "Pending",
                        "priority": "Medium",
                        "due_date": "26-05-2026"
                    }
                ]
            }

    # ================= SAVE DATA =================

    def save_data(self):

        with open("users.json", "w") as f:

            json.dump(Task.users, f, indent=4)

        with open("tasks.json", "w") as f:

            json.dump(Task.tasks, f, indent=4)

    # ================= LOGIN =================

    def login(self):

        print("\n========== LOGIN ==========")

        username = input("Enter Username: ")

        if username not in Task.users:

            print("Invalid Username")
            return

        password = input("Enter Password: ")

        if Task.users[username] == password:

            Task.current_user = username

            print("Login Successful")
            print(f"Login Time : {datetime.now()}")

        else:

            print("Wrong Password")

    # ================= CREATE USER =================

    def create_user(self):

        print("\n========== CREATE USER ==========")

        username = input("Enter Username: ")

        if username in Task.users:

            print("Username Already Exists")
            return

        password = input("Create Password: ")

        Task.users[username] = password

        self.save_data()

        print("User Created Successfully")

    # ================= VIEW TASKS =================

    def view_tasks(self):

        if not Task.current_user:

            print("Please Login First")
            return

        if Task.current_user not in Task.tasks:

            print("No Tasks Found")
            return

        print(f"\n========== {Task.current_user}'s TASKS ==========")

        print("ID\tTask\t\tStatus\t\tPriority\tDue Date")

        for i in Task.tasks[Task.current_user]:

            print(
                f"{i['id']}\t{i['task']}\t{i['status']}\t{i['priority']}\t\t{i['due_date']}"
            )

    # ================= ADD TASK =================

    def add_task(self):

        if not Task.current_user:

            print("Please Login First")
            return

        try:

            print("\n========== ADD TASK ==========")

            task_id = int(input("Enter Task ID: "))

            if Task.current_user in Task.tasks:

                for i in Task.tasks[Task.current_user]:

                    if i['id'] == task_id:

                        print("Task ID Already Exists")
                        return

            task_name = input("Enter Task Details: ")

            priority = input(
                "Enter Priority (High/Medium/Low): ").capitalize()

            due_date = input("Enter Due Date (DD-MM-YYYY): ")

            data = {
                "id": task_id,
                "task": task_name,
                "status": "Pending",
                "priority": priority,
                "due_date": due_date
            }

            if Task.current_user in Task.tasks:

                Task.tasks[Task.current_user].append(data)

            else:

                Task.tasks[Task.current_user] = [data]

            self.save_data()

            print("Task Added Successfully")

        except ValueError:

            print("Invalid Input")

    # ================= DELETE TASK =================

    def delete_task(self):

        if not Task.current_user:

            print("Please Login First")
            return

        try:

            task_id = int(input("Enter Task ID To Delete: "))

            if Task.current_user in Task.tasks:

                for i in Task.tasks[Task.current_user]:

                    if i['id'] == task_id:

                        Task.tasks[Task.current_user].remove(i)

                        self.save_data()

                        print("Task Deleted Successfully")
                        return

            print("Task Not Found")

        except ValueError:

            print("Invalid Input")

    # ================= UPDATE TASK =================

    def update_task(self):

        if not Task.current_user:

            print("Please Login First")
            return

        try:

            task_id = int(input("Enter Task ID To Update: "))

            if Task.current_user in Task.tasks:

                for i in Task.tasks[Task.current_user]:

                    if i['id'] == task_id:

                        ch = input(
                            "Update Task Details? (yes/no): ").lower()

                        if ch == "yes":

                            i['task'] = input("Enter New Task: ")

                        ch = input(
                            "Mark As Completed? (yes/no): ").lower()

                        if ch == "yes":

                            i['status'] = "Completed"

                        else:

                            i['status'] = "Pending"

                        ch = input(
                            "Update Priority? (yes/no): ").lower()

                        if ch == "yes":

                            i['priority'] = input(
                                "Enter Priority: ").capitalize()

                        self.save_data()

                        print("Task Updated Successfully")
                        return

            print("Task Not Found")

        except ValueError:

            print("Invalid Input")

    # ================= PENDING TASKS =================

    def pending_tasks(self):

        if not Task.current_user:

            print("Please Login First")
            return

        print("\n========== PENDING TASKS ==========")

        found = False

        for i in Task.tasks.get(Task.current_user, []):

            if i['status'] == "Pending":

                found = True

                print(
                    f"ID:{i['id']}  Task:{i['task']}  Priority:{i['priority']}"
                )

        if not found:

            print("No Pending Tasks")

    # ================= COMPLETED TASKS =================

    def completed_tasks(self):

        if not Task.current_user:

            print("Please Login First")
            return

        print("\n========== COMPLETED TASKS ==========")

        found = False

        for i in Task.tasks.get(Task.current_user, []):

            if i['status'] == "Completed":

                found = True

                print(
                    f"ID:{i['id']}  Task:{i['task']}  Priority:{i['priority']}"
                )

        if not found:

            print("No Completed Tasks")

    # ================= SEARCH TASK =================

    def search_task(self):

        if not Task.current_user:

            print("Please Login First")
            return

        keyword = input("Enter Task Keyword To Search: ").lower()

        found = False

        for i in Task.tasks.get(Task.current_user, []):

            if keyword in i['task'].lower():

                found = True

                print("\n========== TASK FOUND ==========")

                print(f"Task ID   : {i['id']}")
                print(f"Task      : {i['task']}")
                print(f"Status    : {i['status']}")
                print(f"Priority  : {i['priority']}")
                print(f"Due Date  : {i['due_date']}")

        if not found:

            print("No Matching Task Found")

    # ================= TASK STATISTICS =================

    def task_statistics(self):

        if not Task.current_user:

            print("Please Login First")
            return

        total = len(Task.tasks.get(Task.current_user, []))

        completed = 0
        pending = 0

        for i in Task.tasks.get(Task.current_user, []):

            if i['status'] == "Completed":

                completed += 1

            else:

                pending += 1

        print("\n========== TASK STATISTICS ==========")

        print("Total Tasks      :", total)
        print("Completed Tasks  :", completed)
        print("Pending Tasks    :", pending)

    # ================= LOGOUT =================

    def logout(self):

        if Task.current_user:

            print(f"{Task.current_user} Logged Out Successfully")

            Task.current_user = None

        else:

            print("No User Logged In")


# ================= MAIN FUNCTION =================

def main():

    obj = Task()

    obj.load_data()

    while True:

        print("\n========== TASK SCHEDULER APPLICATION ==========")

        print("1. Login")
        print("2. Create User")
        print("3. View Tasks")
        print("4. Add Task")
        print("5. Update Task")
        print("6. Delete Task")
        print("7. Pending Tasks")
        print("8. Completed Tasks")
        print("9. Search Task")
        print("10. Task Statistics")
        print("11. Logout")
        print("12. Exit")

        try:

            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                obj.login()

            elif choice == 2:
                obj.create_user()

            elif choice == 3:
                obj.view_tasks()

            elif choice == 4:
                obj.add_task()

            elif choice == 5:
                obj.update_task()

            elif choice == 6:
                obj.delete_task()

            elif choice == 7:
                obj.pending_tasks()

            elif choice == 8:
                obj.completed_tasks()

            elif choice == 9:
                obj.search_task()

            elif choice == 10:
                obj.task_statistics()

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
