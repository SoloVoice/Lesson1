income = int(input("Введите сумму выручки компании: "))
outcome = int(input("Введите сумму издержек компании: "))
profit = 0
earnings = 0
profitability = 0
if income > outcome:
    print("Компаия работает в плюс!")
    earnings = income-outcome
    profitability = (earnings/income)*100
    print(f"Рентабельность выыручки компании составляет: {profitability}%")
elif income == outcome:
    print("Компания работает в ноль")
else:
    print("Компания работает в убыток")
staff = int(input("Какое количество сотрудников в компании: "))
earnings_per_person = earnings/staff
print(f"Выручка на одного сотрудника составляет: {earnings_per_person} рублей/долларов/евро/шекелей")