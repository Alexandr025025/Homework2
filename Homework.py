# x = int(input("Введите целое число x: "))
# y = int(input("Введите целое число y: "))
# result = x ** y
# print(f"{x} в степени {y} равно {result}")



# count = 0
# for number in range(100, 1000):
#     digits = str(number)
#     if digits[0] == digits[1] or digits[0] == digits[2] or digits[1] == digits[2]:
#         count += 1
# print(f"Количество целых чисел от 100 до 999 с двумя одинаковыми цифрами: {count}")




# count = 0
# for number in range(100, 10000):
#     digits = str(number)
#     if len(digits) == len(set(digits)): 
#         count += 1
# print(f"Количество целых чисел от 100 до 9999, у которых все цифры разные: {count}")



number = input("Введите любое целое число: ")
result = number.replace('3', '').replace('6', '')
print(f"Результат после удаления цифр 3 и 6: {result}")