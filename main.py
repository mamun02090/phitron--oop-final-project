from Bank import Bank
from Person import User, Admin

def main():
    my_bank = Bank("my_bank", 'Bank para', 10000)
    sakip = User("Sakib", 'sakib@bcb.com', 'sakib02', 'ekhane', 1242344, 1000)
    my_bank.add_user(sakip)
    my_bank.withdraw('sakib@bcb.com', 'sakib02',500)
    my_bank.deposit('sakib@bcb.com', 5000)
    tamim= User("Sakib", 'tamim@bcb.com', 'sakib02', 'ekhane', 1842344, 1000)
    my_bank.add_user(tamim)
    my_bank.transfer('sakib@bcb.com', 'sakib02', 'tamim@bcb.com', 30)
    my_bank.loan_request('sakib@bcb.com', 'sakib02', 200)
    print(sakip.loan)
    admin = Admin("Jalal", 'admin@bcb.com', 'ami09', 'mirpur', 196431659817)
    my_bank.add_admin(admin)
    my_bank.control_feature('admin@bcb.com', 'ami09', 'loan', 'off')
    my_bank.loan_request('sakib@bcb.com', 'sakib02', 200)
    print(my_bank.balance('admin@bcb.com', 'ami09'))
    sakip.show_transaction_history()


if __name__ == '__main__':
    main()