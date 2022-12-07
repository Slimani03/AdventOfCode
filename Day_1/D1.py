text = open ("input.txt","r").read()
summa = 0
lista = []
part2 = False

for calorie in text.splitlines():
    if (calorie == ""):
        lista.append(summa)
        summa=0
    else:
        calories = int(calorie)
        summa += calories

lista.sort()
print(max(lista))

if part2==True:
    summa= sum(lista[-3:])
    print (summa)