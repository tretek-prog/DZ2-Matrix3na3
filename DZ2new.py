m1 = []
m2 = []
otvet = input("Что делаем?! (+ или * ): ")
print("Введите первую матрицу")
for x in range(3):                  #Вводим 1-ую матрицу.
    a = []
    for y in range(3):
        a.append(int(input()))
    m1.append(s)
    
for x in range(3):                  #Вывод 1-ой матрицы для проверки.
    for y in range(3):
        print(m1[x][y], end=" ")
    print()
    
print("Введите вторую матрицу")
for x in range(3):                  #Вводим 2-ую матрицу.
    a = []
    for y in range(3):
        a.append(int(input()))
    m2.append(s)
    
for x in range(3):                  #Вывод 2-ой матрицы для проверки.
    for y in range(3):
        print(m2[x][y], end=" ")
    print()
print()

if  otvet == "+":
    for x in range(3):
        for y in range(3):
            m1[x][y] += m2[x][y]
elif otvet == "*":
     for x in range(3):
         for y in range(3):
             m1[x][y] *= m2[x][y]
for x in range(3):
    for y in range(3):
        print(m1[x][y], end = " ")     
    print()
