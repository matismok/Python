print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

decision = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n')

if decision == "left":
    decision_nr2 = input('You come to lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                         'boat. Type "swim" to swim across.\n')
    if decision_nr2 == "swim":
        print('''
        
                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\ ""--.:-.     `.                            .:/
                  \. /    `-._   `.""-----.,-..::(--"".\ ""`. `:\ 
                   `P         `-._ \          `-:\           `. `:\ 
                                   ""            "             `-._) 
                                   
             You died!!!!!!!!!!!!!                        
                                   
                               
        ''')
    elif decision_nr2 == "wait":
        decision_nr3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow "
                             "and one blue. Which collor do you choose? \n")
        if decision_nr3 == "red":
            print("Game over")
        elif decision_nr3 == "yellow":
            print("Game over")
        elif decision_nr3 == "blue":
            print("You won, collect your prize!")
elif decision == "right":
    print('''
                      __  __
                    /_ _^^_ _\ 
               _____|________|______
              `=====.'""""""'.=====`
                   / /a    /a \   .-.
                  |     /\     | <"  )
                  \            /  /  \ 
     .`\,         _'. \/\/\/ .'_  \ \_\  ./,'
    '-. \-------'  \`------'/  '--""---'//.-'
 ###'.-'/________    \/""""\/    ________\-.'###
     '/`         \      :       /         `\`
                  |            |
                  \     :      |
                  |            \ 
                  \_____:_____ /
                   [I=I=[_]I=I]
                  /    |       \ 
                 /      |_       \ 
                /       /\       \ 
               /       /##\       \ 
               |     ,/ ## \,     |
                \    \  ##  /    /
                 \    \ ## /    /
                  \    \##/    /
              jgs  \   /\/\   /
                 __,\_/X##X\_/.__
               '.' /|\ \XX//|\ '.`
                 '/' |.\##/,|`\ '
                        ##
                        ##
                        ##
                      \ ## /     /
            \ ,   \  \ \##// , / /,   /.
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

                Dead end. You lost! :)
''')
else:
    print("Wrong direction. Try again!")
