class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에서 ", amount, "가 출금되었음")
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(" 통장에 ", amount, "가 입급되었음")
        return self.__balance

myAccount = BankAccount()
balance = myAccount.deposit(100)
print('잔액은', str(balance), '입니다')
balance = myAccount.withdraw(10)
print('잔액은', str(balance), '입니다')
