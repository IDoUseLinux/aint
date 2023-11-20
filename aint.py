from random import SystemRandom ## Lets make this truely random!

## (C) IDoUseLinux, MIT License, 2023

def spoof_text(ai_text, scramble_aggresiveness) :
    spoofed_text = ''
    for letter in ai_text :
        ## We take the original string and start scrambling it with look-alikes
        if letter == "a" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "а"
        elif letter == "c" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "с"
        elif letter == "c" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ԁ"
        elif letter == "h" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "һ"
        elif letter == "i" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "і"
        elif letter == "j" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ј"
        elif letter == "n" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ո"
        elif letter == "o" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = ["о", "ο", "օ" ][SystemRandom().randint(0,2)]
        elif letter == "q" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "р"
        elif letter == "v" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "ν"
        elif letter == "x" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "х"
        elif letter == "y" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "у"
        elif letter == ";" and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = ";"
        elif letter == "." and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "․"
        elif letter == "," and SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter = "‚"

        ## The invisible characters
        if SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter += "‎"*SystemRandom().randrange(0,5)
        if SystemRandom().randrange(0, scramble_aggresiveness) == 0 : letter += "‍"*SystemRandom().randrange(0,5)
        spoofed_text += letter
    return spoofed_text 

ai_text = ''
while True :
    ## We ask them to input the ai-generated text 1 paragraph at a time because any enters would mess with the input option. 
    ai_paragraph = input("Please enter the AI-generated text 1 paragraph at a time. Leave blank if finished copying.\n") 
    if ai_paragraph != '' : 
        ai_text += ai_paragraph
    else : break

scramble_aggresiveness = input("Please input the amount of scramble aggressiveness, leave blank for default\n")
print(scramble_aggresiveness)
while scramble_aggresiveness.isdigit() == False and scramble_aggresiveness != '' :
    scramble_aggresiveness = input("Please input the amount of scramble aggressiveness, leave blank for default\n")

if scramble_aggresiveness == '' :
    scramble_aggresiveness = 30 
else : scramble_aggresiveness = int(scramble_aggresiveness)

print(spoof_text(ai_text=ai_text, scramble_aggresiveness=scramble_aggresiveness))