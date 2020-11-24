
pages = [
    "The mists of your scrying pool clear to reveal the tower of the One-Eyed Wizard, on the coast of the Jagged Sea. Searching the area with your clairvoyance probe, you spot a man sleeping under a moonlit tree. His sword and pack lie to his side."
    ,"The man wakes with a start. You now control his every move! The tower looms atop the coastal mountain range."
    ,"The man dozes off. After some well-deserved rest, he feels ready to tackle the day."
    ,"After an hour of hiking through rocky terrain, you come across a pack of kobolds! As you approach, they scurry away... to reveal a corpse!"
    ,"The man gathers himself and walks on.\n -~- SCRYING POOL MESSAGING SYSTEM -~-\n\nThis is a message from A. the wizard. That corpse back there was the agent I sent, to try to remove the evil spirit from our friend the One-Eyed wizard. On him is an amulet which can seal away the spirit if you get it to look directly at the amulet. Your only chance is to get that amulet!"
    ,"The corpse is covered in fallen stones. All you can uncover is a crystal amulet and a note. The note reads:\n'Seal the spirit posessing the One-Eyed wizard by getting him to look directly at the amulet.'"
    ,"You direct the man along the bottom of a gully in the rock, leading up towards the tower. Not long after, a storm breaks out. A stream develops below the man's feet, threatening to fill the gully."
    ,"You increase his pace. From above, you hear tiny chittering... suddenly, rocks fall! Somewhere deep within the man, warrior instincts awaken, and he jumps aside."
    ,"Struggling up the slick cliffs, he nearly loses grip a couple times. Once at the top, you see the pack of kobolds again, keeping watch of below and preparing to toss rocks below. They spot you, and flee!"
    ,"The entrance to the One-Eyed wizard's grand tower now stands before you. His doors are as always wide open, but there is a chilling atmosphere..."
    ,"As soon as you cross the threshold, you suddenly feel enclosed. Looking around, you're in a long north-south hallway."
    ,"The hallway extends north and south."
    ,"The hallway has, on the north wall, a tapestry made to look like the rest of the wall. The hallway extends south and west."
    ,"There is a door to the south. The hallway extends east-west."
    ,"You enter the room and find an old man camped here. He says:\n'I used to be the One-Eyed wizard's assistant... But recently, something terrible happened. I can't find him anywhere... I've lost myself in these halls... Begone!"
    ,"The man, eager to use his sword, cuts down the tapestry, revealing a winding stair leading up!"
    ,"The stair continues for some time until it opens up to a massive room, with wide windows showing a storm brewing off the coast. Thunder cracks, and a robed figure turns to face the man. Only one eye can be seen under the folds of his cloak.\n'I.. am the One-Eyed wizard! Who... are you..?'"
    ,"Before the man has a chance to draw his sword, the One-Eyed wizard strikes him down with a bolt of lightning from the coastal storm!"
    ,"'What?' the One-Eyed wizard says.\nThen, he looks, and a dark miasma is drawn from within his cloak, and into the amulet!\n'Thank you, Deszmo. You wear a different form from when we last met...'"
    ]

links = [
    {"Seize control.":1}
    ,{"Break camp and head towards it!":3, "Sleep in a little longer...":2}
    ,{"Break camp and head towards the tower.":3}
    ,{"Investigate.":5, "Move on.":4}
    ,{"Go back and investigate (exhasperatedly)":5}
    ,{"Take the amulet and move on.":6}
    ,{"Plod on, maybe a little faster.":7, "Try to climb up the walls of the gully.":8}
    ,{"Count your luck (above the last guy), and get to the base of the tower.":9}
    ,{"Sheath your sword and continue to the base of the tower.":9}
    ,{"Enter.":10}
    ,{"Go north.":12, "Go south.":13}
    ,{"Go north.":12, "Go south.":13} # 11
    ,{"Go south.":11, "Go west.":13, "Cut down the tapestry.":15} #12
    ,{"Go east.":11, "Go west.":12, "Open the door":14} # 13
    ,{"Return to the hall.":13}
    ,{"Take the stair.":16}
    ,{"I am Sir Carthalion, come to slay you!":17, "I am... the wizard Deszmo! Look what I brought for your birthday. (show amulet)":18}
    ,{"Die.":-1}
    ,{"'You're welcome.'":-1}
    ]

running = True
page = 0

while running:

    print()
    print(pages[page])
    print()

    choices = []
    for i,choice in enumerate(links[page].keys()):
        print("("+str(i+1)+")", choice)
        choices.append(choice)

    selecting = True
    while selecting:
        select = input("> ") 
        try:
            select = int(select)
        except:
            print("Input must be a number.")
            continue

        if select > len(links[page].keys()) or select < 1:
            print("Input must be one of the available options.")
            continue

        selecting = False

    if links[page][choices[select-1]] == -1:
        print("GAME OVER. Play again if you wish.")
        break

    page = links[page][choices[select-1]]

        
        
        
