import random

valikud = ['r', 'p', 's']

replay = 'y'

while replay.lower() == 'y':
    valik = input('Sisesta oma valik(r, p, s): ')

    cpuvalik = random.choice(valikud)
    
    if valik == cpuvalik:
        print('Sinu valik: ' + valik + ', Arvuti valik: ' + cpuvalik + '. Tulemus on viik!')

    elif cpuvalik == 'r' and valik == 'p' or cpuvalik == 'p' and valik == 's' or cpuvalik == 's' and valik == 'r':
        print('Sinu valik: ' + valik + ', Arvuti valik: ' + cpuvalik + '. Tulemus on sinu võit!')

    else:
        print('Sinu valik: ' + valik + ', Arvuti valik: ' + cpuvalik + '. Tulemus on sinu kaotus!')

    replay = input('Kas soovid veel mängida?(Y/N): ')