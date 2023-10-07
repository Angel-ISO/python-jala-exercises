class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class User:
    def __init__(self, user_id, password, account):
        self.user_id = user_id
        self.password = password
        self.account = account


class Cashier:
    def __init__(self):
        self.login_attempts = 0

    def login(self, user, password):
        if self.login_attempts < 3:
            if user.password == password:
                self.login_attempts = 0
                return True
            else:
                self.login_attempts += 1
                return False
        else:
            return "Number of attempts exceeded. Please contact customer service."

    def withdraw(self, user, amount):
        if self.login(user, input("Enter your password: ")):
            result = user.account.withdraw(amount)
            if result:
                return f"Withdrawal successful. Remaining balance: {user.account.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Login error."


account1 = Account("12345", 1000)
user1 = User("angel", "1234", account1)
cashier = Cashier()

while True:
    password = input("Enter your password: ")
    if cashier.login(user1, password):
        break
    else:
        print("Login error. Please try again.")


withdraw_amount = float(input("Enter the amount to withdraw: "))
result = cashier.withdraw(user1, withdraw_amount)
print(result)
