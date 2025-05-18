class Calculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    try:
        a = float(input("Введите первое положительное число: "))
        b = float(input("Введите второе положительное число: "))

        if a < 0 or b < 0:
            print("Ошибка: введите только положительные числа.")
        else:
            print("Сложение:", calc.add(a, b))
            print("Вычитание:", calc.substract(a, b))
            print("Умножение:", calc.multiply(a, b))
            print("Деление:", calc.divide(a, b))

    except ValueError as e:
        print(f"Ошибка: {e}")

