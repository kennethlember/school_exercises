numbers = [4, 10, 8, 21, 25, 25, 26]
numbers.sort()
repeat = numbers.count(numbers[-1])

while repeat != 1:
    numbers.remove(numbers[-1])
    repeat = repeat - 1
    
if repeat == 1:
    print(numbers[-2])