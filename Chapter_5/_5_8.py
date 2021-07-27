people = ['Player1','Player2','Player3','Player4','ADMIN']

for peoples in people:
  if (peoples == "ADMIN"):
    print("Dear ADMIN would you like to see your status report")
  else:
    print(f'Hello {peoples}, thankyou for logging into this website')
