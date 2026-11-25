answer = input("Обичаш ли Python? (да/не): ")

if answer == "да":
    print("Супер!")
else:
    print("Ще го харесаш!")
//1

number = int(input("Въведи число: "))

if number > 10:
    print("Голямо число")
else:
    print("Малко число")
//2

answer = int(input("Колко е 5 × 5? "))

if answer == 25:
    print("Вярно! Браво!")
else:
    print("Грешно! Опитай отново!")
//3

grade = int(input("Въведи своята оценка (от 2 до 6): "))

if grade == 6:
    print("Отличен резултат!")
elif grade == 5:
    print("Много добър резултат!")
elif grade == 4:
    print("Добър резултат!")
elif grade == 3:
    print("Среден резултат!")
else:
    print("Слаб резултат!")
//4

secret_number = 7
guess = int(input("Въведи число: "))

if guess == secret_number:
    print("Поздравления! Позна!")
elif guess > secret_number:
    print("Опитай с по-малко число!")
else:
    print("Опитай с по-голямо число!")
//5

