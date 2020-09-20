import random

tot_p_wins = 0
tot_c_wins = 0
draws = 0
game_end = False

deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
        11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
len_deck = 52
while len_deck >= 6:

    def getcard():
        global len_deck
        len_deck -= 1
        if len_deck <= 0:
            return ("all cards have been played")
        else:
            index = random.randint(1, len_deck)
            card = deck[index]
            deck.pop(index)
            return card


    def pic_card(card_value, user):
        if card_value == 11 or card_value == 12 or card_value == 13:
            return (10)
        elif (card_value == 14) and user == "p":
            z = int(input("do you want your ace to be an 11 or a 1 "))
            return (z)
        elif (card_value == 14) and user == "c":
            z = random.randrange(1, 12, 10)
            return (z)
        else:
            return (card_value)  # if the card is a jack, queen, king or ace


    p_card_1 = getcard()
    p_card_1 = pic_card(p_card_1, "p")
    print("your hand is ")
    print(p_card_1)

    p_card_2 = getcard()
    p_card_2 = pic_card(p_card_2, "p")
    print(p_card_2)

    print("       ")

    c_card_1 = getcard()
    c_card_1 = pic_card(c_card_1, "c")
    print("the computers hand is ")
    print(c_card_1)

    c_card_2 = getcard()
    c_card_2 = pic_card(c_card_2, "c")

    # ----------------------------

    p_tot = p_card_1 + p_card_2
    c_tot = c_card_1 + c_card_2


    # -------------------------
    def twist(user):
        temp = getcard()
        temp = pic_card(temp, user)
        print("you got a", temp)
        return (temp)


    # ------------------
    def stick():
        global c_tot
        global tot_c_wins
        global tot_p_wins
        global draws
        global game_end

        while c_tot <= 17 and game_end == False:
            temp = getcard()
            temp = pic_card(temp, "c")
            print("the computer's total is ", c_tot)
            print("the computer twisted and got ", temp)

            c_tot = c_tot + temp
            print("the computer's new total is ", c_tot)

        print("       ")

        if c_tot > 21 and game_end == False:
            print("the computer went bust")
            tot_p_wins += 1
            game_end = True

        if p_tot > c_tot and p_tot <= 21 and game_end == False:
            print("YOU WON")
            print("the computer had ", c_tot)
            tot_p_wins += 1
            game_end = True

        if p_tot < c_tot and c_tot <= 21 and game_end == False:
            print("you lost, the computer had ", c_tot)
            tot_c_wins += 1
            game_end = True

        if p_tot == c_tot and game_end == False:
            print("YOU Drew")
            print("the computer had ", c_tot)
            draws += 1
            game_end = True


    while (p_tot < 17):

        choice = input("to twist type twist ")
        print("       ")
        if choice == "twist":
            temp = twist("p")

            p_tot = p_tot + temp
            print("your total is ", p_tot)

        if p_tot > 21:
            print("you went bust")
            tot_c_wins += 1
            break;

    while (p_tot >= 17 and p_tot < 22):
        choice = input("do you want to stick or twist")
        print("       ")
        if choice == "twist":
            temp = twist("p")

            p_tot = p_tot + temp
            print("your total is ", p_tot)

        if choice == "stick":
            stick()
            break;
    print("       ")
    print("~~~~~~~~~~~~~")
    print("total p wins", tot_p_wins)
    print("total c wins", tot_c_wins)
    print("total draws", draws)
    print("~~~~~~~~~~~~~")
    print("       ")
    game_end = False

print("there are no more cards left in the deck to play blackjack")
print("the final scores were ")
print("       ")
print("~~~~~~~~~~~~~")
print("total p wins", tot_p_wins)
print("total c wins", tot_c_wins)
print("total draws", draws)
print("~~~~~~~~~~~~~")





