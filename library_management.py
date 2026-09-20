# ================= LIBRARY MANAGEMENT SYSTEM =================
# Features Added:
# 1. View Books
# 2. Add Book
# 3. Search Book
# 4. Issue Book
# 5. Return Book
# 6. Fine Calculation
# 7. Student Registration
# 8. Book Availability Status
# 9. Book Delete Option
# 10. View Issued Books
# 11. JSON File Storage
# 12. Exception Handling
# 13. Library Revenue From Fines
# =============================================================

from datetime import datetime
import json


class Library:

    books = {}
    students = {}
    issued_books = {}
    total_fine = 0

    # ================= LOAD DATA =================

    def load_data(self):

        try:

            with open("books.json", "r") as f:

                Library.books = json.load(f)

        except:

            Library.books = {
                "1": ['My Life Story', 450, "yes"],
                "2": ['India History', 550, "yes"],
                "3": ['Cars History', 300, "yes"],
                "4": ['Moto History', 700, "yes"]
            }

        try:

            with open("students.json", "r") as f:

                Library.students = json.load(f)

        except:

            Library.students = {}

        try:

            with open("issued_books.json", "r") as f:

                Library.issued_books = json.load(f)

        except:

            Library.issued_books = {}

    # ================= SAVE DATA =================

    def save_data(self):

        with open("books.json", "w") as f:
            json.dump(Library.books, f, indent=4)

        with open("students.json", "w") as f:
            json.dump(Library.students, f, indent=4)

        with open("issued_books.json", "w") as f:
            json.dump(Library.issued_books, f, indent=4)

    # ================= VIEW BOOKS =================

    def view_books(self):

        print("\n========== BOOK DETAILS ==========")

        print("BookID\tBook Name\t\tPrice\tAvailable")

        for k, v in Library.books.items():

            print(f"{k}\t{v[0]}\t{v[1]}\t{v[2]}")

    # ================= ADD BOOK =================

    def add_book(self):

        try:

            book_id = input("Enter Book ID: ")

            if book_id in Library.books:

                print("Book ID Already Exists")
                return

            book_name = input("Enter Book Name: ")

            book_price = int(input("Enter Book Price: "))

            Library.books[book_id] = [
                book_name,
                book_price,
                "yes"
            ]

            self.save_data()

            print(f"{book_name} Added Successfully")

        except ValueError:

            print("Invalid Input")

    # ================= DELETE BOOK =================

    def delete_book(self):

        book_id = input("Enter Book ID To Delete: ")

        if book_id in Library.books:

            del Library.books[book_id]

            self.save_data()

            print("Book Deleted Successfully")

        else:

            print("Book Not Found")

    # ================= SEARCH BOOK =================

    def search_book(self):

        name = input("Enter Book Name To Search: ").lower()

        found = False

        for k, v in Library.books.items():

            if name in v[0].lower():

                found = True

                print("\n========== BOOK FOUND ==========")

                print("Book ID    :", k)
                print("Book Name  :", v[0])
                print("Price      :", v[1])
                print("Available  :", v[2])

        if not found:

            print("No Matching Book Found")

    # ================= REGISTER STUDENT =================

    def register_student(self):

        student_id = input("Enter Student ID: ")

        if student_id in Library.students:

            print("Student Already Registered")
            return

        name = input("Enter Student Name: ")

        dept = input("Enter Department: ")

        Library.students[student_id] = {

            "name": name,
            "department": dept
        }

        self.save_data()

        print("Student Registered Successfully")

    # ================= ISSUE BOOK =================

    def issue_book(self):

        try:

            student_id = input("Enter Student ID: ")

            if student_id not in Library.students:

                print("Student Not Registered")
                return

            book_id = input("Enter Book ID: ")

            if book_id not in Library.books:

                print("Invalid Book ID")
                return

            if Library.books[book_id][2] == "no":

                print("Book Already Issued")
                return

            deposit = int(input("Enter Deposit Amount: "))

            if Library.books[book_id][1] <= 500 and deposit < 500:

                print("Deposit Must Be Minimum 500")
                return

            if Library.books[book_id][1] > 500 and deposit < 1000:

                print("Deposit Must Be Minimum 1000")
                return

            issue_time = str(datetime.now())

            Library.books[book_id][2] = "no"

            Library.issued_books[book_id] = {

                "student_id": student_id,
                "student_name": Library.students[student_id]['name'],
                "issue_time": issue_time,
                "deposit": deposit
            }

            self.save_data()

            print("Book Issued Successfully")

        except ValueError:

            print("Invalid Input")

    # ================= VIEW ISSUED BOOKS =================

    def view_issued_books(self):

        if not Library.issued_books:

            print("No Books Issued")
            return

        print("\n========== ISSUED BOOKS ==========")

        for k, v in Library.issued_books.items():

            print("\nBook ID      :", k)
            print("Student ID   :", v['student_id'])
            print("Student Name :", v['student_name'])
            print("Issue Time   :", v['issue_time'])

    # ================= RETURN BOOK =================

    def return_book(self):

        book_id = input("Enter Book ID To Return: ")

        if book_id not in Library.issued_books:

            print("Book Was Not Issued")
            return

        issue_time = datetime.fromisoformat(
            Library.issued_books[book_id]['issue_time']
        )

        return_time = datetime.now()

        difference = return_time - issue_time

        seconds = difference.total_seconds()

        deposit = Library.issued_books[book_id]['deposit']

        fine = 0

        if seconds > 20:

            fine = 50

        refund = deposit - fine

        Library.total_fine += fine

        Library.books[book_id][2] = "yes"

        del Library.issued_books[book_id]

        self.save_data()

        print("\n========== RETURN DETAILS ==========")

        print("Fine Amount      :", fine)
        print("Refund Amount    :", refund)
        print("Book Returned Successfully")

    # ================= LIBRARY REVENUE =================

    def revenue(self):

        print("\n========== LIBRARY REVENUE ==========")

        print("Total Fine Collected :", Library.total_fine)

    # ================= MAIN FUNCTION =================

    def main(self):

        self.load_data()

        while True:

            print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")

            print("1. View Books")
            print("2. Add Book")
            print("3. Delete Book")
            print("4. Search Book")
            print("5. Register Student")
            print("6. Issue Book")
            print("7. Return Book")
            print("8. View Issued Books")
            print("9. Library Revenue")
            print("10. Exit")

            try:

                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    self.view_books()

                elif choice == 2:
                    self.add_book()

                elif choice == 3:
                    self.delete_book()

                elif choice == 4:
                    self.search_book()

                elif choice == 5:
                    self.register_student()

                elif choice == 6:
                    self.issue_book()

                elif choice == 7:
                    self.return_book()

                elif choice == 8:
                    self.view_issued_books()

                elif choice == 9:
                    self.revenue()

                elif choice == 10:

                    print("Thank You")
                    break

                else:

                    print("Invalid Choice")

            except ValueError:

                print("Enter Numbers Only")


# ================= DRIVER CODE =================

if __name__ == "__main__":

    obj = Library()

    obj.main()
