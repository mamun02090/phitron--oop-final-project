from Bank import Bank
class Person:
    def __init__(self, name, email, password, address, nid) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.nid = nid
        self.address = address
    

class User(Person):
    def __init__(self, name, email, password,address, nid,  amount) -> None:
        super().__init__(name, email, password,address, nid)
        self.__balance = amount
        self.id = None
        self.__loan = 0
        self.transaction_history = []
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        self.__balance += value
    @balance.setter
    def withdraw(self, amount):
        self.__balance -= amount
    @property
    def loan(self):
        return self.__loan
    @loan.setter
    def loan(self, value):
        self.__loan += value
    
    def show_transaction_history(self):
        print("--------------- Transaction History------------------------")
        if(self.id != None):
            for transaction in self.transaction_history:
                print(f"{transaction.type} {transaction.amount} {transaction.time}")
        else:
            print("You are not a user of this bank.")

class Admin(Person):
    def __init__(self, name, email, password, address, nid) -> None:
        super().__init__(name, email, password, address, nid)
        self.role = 'Admin'
    
    
    
    
