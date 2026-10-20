"""Basit hesap makinesi: toplama, çıkarma, çarpma, bölme."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra bölme hatası")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main():
    try:
        a = float(input("Birinci sayı: "))
        op = input("İşlem (+, -, *, /): ").strip()
        b = float(input("İkinci sayı: "))
    except ValueError:
        print("Geçersiz sayı.")
        return

    if op not in OPERATIONS:
        print("Geçersiz işlem.")
        return

    try:
        print(f"Sonuç: {OPERATIONS[op](a, b)}")
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()
