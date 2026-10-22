# ================= HOTEL MANAGEMENT SYSTEM =================
# Features Added:
# 1. View Available Rooms
# 2. Book Room
# 3. Customer Details
# 4. Food Ordering System
# 5. Checkout & Billing
# 6. Cancel Room Booking
# 7. Search Room
# 8. Room Service Charges
# 9. JSON File Storage
# 10. Exception Handling
# 11. Booking History
# 12. Total Hotel Revenue
# ===========================================================

from datetime import datetime
import json


class Hotel:

    rooms = {}
    customers = {}
    bookings = {}
    food = {
        1: ['Chicken Biryani', 250],
        2: ['Veg Biryani', 200],
        3: ['Water Bottle', 20],
        4: ['Cool Drink', 40],
        5: ['Ice Cream', 100]
    }

    total_revenue = 0

    # ================= LOAD DATA =================

    def load_data(self):

        try:

            with open("rooms.json", "r") as f:

                Hotel.rooms = json.load(f)

        except:

            Hotel.rooms = {
                "101": ['River View', 2000, 4, 'No'],
                "102": ['Ground Floor', 1800, 3, 'No'],
                "103": ['Deluxe AC', 3000, 2, 'No'],
                "104": ['Suite Room', 5000, 5, 'No']
            }

        try:

            with open("customers.json", "r") as f:

                Hotel.customers = json.load(f)

        except:

            Hotel.customers = {}

        try:

            with open("bookings.json", "r") as f:

                Hotel.bookings = json.load(f)

        except:

            Hotel.bookings = {}

    # ================= SAVE DATA =================

    def save_data(self):

        with open("rooms.json", "w") as f:
            json.dump(Hotel.rooms, f, indent=4)

        with open("customers.json", "w") as f:
            json.dump(Hotel.customers, f, indent=4)

        with open("bookings.json", "w") as f:
            json.dump(Hotel.bookings, f, indent=4)

    # ================= VIEW ROOMS =================

    def available_rooms(self):

        print("\n========== AVAILABLE ROOMS ==========")

        print("Room\tType\t\tPrice\tBeds\tBooked")

        for k, v in Hotel.rooms.items():

            print(f"{k}\t{v[0]}\t{v[1]}\t{v[2]}\t{v[3]}")

    # ================= SEARCH ROOM =================

    def search_room(self):

        room_type = input("Enter Room Type: ").lower()

        found = False

        print("\n========== SEARCH RESULT ==========")

        for k, v in Hotel.rooms.items():

            if room_type in v[0].lower():

                found = True

                print(
                    f"Room:{k}  Type:{v[0]}  Price:{v[1]}  Beds:{v[2]}"
                )

        if not found:

            print("No Matching Rooms Found")

    # ================= BOOK ROOM =================

    def book_room(self):

        room_no = input("Enter Room Number: ")

        if room_no not in Hotel.rooms:

            print("Invalid Room Number")
            return

        room = Hotel.rooms[room_no]

        if room[3] == "Yes":

            print("Room Already Booked")
            return

        try:

            name = input("Enter Customer Name: ")

            phone = input("Enter Phone Number: ")

            days = int(input("Enter Number Of Days: "))

            if days <= 0:

                print("Days Must Be Greater Than Zero")
                return

            amount = room[1] * days

            Hotel.customers[room_no] = {
                "name": name,
                "phone": phone,
                "days": days,
                "room_amount": amount,
                "food_amount": 0
            }

            room[3] = "Yes"

            Hotel.bookings[room_no] = {
                "customer": name,
                "date": str(datetime.now())
            }

            self.save_data()

            print("\n========== ROOM BOOKED ==========")

            print("Customer Name :", name)
            print("Room Number   :", room_no)
            print("Total Amount  :", amount)

        except ValueError:

            print("Invalid Input")

    # ================= VIEW CUSTOMERS =================

    def view_customers(self):

        if not Hotel.customers:

            print("No Customers Found")
            return

        print("\n========== CUSTOMER DETAILS ==========")

        for k, v in Hotel.customers.items():

            print("\nRoom Number :", k)
            print("Customer    :", v['name'])
            print("Phone       :", v['phone'])
            print("Days Stay   :", v['days'])

    # ================= FOOD ORDER =================

    def food_items(self):

        room_no = input("Enter Room Number: ")

        if room_no not in Hotel.rooms:

            print("Invalid Room Number")
            return

        if Hotel.rooms[room_no][3] == "No":

            print("Room Not Booked")
            return

        print("\n========== FOOD MENU ==========")

        print("ItemNo\tFood Item\t\tPrice")

        for k, v in Hotel.food.items():

            print(f"{k}\t{v[0]}\t\t{v[1]}")

        total_food_bill = 0

        while True:

            try:

                order = int(
                    input("Enter Item Number (999 To Stop): "))

                if order == 999:
                    break

                if order not in Hotel.food:

                    print("Invalid Food Item")
                    continue

                quantity = int(input("Enter Quantity: "))

                total = Hotel.food[order][1] * quantity

                total_food_bill += total

                print(
                    f"{Hotel.food[order][0]} Ordered Successfully"
                )

            except ValueError:

                print("Invalid Input")

        Hotel.customers[room_no]['food_amount'] += total_food_bill

        self.save_data()

        print("Food Order Completed")
        print("Food Bill :", total_food_bill)

    # ================= CHECKOUT =================

    def checkout(self):

        room_no = input("Enter Room Number For Checkout: ")

        if room_no not in Hotel.customers:

            print("No Booking Found")
            return

        customer = Hotel.customers[room_no]

        room_bill = customer['room_amount']

        food_bill = customer['food_amount']

        service_charge = 500

        total_bill = room_bill + food_bill + service_charge

        Hotel.total_revenue += total_bill

        print("\n========== FINAL BILL ==========")

        print("Date :", datetime.now())
        print("Customer Name :", customer['name'])
        print("Room Bill     :", room_bill)
        print("Food Bill     :", food_bill)
        print("Service Charge:", service_charge)
        print("Total Bill    :", total_bill)

        Hotel.rooms[room_no][3] = "No"

        del Hotel.customers[room_no]

        self.save_data()

        print("Checkout Completed Successfully")

    # ================= CANCEL BOOKING =================

    def cancel_booking(self):

        room_no = input("Enter Room Number To Cancel: ")

        if room_no not in Hotel.customers:

            print("No Booking Found")
            return

        Hotel.rooms[room_no][3] = "No"

        del Hotel.customers[room_no]

        self.save_data()

        print("Room Booking Cancelled Successfully")

    # ================= BOOKING HISTORY =================

    def booking_history(self):

        if not Hotel.bookings:

            print("No Booking History Found")
            return

        print("\n========== BOOKING HISTORY ==========")

        for k, v in Hotel.bookings.items():

            print("\nRoom Number :", k)
            print("Customer    :", v['customer'])
            print("Booked Date :", v['date'])

    # ================= HOTEL REVENUE =================

    def hotel_revenue(self):

        print("\n========== HOTEL REVENUE ==========")

        print("Total Revenue :", Hotel.total_revenue)

    # ================= MAIN FUNCTION =================

    def main(self):

        self.load_data()

        while True:

            print("\n========== HOTEL MANAGEMENT SYSTEM ==========")

            print("1. View Available Rooms")
            print("2. Search Room")
            print("3. Book Room")
            print("4. View Customers")
            print("5. Food Ordering")
            print("6. Checkout")
            print("7. Cancel Booking")
            print("8. Booking History")
            print("9. Hotel Revenue")
            print("10. Exit")

            try:

                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    self.available_rooms()

                elif choice == 2:
                    self.search_room()

                elif choice == 3:
                    self.book_room()

                elif choice == 4:
                    self.view_customers()

                elif choice == 5:
                    self.food_items()

                elif choice == 6:
                    self.checkout()

                elif choice == 7:
                    self.cancel_booking()

                elif choice == 8:
                    self.booking_history()

                elif choice == 9:
                    self.hotel_revenue()

                elif choice == 10:

                    print("Thank You")
                    break

                else:

                    print("Invalid Choice")

            except ValueError:

                print("Enter Numbers Only")


# ================= DRIVER CODE =================

if __name__ == "__main__":

    obj = Hotel()

    obj.main()
