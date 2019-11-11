import random

number = random.randint(0, 100)
guess = -1
while number != guess:
    guess = int(input('Sisesta oma pakkumine: '))

    if number < guess:
        print('Sinu pakkumine oli kahjuks vale. Õige number on pakkumisest väiksem.')    
    elif number > guess:
        print('Sinu pakkumine oli kahjuks vale. Õige number on pakkumisest suurem.')
        
print('Palju õnne! Sa pakkusid õige arvu. Õige arv oli: ' + str(number) + '.')
replay = input(str('Kas soovid veel mängida? (y/n): '))

if replay == 'y':
     guess
elif replay == 'n':
    return