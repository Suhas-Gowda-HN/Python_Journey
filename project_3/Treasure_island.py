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
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
      ''')

print("Welcome to Treasure Island.")
print('''
You are not a hero.
You are a desperate soul… chasing a treasure that has buried kings, shattered empires, and driven men insane.
Legends call it “The Heart of Oblivion.”
No one who has seen it… has returned the same.
''')
step1 = input("Your broken boat crashes onto a cursed island. The waves retreat… unnaturally silent.\nAhead:\n1. A dark jungle, whispering your name\n2. A rotting shipwreck, half-buried in sand\nMake your choice: 1 or 2 ?... ")
if int(step1)==2:
    print("\nYou find a rusted compass… it spins wildly, then locks onto something deep inland.\n⚡ You may proceed… but something is watching.")
    step2=input('''
Following the compass, you reach ancient ruins.
Two paths:
3.Enter a tunnel echoing with whispers
4.Climb a cracked staircase toward a glowing chamber
          Make your choice: 3 or 4 ?... ''')
    if int(step2)==3:
        print("\nYou reach a chamber with 3 ancient symbols… but only one path forward.\n💀 The air feels… alive.")
        step3 = input('''\n
At the center lies the treasure… but guarded by a shadow that looks exactly like you.
It speaks:
"Only one of us leaves."
Two choices:
5. Fight the shadow
6. Bow and accept its power
        Make your choice: 5 or 6 ?... ''')
        if int(step3)==6:
            print('''
You kneel… accepting the darkness.
The shadow smiles… and merges with you.

🏆 You become the guardian of the treasure.
Not a hero… not a victim…
Something far worse.

YOU FOUND THE TREASURE… BUT LOST YOUR SOUL.
                  ''')
        else:
            print("\nYou attack… but every move you make, it mirrors perfectly.\n⚔️ You cannot defeat yourself.You fall.")
            print("\n\tGAME OVER\n")
    else:
        print("\nVoices grow louder… they mimic your thoughts…\tYou realize too late — they are inside your head.\n🧠 You lose yourself forever.")
        print("\n\tGAME OVER\n")

else:
    print("\nYou walk in… vines tighten… something breathes behind you.\n🔥 You are dragged into the darkness.")
    print("\n\tGAME OVER\n")