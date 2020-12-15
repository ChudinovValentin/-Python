revenue = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))

if revenue > cost:
    print("Прибыль - выручка больше издержек!")
    profit = revenue - cost
    print("Прибыль составила: ", profit)

    print(f"{profit:02}")

    people = int(input("Введите количество сотрудников в фирме: "))
    profitPeople = profit // people
    print("Прибыль фирмы в расчете на одного сотрудника: ", profitPeople)
elif revenue == cost:
    print("Выручка равна издержкам!")
else:
    print("Убыток - издержки больше выручки!")
