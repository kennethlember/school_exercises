def number(a, b):
    result = a * b
    return str(a) + ' x ' + str(b) + ' = ' + str(result)
    

user_number = int(input('Sisesta number, mille korrutustabelit soovid näha: '))
i = 0

while i < 13:
    print(number(user_number, i))
    i = i + 1