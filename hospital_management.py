# ================= HOSPITAL MANAGEMENT SYSTEM =================
# Features Added:
# 1. Add Doctor
# 2. View Doctors
# 3. Register Patient
# 4. Book Appointment
# 5. Cancel Appointment
# 6. View Patients
# 7. Search Doctor By Specialization
# 8. Doctor Availability
# 9. Billing System
# 10. Appointment History
# 11. JSON File Storage
# 12. Exception Handling
# ===============================================================

import json
from datetime import datetime


class Hospital:

    def __init__(self):

        self.doctors = {}
        self.patients = {}
        self.appointments = {}
        self.appointment_id = 1

    # ================= LOAD DATA =================

    def load_data(self):

        try:

            with open("doctors.json", "r") as f:

                self.doctors = json.load(f)

        except:

            self.doctors = {

                "D101": {
                    "d_name": "Rohit",
                    "d_spec": "cardio",
                    "d_isbusy": False
                },

                "D102": {
                    "d_name": "Surya",
                    "d_spec": "ent",
                    "d_isbusy": False
                },

                "D103": {
                    "d_name": "Virat",
                    "d_spec": "neuro",
                    "d_isbusy": True
                }
            }

        try:

            with open("patients.json", "r") as f:

                self.patients = json.load(f)

        except:

            self.patients = {}

        try:

            with open("appointments.json", "r") as f:

                self.appointments = json.load(f)

        except:

            self.appointments = {}

    # ================= SAVE DATA =================

    def save_data(self):

        with open("doctors.json", "w") as f:
            json.dump(self.doctors, f, indent=4)

        with open("patients.json", "w") as f:
            json.dump(self.patients, f, indent=4)

        with open("appointments.json", "w") as f:
            json.dump(self.appointments, f, indent=4)

    # ================= ADD DOCTOR =================

    def add_doctor(self):

        print("\n========== ADD DOCTOR ==========")

        d_id = input("Enter Doctor ID: ")

        if d_id in self.doctors:

            print("Doctor ID Already Exists")
            return

        d_name = input("Enter Doctor Name: ")

        d_spec = input(
            "Enter Specialization (ENT/Cardio/Neuro/Derma): ").lower()

        self.doctors[d_id] = {
            "d_name": d_name,
            "d_spec": d_spec,
            "d_isbusy": False
        }

        self.save_data()

        print(f"Dr.{d_name} Added Successfully")

    # ================= VIEW DOCTORS =================

    def view_doctors(self):

        if not self.doctors:

            print("No Doctors Available")
            return

        print("\n========== DOCTOR DETAILS ==========")

        print("DoctorID\tName\t\tSpecialization\tStatus")

        for k, v in self.doctors.items():

            status = "Busy" if v['d_isbusy'] else "Available"

            print(
                f"{k}\t\t{v['d_name']}\t\t{v['d_spec']}\t\t{status}"
            )

    # ================= REGISTER PATIENT =================

    def register_patient(self):

        try:

            print("\n========== REGISTER PATIENT ==========")

            p_adhaar = input("Enter Patient Aadhaar: ")

            p_name = input("Enter Patient Name: ")

            p_age = int(input("Enter Patient Age: "))

            p_issue = input(
                "Enter Problem (ENT/Cardio/Neuro/Derma): ").lower()

            self.patients[p_adhaar] = {
                "p_name": p_name,
                "p_age": p_age,
                "p_issue": p_issue
            }

            self.save_data()

            print(f"Patient {p_name} Registered Successfully")

        except ValueError:

            print("Invalid Input")

    # ================= VIEW PATIENTS =================

    def view_patients(self):

        if not self.patients:

            print("No Patients Registered")
            return

        print("\n========== PATIENT DETAILS ==========")

        print("Aadhaar\t\tName\t\tAge\tIssue")

        for k, v in self.patients.items():

            print(
                f"{k}\t{v['p_name']}\t\t{v['p_age']}\t{v['p_issue']}"
            )

    # ================= SEARCH DOCTOR =================

    def search_doctor(self):

        spec = input("Enter Specialization To Search: ").lower()

        found = False

        print("\n========== SEARCH RESULT ==========")

        for k, v in self.doctors.items():

            if v['d_spec'] == spec:

                found = True

                status = "Busy" if v['d_isbusy'] else "Available"

                print(
                    f"Doctor ID:{k}  Name:{v['d_name']}  Status:{status}"
                )

        if not found:

            print("No Doctor Found")

    # ================= BOOK APPOINTMENT =================

    def book_appointment(self):

        p_adhaar = input("Enter Patient Aadhaar: ")

        if p_adhaar not in self.patients:

            print("Patient Not Registered")
            return

        p_issue = self.patients[p_adhaar]['p_issue']

        for k, v in self.doctors.items():

            if v['d_spec'] == p_issue and not v['d_isbusy']:

                appointment_no = f"A{self.appointment_id}"

                self.appointments[appointment_no] = {

                    "patient_name":
                    self.patients[p_adhaar]['p_name'],

                    "doctor_name":
                    v['d_name'],

                    "specialization":
                    v['d_spec'],

                    "date":
                    str(datetime.now())
                }

                v['d_isbusy'] = True

                self.appointment_id += 1

                self.save_data()

                print("\n========== APPOINTMENT BOOKED ==========")

                print("Appointment ID :", appointment_no)
                print("Doctor Name    :", v['d_name'])
                print("Specialization :", v['d_spec'])

                return

        print("No Available Doctors For This Issue")

    # ================= VIEW APPOINTMENTS =================

    def view_appointments(self):

        if not self.appointments:

            print("No Appointments Found")
            return

        print("\n========== APPOINTMENT DETAILS ==========")

        for k, v in self.appointments.items():

            print("\n----------------------------------")

            print("Appointment ID :", k)
            print("Patient Name   :", v['patient_name'])
            print("Doctor Name    :", v['doctor_name'])
            print("Department     :", v['specialization'])
            print("Date & Time    :", v['date'])

    # ================= CANCEL APPOINTMENT =================

    def cancel_appointment(self):

        a_id = input("Enter Appointment ID To Cancel: ")

        if a_id not in self.appointments:

            print("Appointment Not Found")
            return

        doctor_name = self.appointments[a_id]['doctor_name']

        for v in self.doctors.values():

            if v['d_name'] == doctor_name:

                v['d_isbusy'] = False

        del self.appointments[a_id]

        self.save_data()

        print("Appointment Cancelled Successfully")

    # ================= BILLING SYSTEM =================

    def billing_system(self):

        try:

            print("\n========== BILLING SYSTEM ==========")

            patient = input("Enter Patient Name: ")

            consultation_fee = int(input("Enter Consultation Fee: "))

            medicine_fee = int(input("Enter Medicine Fee: "))

            total = consultation_fee + medicine_fee

            print("\n========== BILL RECEIPT ==========")

            print("Patient Name      :", patient)
            print("Consultation Fee  :", consultation_fee)
            print("Medicine Fee      :", medicine_fee)
            print("Total Bill        :", total)

        except ValueError:

            print("Invalid Input")

    # ================= MAIN FUNCTION =================

    def main(self):

        self.load_data()

        while True:

            print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")

            print("1. Add Doctor")
            print("2. View Doctors")
            print("3. Register Patient")
            print("4. View Patients")
            print("5. Search Doctor")
            print("6. Book Appointment")
            print("7. View Appointments")
            print("8. Cancel Appointment")
            print("9. Billing System")
            print("10. Exit")

            try:

                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    self.add_doctor()

                elif choice == 2:
                    self.view_doctors()

                elif choice == 3:
                    self.register_patient()

                elif choice == 4:
                    self.view_patients()

                elif choice == 5:
                    self.search_doctor()

                elif choice == 6:
                    self.book_appointment()

                elif choice == 7:
                    self.view_appointments()

                elif choice == 8:
                    self.cancel_appointment()

                elif choice == 9:
                    self.billing_system()

                elif choice == 10:

                    print("Thank You")
                    break

                else:

                    print("Invalid Choice")

            except ValueError:

                print("Enter Numbers Only")


# ================= DRIVER CODE =================

if __name__ == "__main__":

    obj = Hospital()

    obj.main()
