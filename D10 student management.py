import csv
import os


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, roll_no, name, age, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def add_student(self):

        file_exists = os.path.exists("students.csv")

        with open("students.csv", "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Roll No", "Name", "Age", "Marks"])

            writer.writerow(
                [self.roll_no, self.name, self.age, self.marks]
            )

        print("Student Added Successfully")

    def display_students(self):

        try:

            with open("students.csv", "r") as file:

                reader = csv.reader(file)

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("No student record found.")

    def search_student(self, roll):

        found = False

        with open("students.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                if row[0] == roll:

                    print("\nStudent Found\n")

                    print("Roll No :", row[0])
                    print("Name    :", row[1])
                    print("Age     :", row[2])
                    print("Marks   :", row[3])

                    found = True
                    break

        if not found:
            print("Student Not Found")

    def update_student(self, roll):

        rows = []

        updated = False

        with open("students.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0] == roll:

                    print("Enter New Data")

                    name = input("New Name : ")
                    age = input("New Age : ")
                    marks = input("New Marks : ")

                    row = [roll, name, age, marks]

                    updated = True

                rows.append(row)

        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        if updated:
            print("Record Updated")
        else:
            print("Student Not Found")

    def delete_student(self, roll):

        rows = []

        deleted = False

        with open("students.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0] == roll:
                    deleted = True
                    continue

                rows.append(row)

        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        if deleted:
            print("Student Deleted")
        else:
            print("Student Not Found")


def main():

    while True:

        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":

            roll = input("Roll No : ")
            name = input("Name : ")
            age = input("Age : ")
            marks = input("Marks : ")

            s = Student(roll, name, age, marks)

            s.add_student()

        elif choice == "2":

            s = Student("", "", "", "")

            s.display_students()

        elif choice == "3":

            roll = input("Enter Roll Number : ")

            s = Student("", "", "", "")

            s.search_student(roll)

        elif choice == "4":

            roll = input("Enter Roll Number : ")

            s = Student("", "", "", "")

            s.update_student(roll)

        elif choice == "5":

            roll = input("Enter Roll Number : ")

            s = Student("", "", "", "")

            s.delete_student(roll)

        elif choice == "6":

            print("Program Closed")

            break

        else:

            print("Invalid Choice")


main()