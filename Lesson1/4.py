numb = int(input("Введите целое положительное число: "))
max = -1
while numb > 10:
    d = numb % 10
    numb = numb // 10
    if d > max:
        max = d
print("Максимальая цифра в вашем числе: ", max)
