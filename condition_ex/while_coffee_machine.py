coffee = 10
while True:
  money = int(input())
  
  if money >= 300:
    print('change is %d and get you coffee' %(money-300))
    print("remaining amount of coffee is %d" %coffee)
    coffee -= 1;
  else: 
    print("no money no coffee")
    print("remaining amount of coffee is %d" %coffee)
  if coffee == 0:
    print('sorry no coffee')
    break;
