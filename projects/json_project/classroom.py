import json
import os

DATA_FILE = "students.json"

class Student:
    def __init__(self, regno, name, age, gender, class_name, parent_name, phone_number):
        self.regno = regno
        self.name = name
        self.age = age
        self.gender = gender
        self.class_name = class_name
        self.parent_name = parent_name
        self.phone_number = phone_number

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "class_name": self.class_name,
            "parent_name": self.parent_name,
            "phone_number": self.phone_number
        }

    def __str__(self):
        return (
            f"Reg No: {self.regno}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Class: {self.class_name}\n"
            f"Parent: {self.parent_name}\n"
            f"Phone: {self.phone_number}\n"
        )


class School:
    def __init__(self):
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                fixed_data = {}
                for reg, info in data.items():
                    # ✅ backward compatibility: rename "class" → "class_name"
                    if "class" in info:
                        info["class_name"] = info.pop("class")

                    # ✅ pass reg separately
                    fixed_data[reg] = Student(
                        reg,
                        info["name"],
                        info["age"],
                        info["gender"],
                        info["class_name"],
                        info["parent_name"],
                        info["phone_number"]
                    )
                return fixed_data
        return {}

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump({reg: s.to_dict() for reg, s in self.students.items()}, file, indent=4)

    def add_student(self):
        regno = input("Enter Registration Number: ").strip()

        if regno in self.students:
            print(f" Student with Registration No {regno} already exists!")
            return

        student = Student(
            regno,
            input("Enter Student Name: ").strip(),
            input("Enter Age: ").strip(),
            input("Enter Gender (M/F): ").strip(),
            input("Enter Class: ").strip(),
            input("Enter Parent Name: ").strip(),
            input("Enter Phone Number: ").strip()
        )

        self.students[regno] = student
        self.save_data()
        print(f" Student {student.name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students registered yet.")
            return
        for student in self.students.values():
            print(student)
            print("-" * 30)

    def search_student(self):
        if not self.students:
            print("No students to search.")
            return

        filters = ["name", "class_name", "regno", "parent_name", "phone_number"]
        candidates = list(self.students.values())

        for f in filters:
            value = input(f"Enter {f} to search (or press Enter to skip): ").strip()
            if not value:
                continue

            candidates = [s for s in candidates if getattr(s, f) == value]

            if len(candidates) == 1:
                print("\n Student found:\n")
                print(candidates[0])
                return
            elif len(candidates) > 1:
                print(f"Multiple students found with {f} = {value}, refining search...")
            else:
                print(f"No students found with {f} = {value}. Try another field.")
                return

        if candidates:
            print("Multiple matches remain, please refine search again.")
        else:
            print("No student found.")


def main():
    school = School()

    while True:
        print("\n--- School Management System ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            school.add_student()
        elif choice == "2":
            school.view_students()
        elif choice == "3":
            school.search_student()
        elif choice == "4":
            print("Exiting program... ")
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
