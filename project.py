#Игра горячо-холодно
number=90
appmax=0
result=0
while result != number:
 result=int(input('Введи число от 1 до 100: '))
 appmax +=1
 print(f"Попыток: {appmax}")  
 if result > number:
  print('Горячо!')
 elif result < number:
  print('Холодно!')
 elif result == number:
  print(f"Угадал!Количество попыток: {appmax}")
  break
