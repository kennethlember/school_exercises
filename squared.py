number = int(input("Sisesta number: "))
numbers = []
numbers.extend(range(number))
string = ''
for i, e in enumerate(numbers):
    if i == len(numbers) - 1:
        string += str(e ** 2)
    else:
        string += str(e ** 2) + ', '
print(string)