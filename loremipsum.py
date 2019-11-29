dict_of_letters = {}
sorted_dict = {}

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non sem eu magna varius pulvinar. ' \
        'Integer eu quam imperdiet, pellentesque lorem at, sagittis felis. Nulla id varius est. Nulla quis mi ' \
        'commodo, mollis sapien sed, auctor ex. Aliquam sed accumsan nulla. Donec fermentum urna consectetur ' \
        'sollicitudin vestibulum. Vestibulum sollicitudin neque vitae bibendum tempus.'

for i in lorem:
    if i.isalpha() and i.upper() not in dict_of_letters:
        dict_of_letters[i.upper()] = 1
    elif i.isalpha() and i.upper() in dict_of_letters:
        dict_of_letters[i.upper()] += 1

for i in sorted(dict_of_letters.keys()):
    sorted_dict[i] = dict_of_letters[i]

print(sorted_dict)