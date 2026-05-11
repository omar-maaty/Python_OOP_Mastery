from datetime import datetime

class BankAccount:
    total_user=0
    total_liq=0
    last_acc_num=1000

    def __init__(self, name:str, balance:int =0):
        self.name=name
        self.balance=balance
        self.hist_acc=[]

        BankAccount.last_acc_num+=1
        self.acc_num = BankAccount.last_acc_num
        BankAccount.total_liq+=self.balance
        BankAccount.total_user+=1


    def deposit(self,mnt:int):
        if self.check_mnt(mnt):
            self.balance+=mnt
            BankAccount.total_liq+=mnt
            x=f"You Deposit {mnt} EGP AT {BankAccount.get_time()} "
            self.hist_acc.append(x)
        else:
            print("You can't Deposit a negative amount")


    def withdraw(self,mnt:int):
        if self.check_mnt(mnt) and self.balance>=mnt:
            self.balance-=mnt
            BankAccount.total_liq-=mnt
            x=f"You Withdraw {mnt} EGP AT {BankAccount.get_time()}"
            self.hist_acc.append(x)
        else:
            print("Your Balance not Enough for this Operation")


    def transfer(self,target_acc,mnt:int):
        if self.check_mnt(mnt) and self.balance>=mnt:
            self.withdraw(mnt)
            target_acc.deposit(mnt)
            self.hist_acc.append(f"You Transfer {mnt} to {target_acc.name}")
            print(f"Transfer Successful At {BankAccount.get_time()}")
        else:
            print("Transfer failed, Please check amount and balance")


    @classmethod
    def from_str(cls,string:str):
        name, balance =string.split("-")
        return cls(name,int(balance))


    @classmethod
    def from_dict(cls,data:dict):
        name =data["n"]
        balance=data["b"]
        return cls(name, int(balance))


    @staticmethod
    def check_mnt(mnt:int):
        return mnt>0

    @staticmethod
    def get_time():
        now = datetime.now()
        formatted_date = now.strftime("%y-%m-%d | %H:%M")
        return formatted_date

    def show_history(self):
        print(f"\n--- Transaction History for {self.name} ---")
        for trans in self.hist_acc:
            print(trans)
        print("-"*40)


accounts_db = {}


def Bank_data():
    print("\n--- Bank Global Data ---")
    print(f"Total User Accounts: {BankAccount.total_user}")
    print(f"Current Bank Liquidity: {BankAccount.total_liq} EGP")
    print("--------------------------\n")


while True:
    print("\n" + "=" * 35)
    print("Welcome to MAATY System Bank")
    print("1. Create New Account (Name-Balance)")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Show Account History")
    print("6. Show Bank Details")
    print("7. Exit")
    print("=" * 35)

    op = int(input("Enter The Operation You Want (1-7): "))

    match op:
        case 1:
            data_str = input("Enter User Data (Format: Name-Balance): ")
            new_acc = BankAccount.from_str(data_str)
            accounts_db[new_acc.acc_num] = new_acc
            print(f"Account created successfully! Your Account Number is: {new_acc.acc_num}")

        case 2:
            acc_id = int(input("Enter your Account Number: "))
            if acc_id in accounts_db:
                amount = int(input("Enter the amount to Deposit: "))
                accounts_db[acc_id].deposit(amount)
                print(f"Current balance: {accounts_db[acc_id].balance}")
            else:
                print("Account not found!")

        case 3:
            acc_id = int(input("Enter your Account Number: "))
            if acc_id in accounts_db:
                amount = int(input("Enter the amount to Withdraw: "))
                accounts_db[acc_id].withdraw(amount)
                print(f"Current balance: {accounts_db[acc_id].balance}")
            else:
                print("Account not found!")

        case 4:
            sender_id = int(input("Enter YOUR Account Number: "))

            if sender_id in accounts_db:
                receiver_id = int(input("Enter RECEIVER Account Number: "))

                if receiver_id in accounts_db:

                    if sender_id != receiver_id:
                        amount = int(input("Enter the amount to Transfer: "))
                        accounts_db[sender_id].transfer(accounts_db[receiver_id], amount)
                    else:
                        print("You cannot transfer money to yourself!")
                else:
                    print("Receiver Account not found!")
            else:
                print("Your Account not found!")

        case 5:
            acc_id = int(input("Enter your Account Number: "))
            if acc_id in accounts_db:
                accounts_db[acc_id].show_history()
                print(f"The current Balance {accounts_db[acc_id].balance} EGP")
            else:
                print("Account not found!")

        case 6:
            Bank_data()

        case 7:
            print("Thank you for using MAATY System Bank. Have a great day!")
            break

        case _:
            print("Invalid Option! Please choose a number from 1 to 7.")
