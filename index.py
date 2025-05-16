class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"+{amount} сом добавлено на счет.")
        else:
            print("Ошибка: сумма должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"-{amount} сом снято с баланса.")
        else:
            print("Ошибка: недостаточно средств.")

    def check_balance(self):
        print(f"Баланс {self.owner}: {self.__balance} сом")

w = Wallet("Сайкал")
w.deposit(1000)
w.withdraw(300)
w.check_balance()
