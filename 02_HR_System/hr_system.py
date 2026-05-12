class Employee:

    raise_amt = 1.04
    nums_of_emps=0
    emp_id=1000

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f"{first.lower()}.{last.lower()}@gmail.com"

        Employee.nums_of_emps+=1

        Employee.emp_id += 1
        self.emp_id=Employee.emp_id


    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay,prog_lang="Python"):
        super().__init__(first, last, pay)
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def calculate_team_payroll(self):
        return sum(emp.pay for emp in self.employees)

hr_db = dict()

while True:
    print("\n" + "=" * 35)
    print("Welcome to MAATY HR_System")
    print("1. Add New Employee")
    print("2. Move a Developer/Employee to Team_Admin")
    print("3. Display All Team_members")
    print("4. Calc Team_Payroll")
    print("5. Apply Raise")
    print("6. Exit")
    print("=" * 35)

    op = int(input("Enter The Operation U want (1-6): "))

    match op:
        case 1:
            print("\n1) Admin \n2) Employee \n3) Developer")
            em_cr = int(input("What's The role of the Employee (1-3)? "))

            first = input("First Name: ")
            last = input("Last Name: ")
            pay = int(input("Salary: "))

            match em_cr:
                case 1:
                    new_emp = Manager(first, last, pay)
                    hr_db[new_emp.emp_id] = new_emp
                    print(f"Admin added successfully! ID: {new_emp.emp_id}")

                case 2:
                    new_emp = Employee(first, last, pay)
                    hr_db[new_emp.emp_id] = new_emp
                    print(f"Employee added successfully! ID: {new_emp.emp_id}")

                case 3:
                    lang = input("Programming Language: ")
                    new_emp = Developer(first, last, pay, lang)
                    hr_db[new_emp.emp_id] = new_emp
                    print(f"Developer added successfully! ID: {new_emp.emp_id}")

                case _:
                    print("Invalid Role!")

        case 2:
            mgr_id = int(input("Enter Admin ID: "))
            emp_id = int(input("Enter Employee/Developer ID: "))

            if mgr_id in hr_db and emp_id in hr_db:
                if isinstance(hr_db[mgr_id], Manager):
                    hr_db[mgr_id].add_emp(hr_db[emp_id])

                    print(
                        f"Added {hr_db[emp_id].fullname()} to Admin {hr_db[mgr_id].fullname()}'s team."
                    )
                else:
                    print("Error: The first ID is not an Admin!")
            else:
                print("Error: ID not found in database!")

        case 3:
            mgr_id = int(input("Enter Admin ID to display team: "))

            if mgr_id in hr_db and isinstance(hr_db[mgr_id], Manager):
                print(f"\n--- {hr_db[mgr_id].fullname()}'s Team ---")
                hr_db[mgr_id].print_emps()
            else:
                print("Error: Admin not found!")

        case 4:
            mgr_id = int(input("Enter Admin ID to calc payroll: "))

            if mgr_id in hr_db and isinstance(hr_db[mgr_id], Manager):
                total = hr_db[mgr_id].calculate_team_payroll()

                print(f"Total Payroll for this team: {total} EGP")
            else:
                print("Error: Admin not found!")

        case 5:
            emp_id = int(input("Enter Employee ID to apply raise: "))

            if emp_id in hr_db:
                old_pay = hr_db[emp_id].pay
                hr_db[emp_id].apply_raise()

                print(
                    f"Raise applied! {hr_db[emp_id].fullname()}'s salary went from {old_pay} to {hr_db[emp_id].pay}"
                )
            else:
                print("Error: Employee not found!")

        case 6:
            print("Exiting MAATY HR_System. See you later!")
            break

        case _:
            print("Invalid Option!")
