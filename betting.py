import random
d = open("betdata.txt", "w")
d.write("Strategy,Starting Funds,Target Funds,Color,Wins,Losses,Total Rounds,Ending Funds\n")

def Gamble():
    red = [1,3,5,7,9, 12,14,16,18,19,21,23,25,27,30,32,34,36]
    blk = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    result = random.randint(0,36)
    if result == 0:
        return "green"
    elif result in red:
        return "red"
    elif result in blk:
        return "black"
    else:
        print ("it broke")
        return 0

def Mart(color, target, funds):
    stratg = "Martingale"
    start = funds
    win = 0
    loss = 0
    rounds = 0
    bet = 10
    while ((funds < target) and (funds > 0)):
        if color != Gamble():
            funds -= bet
            bet *= 2
            loss += 1
            rounds += 1
            print ("lost! increasing bet ($" + str(funds) + ")")
        else:
            funds += bet
            win += 1
            rounds += 1
            print ("won! same bet ($" + str(funds) + ")")
    if funds >= target:
        print ("won a total of " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    else:
        print ("bankrupt! Now at " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    
def AntiMart(color, target, funds):
    stratg = "Anti-Martingale"
    start = funds
    win = 0
    loss = 0
    rounds = 0
    bet = 10
    while ((funds < target) and (funds > 0)):
        if color == Gamble():
            funds += bet
            bet *= 2
            win += 1
            rounds += 1
            print ("won! increasing bet ($" + str(funds) + ")")
        else:
            funds -= bet
            loss += 1
            rounds += 1
            if (bet > 2):
                bet = int(bet/2)
            print ("lost! decreasing bet ($" + str(funds) + ")")
    if funds >= target:
        print ("won a total of " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    else:
        print ("bankrupt! Now at " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    
def Oscar(color, target, funds):
    stratg = "Oscar's Grind"
    start = funds
    win = 0
    loss = 0
    rounds = 0
    bet = 10
    betUnit = bet
    cycleProfit = 0
    while ((funds < target) and (funds > 0)):
        if color != Gamble():
            funds -= bet
            loss += 1
            rounds += 1
            cycleProfit -= bet
            print ("lost! same bet ($" + str(funds) + ")")
        else:
            funds += bet
            win += 1
            rounds += 1
            cycleProfit += bet
            if (cycleProfit > 0):
                bet = betUnit
                cycleProfit = 0
                print ("won! cycle restart ($" + str(funds) + ")")
            elif (cycleProfit == 0):
                bet = betUnit
                print ("won! bet set to unit ($" + str(funds) + ")")
            elif ((cycleProfit < -bet) and (cycleProfit != 0)):
                bet += betUnit
                print ("won! increasing bet for cycle ($" + str(funds) + ")")
            elif (cycleProfit >= -bet):
                bet = abs(cycleProfit) + betUnit
                print ("won! bet set for positive unit profit for cycle ($" + str(funds) + ")")
    if funds >= target:
        print ("won a total of " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    else:
        print ("bankrupt! Now at " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
        
def Labouche(color, target, funds):
    stratg = "Labouchere"
    start = funds
    win = 0
    loss = 0
    rounds = 0
    groceries = []
    temp = target - funds
    while (temp >= 20):
        newAdd = random.randint(1,20)
        temp -= newAdd
        groceries.append(newAdd)
    while ((temp < 20) and (temp > 0)):
        newAdd = random.randint(1,temp)
        temp -= newAdd
        groceries.append(newAdd)
    print (groceries)
    while ((funds < target) and (funds > 0)):
        if (len(groceries) > 1):
            currentBet = groceries[0] + groceries[-1]
        else:
            currentBet = groceries[0]
            
        if color == Gamble():
            win += 1
            rounds += 1
            funds += currentBet
            groceries.pop(0)
            if (len(groceries) > 0):
                groceries.pop(-1)
            print ("won! removing from list ($" + str(funds) + ")")
        else:
            loss += 1
            rounds += 1
            funds -= currentBet
            groceries.append(currentBet)
            print ("lost! adding " + str(currentBet) + " to list ($" + str(funds) + ")")
    if funds >= target:
        print ("won for a total of " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    else:
        print ("bankrupt! Now at " + str(funds))
        d.write(stratg + "," + str(start) + "," + str(target) + "," + str(color) + "," + str(win) + "," + str(loss) + "," + str(rounds) + "," + str(funds) + "\n")
    
    
while True:
    response = input('\nMethod? : ')
    if (response == 'mart'):
        Mart(str(input('color: ')), int(input('target: ')), int(input('funds: ')))
    elif (response == 'antimart'):
        AntiMart(str(input('color: ')), int(input('target: ')), int(input('funds: ')))
    elif (response == 'labouche'):
        Labouche(str(input('color: ')), int(input('target: ')), int(input('funds: ')))
    elif (response == 'oscar'):
        Oscar(str(input('color: ')), int(input('target: ')), int(input('funds: ')))
    else:
        d.close()
        break