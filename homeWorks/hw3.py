
class Bakai_Bank:

    def __init__(self, name, balance):
            self._name = name
            self._balance = balance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def moneyX(self, money):
        self.balance += money
        return self.balance

    def _kill(self):
        self.balance = 0
        return self.balance

    @property
    def kill(self):
        return self._kill()

    def __jackpot(self):
        self.balance = self.balance * 10
        return self.balance

    @property
    def jackpot(self):
        return self.__jackpot()

    def __Freeloader(self, name):
        self.balance *= name.balance
        return self.balance

    @property
    def Freeloader(self):
        return self.__Freeloader

    def __str__(self):
        return (f'имя: {self._name}\n'
                f'деньги: {self._balance}')

x = int(input('введите число: '))
bank = Bakai_Bank('марсель',0)
print(bank.moneyX(x))
bank2 = Bakai_Bank('бакай',2)
print(bank.Freeloader(bank2))