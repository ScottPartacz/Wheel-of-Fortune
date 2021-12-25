# %%
import json
import random
import time

bank = [0,0,0]
number_of_normal_rounds = 2
wheel = ["Lose a Turn","BANKRUPT","Mystery","Million"]
for x in range (2,19):
    wheel.append(str(50 * x))

file = open("phrases.json","r")
phrases_hints = json.load(file)
used_phrases = []

def findphrase():
    while(True):

        temp = random.choice(list(phrases_hints.items()))
        phrase = temp[0]
        hint = temp[1]

        if phrase in used_phrases:
            continue
        else:
            print("\n" + phrase)
            used_phrases.append(phrase)
            break
        
    display_word = ["_"] * len(phrase)

    for x in range(0,len(phrase)):
        if phrase[x] == " ":
            display_word[x] = " "
            continue
        if phrase[x].isalpha() == False:
            display_word[x] = phrase[x] 
    
    print(" ".join(display_word))
    print("\n" + "Hint: " + hint + "\n")
    return [phrase,display_word]

def spin():

    temp = random.randint(0,len(wheel) - 1)
    land = wheel[temp]

    if land.isnumeric():
        return land

    elif land == "Lose a Turn":
        return 1

    elif land == "BANKRUPT":
        return 0

    elif land == "Mystery":
        flip = random.randint(1,2)

        print("you landed on Mystery lets see what you get (1000 or BANKRUPT)\n")

        if flip == 1:
            return 1000
        else:
            return 0

    elif land == "Million":
        section = random.randint(1,3)
        print("you landed on the million lets see whay you get (Million or BANKRUPT)\n")

        if section == 2:
            return 1000000
        else:
            return 0

def rounds(bank):
    round_balance = [0,0,0]
    player_turn = random.randint(1,3)
    guesslist = [" "]
    
    results = findphrase()

    phrase = results[0]

    display_word = results[1]
    
    while(True):
        wrong = False
        if player_turn >= 4:
            player_turn = 1
        
        while(True):

            #print(round_balance)
            print("player " + str(player_turn) + " please spin the wheel \n") 
            spun = spin()
        
            if spun == 1:
                print("you landed on lose your turn\n")
                player_turn += 1
                break
        
            elif spun == 0:
                print("you landed on BANKRUPT your round balance has been reset\n")
                round_balance[player_turn - 1] = 0
                player_turn += 1
                break

            else:
                print("you landed on: " + str(spun) + "\n")

            print("would you like to solve the puzzle? y/n\n")
            time.sleep(1)
            yes_no = input().lower()

            if yes_no == "y":
                print("what is the puzzle?")
                time.sleep(1)
                full_guess = input().lower()

                if full_guess == phrase.lower():
                    print("\nyou solved the puzzle\n")
                    print(phrase)
                    bank[player_turn-1] += round_balance[player_turn-1]
                    return bank
                else:
                    print("sorry that is not correct\n")
                    player_turn += 1
                    break
            while(True):
                occurances = 0
                print(" ".join(display_word))
                flag = False
                print("\nplease enter your guess\n")
                time.sleep(1)
                guess = input().lower()

                for x in guesslist:
                    if guess.isnumeric() or len(guess) > 1 or len(guess) <= 0 or guess == x or guess in ["a","e","i","o","u"]:
                        print("invaild input\n")
                        flag = True
                        break
                if flag:
                    continue
                    
                if guess in phrase.lower():
                    for x in range(0,len(phrase)):
                        if guess == phrase[x].lower():
                            display_word[x] = phrase[x]
                            occurances += 1
                    print(" ".join(display_word))
                    round_balance[player_turn-1] += int(spun) * occurances
                else:
                    wrong = True
                
                break

            if wrong:
                player_turn += 1
                continue    
        
            if round_balance[player_turn-1] >= 250:

                print("\nwould you like to buy a vowel y/n\n")
                time.sleep(1)
                yes_no = input().lower()

                if yes_no == "y":
                    while(True):
                        flag = False
                        print("please enter your guess\n")
                        time.sleep(1)
                        guess = input().lower()

                        for x in guesslist:
                            if guess.isnumeric() or len(guess) > 1 or len(guess) <= 0 or guess == x or guess not in ["a","e","i","o","u"]:
                                print("invaild input\n")
                                flag = True
                                break
                        if flag:
                            continue

                        if guess in phrase.lower():
                            for x in range(0,len(phrase)):
                                if guess == phrase[x].lower():
                                    display_word[x] = phrase[x]
                            print(" ".join(display_word))
                        
                        else:
                            print("sorry there is no " + guess + "'s in the phrase")
                            wrong = True

                        round_balance[player_turn-1] -= 250
                        break
                
            if wrong:
                player_turn += 1
                break

def final_round(bank):
    max_prize = 0
    player = 0
    for x in range(0,len(bank)):
        if bank[x] == max_prize:
            temp = random.randint(1,2)
            if temp == 1:
                continue
            else:
                max_prize = bank[x]
                player = x
        if bank[x] > max_prize:
            max_prize = bank[x]
            player = x
    
    print("player " + str(player + 1) + " is moving on to the final round for a chance to win: " + str(max_prize) + "\n")

    results = findphrase()

    phrase = results[0]

    display_word = results[1]

    letters = ["r","s","t","l","n","e"]

    extra_letters = []

    print("revealing given letters\n",letters)

    for x in range(0,len(phrase)):
        for y in letters:
            if y == phrase[x].lower():
                display_word[x] = phrase[x]
    
    print("\n" + " ".join(display_word))

    print("\nyou will now be prompted to give us 3 consonats and 1 vowel in that order")

    for x in range(0,4):
        if x == 3:
            while(True):
                print("\nplease enter a vowel")
                time.sleep(1)
                guess = input().lower()
                if guess.isnumeric() or len(guess) > 1 or len(guess) <= 0 or guess == x or guess not in ["a","e","i","o","u"]:
                    print("invaild input")
                    continue
                extra_letters.append(guess)
                break

        else:
            while(True):
                print("\nplease enter a consonant:")
                time.sleep(1)
                guess = input().lower()
                if guess.isnumeric() or len(guess) > 1 or len(guess) <= 0 or guess == x or guess in ["a","e","i","o","u"]:
                    print("invaild input")
                    continue
                extra_letters.append(guess)
                break

    for x in range(0,len(phrase)):
        for y in extra_letters:
            if y == phrase[x].lower():
                display_word[x] = phrase[x]
        
    print("\n" + " ".join(display_word))

    print("\nyou have one guess to solve the puzzle good luck\n")

    time.sleep(1)
    guess = input().lower()

    if guess == phrase.lower():
        print("YOU WIN =)")
        print("\nPRIZE: ",max_prize)
    else:
        print("YOU LOSE =(")



for x in range(0,number_of_normal_rounds):
    bank = rounds(bank)
    #print("\nBank Values: ",bank)

final_round(bank)






