Pizzas = ['4 Chesse','Truffle','White sauce']

Friends_Pizzas = Pizzas[:]

Pizzas.append('Mushroom')

Friends_Pizzas.append('Cheese')

for pizza in Pizzas:
  print(f'I really love {pizza} pizza.\n')

for friend_pizza in Friends_Pizzas:
  print(f'My friend really loves {friend_pizza} pizza.\n')
  

