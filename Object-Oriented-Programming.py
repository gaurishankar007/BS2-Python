class Account:
    bank_name = "Global Bank"  # Static(class) variables

    def __init__(self, ac_no, ac_name, balance):  # instance method
        self.ac_no = ac_no
        self.ac_name = ac_name
        self.balance = balance

    def balance_enquiry(self):  # instance method
        print("Balance: ", self.balance)

    def withdraw(self, amount):  # instance method
        if self.balance < amount:
            print("Insufficient Amount!")
        else:
            self.balance = self.balance - amount

    @classmethod
    def change_name(cls):  # class method
        cls.bank_name = "IME"

    @staticmethod
    def sum(x, y):  # static method
        return x + y


a1 = Account(1001, "shyam", 10000)

# For printing class variable
print(Account.bank_name)

# calling class method
Account.change_name()
print(Account.bank_name)

# calling static method
print(a1.sum(2, 3))