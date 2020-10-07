input_sec = int(input("Введите сколько секунд преобразовать: "))
hours = input_sec//3600
minutes = (input_sec%3600)//60
seconds = (input_sec%3600)%60
print(f"{hours}:{minutes}:{seconds}")