import math


print("Тестовое задание для Boenergo. Сервис для решений квадратных уравнений.")
print("Введите коэффиценты соответствуя формуле: ax^2 + bx + c = 0:")
a = float(input("Введите значение a= "))
b = float(input("Введите значение b= "))
c = float(input("Введите значение c= "))
Discr = b ** 2 - 4 * a * c
print(f"Дискриминант равен {Discr}")
if Discr < 0:
  print("Корней нет")
elif Discr == 0:
  x = -b / 2 * a
  print (f"Корень {x}")
else:
  x1 = (-b + math.sqrt(Discr)) / (2 * a)
  x2 = (-b - math.sqrt(Discr)) / (2 * a)
  print(f"Корень 1 {x1}")
  print(f"Корень 2 {x2}")