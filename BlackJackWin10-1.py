import random

def getCard():
    card = random.random()
    return int(card * 13 + 1)

def value(card):
    if card < 11:
        return card
    else:
        return 10

def name(card):
    #names = ['Joker', 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight','Nine','Ten','Jack','Queen','King']
    names = "Joker Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King".split()
    return names[card]

def hasAce(hand):
    for card in hand:
        if card == 1:
            return True
    return False

def softSum(hand, isAce):
    sum = 0
    for card in hand:
        card = value(card)
        sum += card
    if sum < 12 and isAce == True:
        sum += 10
    elif sum > 21 and isAce == True:
        sum -= 10
    return sum 

def sum(hand):
    sum = 0
    for card in hand:
        sum += value(card)
    return sum

def busted(hand):
    sum = 0
    for x in hand:
        sum += x
    if sum > 21:
        return True
    else:
        return False

def handValue(hand, points, isAce):
    if isAce == True:
        return softSum(hand, isAce)
    else:
        return sum(hand)

def handNames(hand):
    names = ""
    for card in hand:
        cardName = name(card)
        #cardName.join(names)
        #" ".join(names)
        names += cardName + " "
        #names.append(cardName + " ")
    return names

def dealerHit(dealerHand, dealerHandNames, dealerPoints):
    newCard = getCard()
    dealerHand.append(newCard)
    newAce = hasAce(dealerHand)
    dealerPoints = handValue(dealerHand, dealerPoints, newAce)
    return dealerPoints

def playerHit(playerHand, playerHandNames, playerPoints):
    newCard = getCard()
    playerHand.append(newCard)
    newAce = hasAce(playerHand)
    playerPoints = handValue(playerHand, playerPoints, newAce)
    return playerPoints

def printRound(playerHandNames,playerPoints, dealerHandNames, dealerPoints):
    print("")
    print(f"Player Hand: {playerHandNames}")
    print(f"Player Points: {playerPoints}")
    print(f"Dealer Hand: {dealerHandNames}")
    print(f"Dealer Points: {dealerPoints}")
    print("")

playerHand = [getCard(),getCard()]
playerHandNames = ""

dealerHand = [getCard(), getCard()]
dealerHandNames = ""

playerPoints = 0
dealerPoints = 0
playerScore = 0
gameCount = 1

dealerStands = False
playerStands = ""

gameOver = False

playerHandNames = handNames(playerHand)
dealerHandNames = handNames(dealerHand)
dealerNameSplit = dealerHandNames.split()
hideDealer = ""
hideDealer = hideDealer.join(dealerNameSplit[1:])
hideDealer += " "


playerAce = hasAce(playerHand)
dealerAce = hasAce(dealerHand)

playerPoints = handValue(playerHand, playerPoints, playerAce)
dealerPoints = handValue(dealerHand, dealerPoints, dealerAce)

print(f"Game #{gameCount}:")
print("")
print(f"Player Hand: {playerHandNames}")
print(f"Player Points: {playerPoints}")
print(f"Dealer Hand: {hideDealer}")
print(f"Dealer Points: {dealerPoints}")
print("")

while gameCount < 11:

    while dealerStands == False and playerStands != "Stand" or dealerStands == False and dealerPoints < 15 and dealerPoints < playerPoints:

        if playerPoints == 21:
            print("Player wins by blackJack!")
            playerScore += 10
            break

        if dealerPoints == 21:
            print("Dealer wins by blackjack!")
            playerScore -= 10
            break
            
        # playerHits
        if playerPoints < 21 and playerStands != "Stand":
            if len(playerHand) == 5:
                playerStands == "Stand"
                break

            playerStands = input("Would you like to 'Hit' or 'Stand': ")
            if playerStands == "Hit":
                print("\nYou hit!")
                playerPoints = playerHit(playerHand, playerHandNames, playerPoints)
                playerHandNames = handNames(playerHand)
                printRound(playerHandNames,playerPoints, dealerHandNames, dealerPoints)
        
        # Dealer Hits
        if dealerPoints < 15 and playerPoints < 21:
            print("\nDealer Hits!")
            dealerPoints = dealerHit(dealerHand, dealerHandNames, dealerPoints)
            dealerHandNames = handNames(dealerHand)
            dealerNameSplit = dealerHandNames.split()
            hideDealer = ""
            hideDealer = " ".join(dealerNameSplit[1:])
            printRound(playerHandNames,playerPoints, hideDealer, dealerPoints)
            if dealerPoints > 15:
                dealerStands == True
        else:
            dealerStands == True

        if dealerPoints > 21:
            print("")
            print(f"Player Wins! Dealer Busted: {dealerPoints}")
            print("")
            playerScore += 10
            gameOver = True
            break

        if playerPoints > 21  :
            print("")
            print(f"Dealer Wins! Player Busted: {playerPoints}")
            print("")
            playerScore -= 10
            gameOver = True
            break

    #Dealer wins
    if gameOver == False and playerPoints != 21 and dealerPoints != 21:    

        # 5 card
        if len(playerHand) > 4 and playerPoints < 22 and gameOver == False:
            print("")
            print(f"Player Wins! 5 card charlie!")
            print("")
            break

        if dealerPoints >= playerPoints:
            print("\nDealer Wins!\n")
            playerScore -= 10
        else:
            print("\nPlayer Wins!\n")
            playerScore += 10

    # reset values for next round
    gameCount += 1
    print("")
    print(f"Overall Score after game {gameCount-1}: {playerScore}")
    print("\n" * 10) 

    if gameCount < 11:
        print(f"Game #{gameCount}:")

        playerHand = [getCard(), getCard()]
        playerHandNames = ""

        dealerHand = [getCard(), getCard()]
        dealerHandNames = ""

        playerPoints = 0
        dealerPoints = 0

        dealerStands = False
        playerStands = ""

        playerHandNames = handNames(playerHand)
        dealerHandNames = handNames(dealerHand)

        playerAce = hasAce(playerHand)
        dealerAce = hasAce(dealerHand)

        playerPoints = handValue(playerHand, playerPoints, playerAce)
        dealerPoints = handValue(dealerHand, dealerPoints, dealerAce)

        printRound(playerHandNames,playerPoints, dealerHandNames, dealerPoints)

    # Aces count 1 or 11     DONE
    # Face cards count 10    DONE
    # Dealer wins ties       DONE
    # player plays first     DONE
    # 22 is bust             DONE
    # dealer always stands on hard 15  DONE
    # opening hand reveals one of dealers cards  DONE but not finished
    # 5 cards < 22 is a win for player DONE
    # each hand worth 10 DONE
    # game goes for 10 hands DONE