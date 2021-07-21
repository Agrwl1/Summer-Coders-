wannago = ['Paris','Colombia','New York','Jerusulam','Hong Kong']

number = len(wannago)
revesed_wannago = wannago.copy() 
revesed_wannago.sort(reverse=True)

print(f'\n\n{wannago}')

print(f'\n\n{sorted(wannago)}')

print(f'\n\n{revesed_wannago}')

wannago.reverse()

print(f'\n\n{wannago}')

wannago.reverse()

print(f'\n\n{wannago}')

print(f'There are currently {number} places I wanna go to')

pop_wannago = wannago.pop()

print(f'\n\n{wannago}')

wannago.append('India')

print(f'\n\n{wannago}')