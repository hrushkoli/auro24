class BankAccount:
    def __init__(self,accountNumber,accountName,accountBalance):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.accountBalance = accountBalance
    
    def displayAccountDetails(self):
        print("Account Number: ",self.accountNumber,"|| Account Name: ",self.accountName)

    def fetchBalance(self):
        print("Balance for Account# ",accountNumber," is:",self.accountBalance)

    def withdrawal(self,amount):
        self.accountBalance -= amount
        print("Balance for Account# ",accountNumber," After Withdrawal:",self.accountBalance)

    def deposit(self,amount):
        self.accountBalance += amount
        print("Balance for Account# ",accountNumber," After Deposit:",self.accountBalance)

bank = []

while True:
    print("Welcome to the Banking System: \n")
    menu = int(input("Menu:\n Press 1 for Account List \n Press 2 to Withdraw \n Press 3 to Deposit \n Press 4 to fetch Balance \n Press 5 to Create a New Account\n"))

    if(menu == 1) :
        if (len(bank)==0):
            print("No Accounts")
        else:
            for account in bank:
                account.displayAccountDetails()
    if(menu == 2) :
        accountNumber = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount to Withdraw: "))
        bank[accountNumber].withdrawal(amount)

    if(menu == 3) :
        accountNumber = int(input("Enter Account Number: "))
        amount = int(input("Enter Amount to Deposit: "))
        bank[accountNumber].deposit(amount)
    if(menu == 4) :
        accountNumber = int(input("Enter Account Number: "))
        bank[accountNumber].fetchBalance()
    if(menu == 5):
        accountName = input("Enter Account Holder's Name: ")
        balance = int(input("Enter Balance: "))
        newAccount = BankAccount(int(len(bank)),accountName,balance)
        bank.append(newAccount)
