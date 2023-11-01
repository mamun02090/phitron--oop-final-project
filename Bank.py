from datetime import datetime
class Bank:
    def __init__(self, name, address, amount) -> None:
        self.name = name
        self.address = address
        self.__balance = amount
        self.users = []
        self.admins = []
        self.__loan = 0
        self.transactions = {}
        self.inActiveFeatures = []
    
    def balance(self, email, password):
        for admin in self.admins:
            if email == admin.email and password == admin.password:
                return self.__balance
        print("You are not allowed")
    def total_loan(self, email, password):
        for admin in self.admins:
            if email == admin.email and password == admin.password:
                return self.__loan
        print("You are not allowed")        
    def control_feature(self, email, password, feature, action):
        for admin in self.admins:
            if email == admin.email and password == admin.password:
                if action == 'off':
                    self.inActiveFeatures.append(feature)
                    
                elif action == 'on':
                    self.inActiveFeatures.remove(feature)
            else:      
                print("You are not allowed") 
    def add_user(self, user):
        id = f'02000{len(self.users)+1}'
        user.id = id
        self.users.append(user)
        self.transactions[id] = []
    
    def add_admin(self, admin):
        id = f'admin_{len(self.users)+1}'
        admin.id = id
        self.admins.append(admin)
    
    def deposit(self, email, amount):
        if('deposit' in self.inActiveFeatures):
            print("This feature is currently unavailable")
            return
        for user in self.users:
            if user.email == email:
                self.__balance += amount
                user.balance = amount
                transaction = TransactionHistory('Deposit', amount)
                self.transactions[user.id].append(transaction)
                user.transaction_history.append(transaction)
                print("Deposit successful")
                return
        print("User doesn't exist")
    
    def withdraw(self, email, password, amount):
        if('withdraw' in self.inActiveFeatures):
            print("This feature is currently unavailable")
            return
        if(amount> self.__balance):
            print(f"{self.name} is bankrupt")
        for user in self.users:
            if user.email==email:
                if user.password == password:
                    if(user.balance>=amount):
                        user.withdraw = amount
                        self.__balance = amount
                        transaction = TransactionHistory('withdraw', amount)
                        self.transactions[user.id].append(transaction)
                        user.transaction_history.append(transaction)
                        print(f"{user.name}, Your withdraw request for {amount} has been successful")
                    else:
                        print(f"{user.name}, You don't have enough money")
                else:
                    print("Unauthenticated, Email or password is wrong")
                return
                
        else:
            print("User doesn't exist")
    
    def transfer(self, sender_email, sender_password, receiver_email, amount):
        if('transfer' in self.inActiveFeatures):
            print("This feature is currently unavailable")
            return
        sender = None
        receiver = None
        if(sender_email==receiver_email):
            print("You can't transfer amount to yourself")
        for user in self.users:
            if user.email == receiver_email:
                receiver = user
            if user.email == sender_email:
                sender = user
            if(receiver and sender):
                break
        if receiver==None:
            print("Receiver doesn't exist")
            return
        if(sender != None):
            if sender_password == sender.password:
                if(sender.balance>=amount):
                    sender.withdraw= amount 
                    receiver.balance = amount
                    transaction = TransactionHistory('Transfer', amount)
                    transaction_rec = TransactionHistory('Deposit', amount)
                    self.transactions[sender.id].append(transaction)
                    sender.transaction_history.append(transaction)
                    self.transactions[receiver.id].append(transaction_rec)
                    receiver.transaction_history.append(transaction_rec)
                    print(f"{sender.name}, Your transfer request for {amount} has been successful")
                else:
                    print(f"{sender.name}, You don't have enough money")
        else:
            print("Sender doesn't exist")
    
    def loan_request(self, email, password, amount):
        if('loan' in self.inActiveFeatures):
            print("This feature is currently unavailable")
            return
        for user in self.users:
            if user.email == email:
                if(user.password ==password):
                    if(amount< 2*user.balance):
                        self.__loan += amount
                        user.loan = amount
                        transaction = TransactionHistory('Loan', amount)
                        self.transactions[user.id].append(transaction)
                        user.transaction_history.append(transaction)
                        print(f"You get {amount} loan")
                        return
                    else:
                        print(f"{user.name}, You don't have enough money to get requested loan")
                        return
                else:
                    print("Unauthenticated")
        print("User doesn't exist")
        

class TransactionHistory:
    def __init__(self, type, amount) -> None:
        self.type = type
        self.amount = amount
        self.time = datetime.now()      
    