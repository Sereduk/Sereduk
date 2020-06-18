#Завдання 1
#Користувач вводить 3 числа. Далі в залежності від вибору користувача 
# потрібно знайти суму або добуток цих чисел. 
# (Тобто програма запитує в користувача, що потрібно зробити)


a = int(input("Enter 1 number:"))
b = int(input("Enter 2 number:"))
c = int(input("Enter 3 number:"))
d = input("change + or *")
if d == "+":
    print(a+b+c)
elif d == "*":
    print(a*b*c)


    #Завдання 2
#Користувач вводить 3 числа.
#Далі в залежності від вибору користувача потрібно знайти найбільше з 3-х, 
#найменше, або середнє арифметичне. (Подібно до 1-го)

a = int(input("Enter 1 number:"))
b = int(input("Enter 2 number:"))
c = int(input("Enter 3 number:"))
number = input("""Enter the 
> больше: 
< меньше: 
= среднее: """)
if number == ">":
    if a > b > c:
        print(a)
    elif b > a >c:
        print(b)
    elif c > b > a:
        print(c)
elif number == "<":
    if a < b < c:
        print(a)
    elif b < a < c:
        print(b)
    elif c < b < a:
        print(c)
elif number == "=":
    print((a+b+c)/3)


    #Користувач вводить з клавіатури кількість метрів.
    #В залежності від вибору - програма конвертує їх в сантиметри, міліметри, або кілометри.

    a = int(input("количество метров: "))
number = input("""Enter the 
cm: 
mm: 
km: """)
if number == "cm":
    if 100 * a:
        print("cm: ", a * 100)
elif number == "mm":
    if 1000 * a:
        print("mm:", a * 1000)
elif number == "km":
    if a / 1000:
        print("km", a / 1000) 