class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
        return self.num1 + self.num2

    def __sub__(self):
        return self.num1 - self.num2

    def __mul__(self):
        return self.num1 * self.num2

    def __truediv__(self):
        return self.num1 / self.num2

num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))
action = input("введите дейсвтие: ")
calc = calculator(num1, num2)
if action == "+":
    print(calc.__add__())
elif action == "-":
    print(calc.__sub__())
elif action == "*":
    print(calc.__mul__())
elif action == "/":
    print(calc.__truediv__())