number = int(input("Sisesta number: "))
numbers = []
numbers.extend(range(number))
string = ''
for i, e in enumerate(numbers):
    if i == len(numbers) - 1:
        string += str(i ** 2)
    else:
        string += str(i ** 2) + ', '
print(string)