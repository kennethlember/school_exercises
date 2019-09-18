import math

r = float(input("Sisesta ringi raadius: "))
c = r * 2 * math.pi
s = r * r * math.pi
print("Kui ringi raadius on " + str(r) + ", siis selle ümbermõõt on " + str(round(c, 2)) + " ja selle pindala on " + str(round(s, 2)) + ".")