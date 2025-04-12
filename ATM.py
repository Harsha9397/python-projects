class account:
    def __init__(self,username,password,balance=0):
        self.username=username
        self.password=password
        self.balance=balance

class bankmanagement():
    def __init__(self):
        self.accounts={}
    
    def createaccount(self):
        username=input("Enter thr user name : ")
        password=input("Enter the password : ")

        if username in self.accounts:
            print("user name is already in use")

        else:
            self.accounts[username]=account(username,password,0)
            print("account created sucessfully")
    
    def login(self):
        username=input("Enter your username : ")
        password=input("Enter your password : ")

        if username in self.accounts:
            ac=self.accounts[username]
            if ac.password == password:
                print(f"your login is successfull! {username}")
                return ac
            else:
                print("incorrect passsword")
        else :
            print("username not found!please try again!!")
            return None
    
    def depo_sit(self,account):
        amount = float(input("Enter the amount to deposit : "))
        if amount > 0:
            account.balance += amount
            print(f"deposit amount is :{amount} and new total balance is : {account.balance}")
        else:
            print("invalid amount")
    def with_drawl(self,account):
        amount = float(input("Enter the withdrawl amount : "))
        if amount < account.balance:
            account.balance -=amount
            print(f"withdrawl amount is : {amount} and remaining balance is :{account.balance} ")
        else:
            ("insufficient balance ")
    def check_balance(self,account):
        print(f"your cutrrent balance is : {account.balance}")

    def mini_statement(self,account):
        print("MINI STATEMENT :")
        print(f"account user name is : {account.username}")
        print(f"account balance is : {account.balance}")

    def exit(self):
        print("Thankyou..!")
        exit()
bank = bankmanagement()
while True:
    print("...Welcome to Jessy bank...")
    print("1.Create account")
    print("2.Login account")
    print("3.Exit")
    choose_option=int(input("Enter the option : "))

    if  choose_option == 1:
        bank.createaccount()
    
    elif choose_option == 2:
        account=bank.login()
        if account:
            while True:
                print("Welcome to the Sweety's ATM")
                print("1.Deposite")
                print("2.Withdrawl")
                print("3.Check Balance")
                print("4.Ministatement")
                print("5.Logout")
                option = int(input("Choose your option : "))
                if option == 1:
                    bank.depo_sit(account)
                elif option == 2:
                    bank.with_drawl(account)
                elif option == 3:
                    bank.check_balance(account)
                elif option == 4:
                    bank.mini_statement(account)
                elif option == 5:
                    print("Logout successfully")
                    break
                else:
                    print("invalid option..!")
    
    elif choose_option ==3:
        bank.exit()
    
    else :
        print("Ivalid option..! ")



