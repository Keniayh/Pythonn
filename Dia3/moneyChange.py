coin1 = 10
coin2 = 5
coin3 = 1
count = 0

moneyExchange = int(input(""))

if moneyExchange > 1000:
    print(" ")
else:
    while moneyExchange >= 9:
        for i in range (0,1,1):
            moneyExchange = moneyExchange - coin1
            count = count + 1
    
    while moneyExchange >= 4:
        for i in range (0,1,1):
            moneyExchange = moneyExchange - coin2
            count = count + 1
    
    while moneyExchange >= 1:
        for i in range (0,1,1):
            moneyExchange = moneyExchange - coin3
            count = count + 1
            
    print(count)
