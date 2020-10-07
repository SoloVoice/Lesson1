first_day_result = float(input("Сколько киломестров пробежал спортсмен в первый день? "))
goal = float(input("Сколько километров должен пробежать спортсмен? "))
days = 0
while first_day_result < goal:
    first_day_result = first_day_result*1.2
    days += 1
print(f"Спортсмен достигнет желаемого результата через {days} дней")