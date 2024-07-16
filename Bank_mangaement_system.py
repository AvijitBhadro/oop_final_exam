
class Bank:
    def __init__(self):
        self.__total_balance = 50000000
        self.total_loan_amount = 0
        self.loan_availability = True
    

    def create_account(self,id, name,email, initial_deposit = 0, is_admin=False):
            if is_admin:
                new_user = Admin(id, name,email)
            else:
                new_user = User(id, name,email, initial_deposit)
                self.__total_balance += initial_deposit

            print(f"Account created for {name}.")
            return new_user
            
    

    def get_total_balance(self):
        return self.__total_balance
  
    def add_balance(self,amount):
        self.__total_balance += amount

    
    def reduce_balance(self,amount):
        self.__total_balance -= amount
 


class User:
    def __init__(self, id, name,email, initial_deposit):
        self.id = id
        self.name = name
        self.email = email
        self.balance = initial_deposit
        self.all_transactions = []
        self.loan_taken = 0

    def deposit(self, amount,bank):
        if amount > 0:
            self.balance += amount
            bank.add_balance(amount)
            self.all_transactions.append(f"Deposited: {amount}")
            print(f"{amount} deposited. Your new balance is {self.balance}.")

    def withdraw(self, amount, bank):
        if self.balance >= amount:
            if bank.get_total_balance() >= amount:
                self.balance -= amount
                bank.reduce_balance(amount)
                self.all_transactions.append(f"Withdrawn: {amount}")
                print(f"{amount} withdrawn. Your new balance is {self.balance}.")
            else:
                print("The bank is bankrupt. Withdrawl is not possible.")
        else:
            print("You do not have sufficient balance! cannot withdraw.")

    def check_balance(self):
        print(f"Available balance: {self.balance}")
        

    def transfer(self, amount, other):
        if self.balance >= amount:
            
            self.balance -= amount
            other.balance += amount
            self.all_transactions.append(f"Transferred: {amount} to {other.id}")
            other.all_transactions.append(f"Received: {amount} from {self.id}")
            print(f"{amount} transferred to {other.name}. New balance is {self.balance}.")
            
                
        else:
            print("You do not have sufficient balance. Transfer is not possible.")

    def check_transaction_history(self):
        for transaction in self.all_transactions:
            print(transaction)

    def take_loan(self,amount, bank):
        if bank.loan_availability:
            loan_amount = amount
            if loan_amount <= (self.balance * 2):
                self.balance += loan_amount
                self.loan_taken += loan_amount
                bank.total_loan_amount += loan_amount
                bank.reduce_balance(loan_amount) 
                self.all_transactions.append(f"Loan taken: {loan_amount}")
                print(f"Loan of {loan_amount} taken. New balance is {self.balance}.")
            else:
                print('You cannot take loan. It crossed the upper bound.')
        else:
            print("Sorry! You cannot take the loan.Loan feature is currently disabled.")




class Admin():
    def __init__(self,id, name,email):
        self.id = id
        self.name = name
        self.email = email

    def check_total_balance(self, bank):
        
        print(f"Total available balance in the bank: {bank.get_total_balance()}")


    def check_total_loan_amount(self, bank):
    
        print(f"Total loan amount: {bank.total_loan_amount}") 


    def loan_feature_facility(self, bank, status):
        bank.loan_availability = status






bank = Bank()


 

admin = bank.create_account('admin1', 'Admin1','admin1@email.com', is_admin = True)
admin.check_total_balance(bank)
admin.check_total_loan_amount(bank)


print('\n')

karim = bank.create_account('1', 'karim','karimalhasan@gmail.com', 1500)
bilgates = bank.create_account('2', 'Bil Gates','Bil123@yahoo.com', 30000)

karim.deposit(500,bank)
karim.check_balance()
karim.withdraw(200, bank)
karim.check_balance()
admin.check_total_balance(bank)

bilgates.transfer(300, karim)
karim.check_transaction_history()

admin.loan_feature_facility(bank, False)
karim.take_loan(2000,bank)


admin.loan_feature_facility(bank, True)
bilgates.take_loan(80000,bank)

karim.take_loan(2500,bank)

admin.check_total_balance(bank)
admin.check_total_loan_amount(bank)
