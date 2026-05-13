class Subscriber:
    sub_id=100

    def __init__(self, name:str, email:str, passwd:str, plan:str ="free"):
        self.name=name
        self.plan=plan
        self.email=email
        self.__passwd=passwd

        Subscriber.sub_id+=1
        self.user_id=Subscriber.sub_id


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,new_email:str):
        if "@" in new_email:
            self._email=new_email
        else:
            print("Enter a valid email")


    def res_pass(self,old_pass,new_pass):
        if old_pass==self.__passwd:
            self.__passwd=new_pass
            print("Password Updated Successfully")
        else:
            print("Error: Incorrect Old Password")


    def upgrade(self,new_plan="VIP"):
        self.plan=new_plan
        print(f"Plan Upgraded to {self.plan}")

    def __repr__(self):
        return self.name,self.email,self.plan



saas_db = {}

while True:
    print("\n" + "=" * 35)
    print("Welcome To MAATY SaaS")
    print("1. Add New User")
    print("2. Display Profile_Info")
    print("3. Update Email")
    print("4. Reset Password")
    print("5. Upgrade Plan")
    print("6. Exit")
    print("=" * 35)

    op = int(input("Enter The Operation U Want (1-6): "))

    match op:
        case 1:
            name = input("Enter UR Name: ")
            email = input("Enter a valid Email: ")
            passwd = input("Enter The Password: ")

            new_user = Subscriber(name, email, passwd)

            saas_db[new_user.user_id] = new_user

            print(f"User Added Successfully | ID: {new_user.user_id}")

        case 2:
            user_id = int(input("Enter User_id: "))

            if user_id in saas_db:
                user = saas_db[user_id]

                print(
                    f"\nProfile Info:\n"
                    f"Name: {user.name}\n"
                    f"Email: {user.email}\n"
                    f"Plan: {user.plan}"
                )

            else:
                print("User not found!")

        case 3:
            user_id = int(input("Enter User_id: "))

            if user_id in saas_db:
                new_e = input("Enter The new Valid Email: ")

                saas_db[user_id].email = new_e

                print(f"Current Email is: {saas_db[user_id].email}")

            else:
                print("User not found!")

        case 4:
            user_id = int(input("Enter User_id: "))

            if user_id in saas_db:
                old_p = input("Enter Old Password: ")
                new_p = input("Enter New Password: ")

                saas_db[user_id].res_pass(old_p, new_p)

            else:
                print("User not found!")

        case 5:
            user_id = int(input("Enter User_id: "))

            if user_id in saas_db:
                new_plan = input("Enter New Plan (e.g., Pro, Ultra): ")

                saas_db[user_id].upgrade(new_plan)

            else:
                print("User not found!")

        case 6:
            print("Exiting MAATY SaaS. See you later!")
            break

        case _:
            print("Invalid Option! Choose 1-6.")
