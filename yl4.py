a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
c = int(input("Sisesta kolmas arv: "))

if a > b and a > c:
    maximum = a
elif b > a:
    maximum = b
else:
    maximum = c
    
print("Nende arvude maksimum on " + str(maximum) + ".")