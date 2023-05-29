import time

#set a global variable for an easter egg
global rune
rune = False
#sets a global variable that will count the number of stages survived 
global stages_survived
stages_survived = 0

#sets two global variables that will be used in returning
#responses from functions to other functions
global catch_response_AB
catch_response_AB = "a"
global catch_response_ABC
catch_response_ABC = "a"

#sets three global constants that will be used in checking
#to make sure the user entered a valid argument
a_choice = "a"
b_choice = "b"
c_choice = "c"

#prints title
time.sleep(1.0)
print("""
 ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗                              
██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝                              
██║     ███████║██║   ██║██║   ██║███████╗█████╗                                
██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝                                
╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗                              
 ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                              
""")
time.sleep(1.0)
print("""
██╗   ██╗ ██████╗ ██╗   ██╗██████╗                                              
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗                                             
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝                                             
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗                                             
   ██║   ╚██████╔╝╚██████╔╝██║  ██║                                             
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
""")
time.sleep(1.0)
print("""                                         
 ██████╗ ██╗    ██╗███╗   ██╗                                                   
██╔═══██╗██║    ██║████╗  ██║                                                   
██║   ██║██║ █╗ ██║██╔██╗ ██║                                                   
██║   ██║██║███╗██║██║╚██╗██║                                                   
╚██████╔╝╚███╔███╔╝██║ ╚████║                                                   
 ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
""")
time.sleep(1.0)
print("""                                                                            
 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗   
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╗
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ╚═╝
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██╗
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗╚═╝
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝   
                                                    
                                                                                                                                                     
                                                                            
""")
time.sleep(1.25)
print("""
██╗  ██╗ █████╗ ██╗     ██╗      ██████╗ ██╗    ██╗███████╗███████╗███╗   ██╗   
██║  ██║██╔══██╗██║     ██║     ██╔═══██╗██║    ██║██╔════╝██╔════╝████╗  ██║   
███████║███████║██║     ██║     ██║   ██║██║ █╗ ██║█████╗  █████╗  ██╔██╗ ██║   
██╔══██║██╔══██║██║     ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══╝  ██║╚██╗██║   
██║  ██║██║  ██║███████╗███████╗╚██████╔╝╚███╔███╔╝███████╗███████╗██║ ╚████║   
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═══╝   
                                                                                
███████╗██████╗ ██╗████████╗██╗ ██████╗ ███╗   ██╗                              
██╔════╝██╔══██╗██║╚══██╔══╝██║██╔═══██╗████╗  ██║                              
█████╗  ██║  ██║██║   ██║   ██║██║   ██║██╔██╗ ██║                              
██╔══╝  ██║  ██║██║   ██║   ██║██║   ██║██║╚██╗██║                              
███████╗██████╔╝██║   ██║   ██║╚██████╔╝██║ ╚████║                              
╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")

#takes user name and uses it in intro to story
global name
name = str(input("What is your name, mortal? "))
def print_intro():
    print("""\n\tThe following tale entails you, """ +name+ """, as the protagonist and revolves around
    your encounters with a few especially spooky phenomenons that transpire in a realm now unknown to
    you, but that you will soon discover! Halloween holds the potential for incredible
    adventures, much danger... and terrible frights! Let's see how far you make it...""")


#calls function to print name and intro
print_intro()

#makes user press enter before continuing 
input("""\nPress Enter to continue... if you dare.
===========================================================================================================""")



#takes parameter from test_AB and evaluates which option, a or b,
#the user chose and returns True or False, which is used to
#determine which part to execute next 
def make_choice_AB(response = True):
    if response.lower() == a_choice:
        return True
    elif response.lower() == b_choice:
        return False
    else:
        print("Error to be excepted")
        raise Exception("Did_Not_Enter_A_or_B")

#is called by various parts of program, used to make sure user enters a valid response
#returns response to part that called it
def test_AB(Story_Stage_String):
    while True:
        try:
            choice = input(Story_Stage_String)
            global catch_response_AB
            catch_response_AB = make_choice_AB(choice)
        except Exception:
            print("You did not enter a valid response, try again")
            continue
        if catch_response_AB == True:
            catch_response_AB = a_choice
            return catch_response_AB
            break
        elif catch_response_AB == False:
            catch_response_AB = b_choice
            return catch_response_AB
            break
        else:
            print("error test_AB")

#called by various parts of programs, used to ensure that response entered is valid
#returns response to part that called it
def test_ABC(Story_Stage_String):
    while True:
        try:
            global catch_response_ABC
            catch_response_ABC = make_choice_ABC(Story_Stage_String)
        except Exception:
            print("You didn't enter a valid response, try again")
            continue
        if catch_response_ABC == a_choice:
            return catch_response_ABC
            break
        elif catch_response_ABC == b_choice:
            return catch_response_ABC
            break
        elif catch_response_ABC == c_choice:
            return catch_response_ABC
            break
        else:
            print("error test_ABC")
            

    
#takes the print statement of a part with three choices
#and returns the lowercase value of their choice
def make_choice_ABC(Story_Stage_String):
    response = input(Story_Stage_String)
    response.lower()
    if response == a_choice:
        return response
    elif response == b_choice:
        return response
    elif response == c_choice:
        return response
    else:
        print("Error to be excepted")
        raise Exception("Did_Not_Enter_A_B_or_C")

#First part of game, initiates game by making player choose which path they want to take
def Part_Ia():
    test_AB("""\n\tIt's Hallows' Eve, and you find yourself strolling down a
    cornfield on a hill. You spot the outline of a tall man, by the edge
    of the field.

    Do you:
    a.) Walk closer
    b.) Walk in another direction
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IIa()
    elif catch_response_AB == b_choice:
        Part_IIb()
    else:
        print("Error part Ia")

def Part_Ia_():
    test_AB("""\n\tThe outline of the tall figure by the edge
    of the field is still there.
    
    Do you:
    a.) Walk closer
    b.) Walk in another direction
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IIa()
    elif catch_response_AB == b_choice:
        Part_IIb()
    else:
        print("Error part Ia")

def Part_IIa():
    test_AB("""\n\tYou approach the figure, but something seems to be off...
    It's completely still. The closer you walk, the more details become clearer;
    the figure is actually posted on a tall pole, it's body looks fake. You come
    to realize that you're staring at a scarecrow, but no ordinary one at that.
    Once you are within 5 feet, the form, which is stuffed of hay, begins to stir.

    Do you:
    a.) Stay and watch more
    b.) Run back to the cornfield
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IIIa()
    elif catch_response_AB == b_choice:
        Part_IIIb()
    else:
        print("Error part IIa")

def Part_IIb():
    test_ABC("""\n\tDo you walk east, west, or south?
    a.) East
    b.) South
    c.) West
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_IIIc()
    elif catch_response_ABC == b_choice:
        Part_IIId()
    elif catch_response_ABC == c_choice:
        Part_IIIe()
    else:
        print("Error Part IIb")

def Part_IIb_():
    test_ABC("""\n\tDo you walk east, west, or south?
    a.) East
    b.) South
    c.) West
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_IIIc()
    elif catch_response_ABC == b_choice:
        print("You can't go home anymore, MWAHAHA!")
        Part_IIb_()
    elif catch_response_ABC == c_choice:
        Part_IIIe()
    else:
        print("Error Part IIb_")
        
def Part_IIIa():
    test_AB("""\n\tAs you watch the scarecrow, mystified by this strange phenomenon, it looks
    down at you. It's eyes are that of a human beings. It says "You are not in the human
    realm anymore, """ + name + """. This is world of Halloween." and gives a laugh like
    that of a cat trying to cough up a hairball.

    Do you:
    a.) Question the scarecrow 
    b.) Ditch this freaky conversation and try to get home
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IVa()
    elif catch_response_AB == b_choice:
        Part_IVb()
    else:
        print("Error Part IIIa")
        
def Part_IIIb():
    print("\n\tYou return to the cornfield.")
    global stages_survived
    stages_survived += 1
    Part_Ia()
    
def Part_IIIc():
    test_AB("""\n\tYou traverse the field for what seems like an eternity before
    finally coming across a run down barn.

    Do you:
    a.) Walk towards barn
    b.) Return back to the cornfield
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IVc()
    elif catch_response_AB == b_choice:
        Part_IVd()
    else:
        print("Error IIIc")
        
def Part_IIId():
    print("""\n\tYou decide to wuss out on Hallows' Eve and sprint back home, where
    you hide under the blanket in your bedroom until November 1st. Thanks for
    playing. Wuss...

    YOU WIN?""")
    
def Part_IIIe():
    test_AB("""\n\tYou take a hard left, clearly spooked by the unknown shadowy figure
    in the cornfield. The cornstalks gradually disappear as you find yourself in
    an open, moonlit clearing at the base of the hill.

    Do you:
    a.) Return to the cornfield
    b.) Investigate the clearing
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IVe()
    elif catch_response_AB == b_choice:
        Part_IVf()
    else:
        print("Error IIIe")
        
def Part_IVa():
    test_ABC("""\n\tDo you question:
    a.) How do I get home?
    b.) Ask what he means by the world of Halloween
    c.) Lose your marbles and start bawling
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_Va()
    elif catch_response_ABC == b_choice:
        Part_Vb()
    elif catch_response_ABC == c_choice:
        Part_Vc()
    else:
        print("Error Part_IV")
        
def Part_IVb():
    print("""\n\tYou return to the middle of the cornfield, but it feels different than before,
    the strange feeling that gripped you when you encountered the scarecrow remains still.""")
    global stages_survived
    stages_survived += 1
    Part_IIb_()

def Part_IVc():
    test_AB("""\n\tReaching the barn, you notice that the door is slightly ajar.

    Do you:
    a.) Run home
    b.) Go inside
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_Ve()
    elif catch_response_AB == b_choice:
        Part_Vd()
    else:
        print("Error IVc")
        
def Part_IVd():
    print("\n\tYou decide it's safer in the cornfield than in the clearing.")
    global stages_survived
    stages_survived += 1
    Part_Ia_()

def Part_IVe():
    print("\n\tYou decide it's safer in the cornfield than in the clearing.")
    global stages_survived
    stages_survived += 1
    Part_Ia_()

def Part_IVf():
    test_ABC("""\n\tYou take a look around the field and immediately notice something a
    bit strange... The ground is swathed in a gentle red light. You look up to the
    moon to realize that it is a crimson. Suddenly, a blood curdling howl erupts
    from behind.

    Do you:
    a.) Sprint ahead blindly
    b.) Turn around
    c.) Duck your head and cower like a baby
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_Vf()
    elif catch_response_ABC == b_choice:
        Part_Vg()
    elif catch_response_ABC == c_choice:
        Part_Vh()
    else:
        print("Error Part IVf")
        
def Part_Va():
    print("""\n\tThe scarecrow gives another chuckle, this one more like the low grumbling of thunder,
    "The only way back to your world now is to survive this place long enough...". He is cut off by
    a scream nearby. "You had better start running.", he says.""")
    global stages_survived
    stages_survived += 1
    Part_VIa()
    
def Part_Vb():
    print("""\n\tThe scarecrow responds, "Every year, on the night preceding Halloween, a gate opens
    connecting your realm to this one, a world where vicious monsters and other creatures run about
    and night is everlasting." """)
    global stages_survived
    stages_survived += 1
    Part_IVa()
    
def Part_Vc():
    print("""\n\tYou cry hysterically, and a titan-sized raven plucks you up and consumes you whole.

    GAME OVER""")
    
def Part_Vd():
    test_ABC("""\n\tYou enter the barn and walk into a cult gathering. Hiding
    behind a crate, you listen in on the cult's chant.

    Do you:
    a.) Leave           
    b.) Move in closer to observe the cult
    c.) Stay where you are
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_VIb()
    elif catch_response_ABC == b_choice:
        Part_VId()
    elif catch_response_ABC == c_choice:
        Part_VIc()
    else:
        print("Error Part_Vd")
        
def Part_Ve():
    print("""\n\tBeing the coward that you are, you dash home and cower behind
    mommy and daddy until you finally pass out from exhaustion. Can you
    believe you made it all this way just to run away from a door?

    YOU WIN?""")

def Part_Vf():
    test_ABC("""\n\tYou charge forward not caring what made that horrific sound,
    the only thing you care about is staying alive. The sound of heavy paws
    pounding the ground reaches you... There's something chasing you and
    it's gaining ground at an alarming rate. In seconds you feel that it is
    just on your tail.

    Do you:
    a.) Dive right
    b.) Dive left
    c.) Attempt a mid-stride roundhouse kick
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_VIe()
    elif catch_response_ABC == b_choice:
        Part_VIf()
    elif catch_response_ABC == c_choice:
        Part_VIg()
    else:
        print("Error Part Vf")
        
def Part_Vg():
    print("""\n\tYou quickly swivel around, expecting a beast from the depths of Hell,
    but find instead your parents... Holding your report card revealing all of your
    failing grades! There's F after F after F, and you foresee weeks of solidarity
    within the confines of your bedroom. Your social life coming to an end, you begin
    to dread the next year of isolation. Thanks for playing! Perhaps you should've
    focused more in class than on your phone. Don't worry! You'll have a year to think
    back on your mistakes.

    GAME OVER""")

def Part_Vh():
    print("""\n\tYou lie on the ground crying and sucking your thumb like the
    pathetic, crybaby that you are. You awake drenched in your own sweat
    and drool. Turns out it was just a really bad nightmare. You get an A+
    for failing. You're still a crybaby though.

    GAME OVER""")

def Part_VIa():
    print("\n\tYou run down the hill and enter an open, moonlit clearing at the base of the hill.")
    global stages_survived
    stages_survived += 1
    Part_IVf()
    
def Part_VIb():
    print("""\n\tDeciding it's not a good idea to stick around, you quietly
    leave the barn and go back into the cornfield.""")
    global stages_survived
    stages_survived += 1
    Part_Ia_()

def Part_VIc():
    print("""\n\tDeciding to stay and watch the cult preform their rituals,
    your eyes squint as a bright light emerges from a blood circle the
    cult is surrounding. Ghastly demons rush out of the hole and begin
    to kill the cult members. Attempting to run away, you get caught by
    a demon and are dragged into Hell where you spend eternity in suffering.
    This is what you get for hanging around a cult.

    GAME OVER""")

def Part_VId():
    print("""\n\tCuriosity calling you, you move up to a crate that's
    closer to the cult. Unfortunately for you, a cult member sneaks up
    behind you and grabs you. Thrown onto a stone block, the cult members
    surround you and cut into your chest, removing your organs as you lie
    there, bleeding out slowly as you watch your intestines being pulled out.
    Dying a slow and painful death, you wonder if it was really a good idea to
    get closer to a cult.
    
    GAME OVER""")

def Part_VIe():
    print("""\n\tYou dive to the right, right off the side of a small cliff and into a
    brier patch. You've definitely broken some bones, and you're bleeding all over.
    You slowly bleed to death.

    GAME OVER""")

def Part_VIf():
    print("""\n\tYou dive left... Right into a tree. Look what you got yourself into! Looking
    up from the ground, you find yourself face to face with a werewolf, fresh blood still
    drizzling from its muzzle. It makes a fine meal out of your scrawny flesh. Your story
    ends here.
    
    GAME OVER""")

def Part_VIg():
    test_AB("""\n\tWOW! Your leg actually connects... And it feels wet and furry. A person with
    a wolfish upper half is knocked aside, but loses its balance and tumbles off the side
    of a short cliff.
    
    Do you:
    a.) Run away
    b.) Jump down to finish it off
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_VIIa()
    elif catch_response_AB == b_choice:
        Part_VIIb()
    else:
        print("Error VIg")
        
def Part_VIIa():
    test_AB("""\n\tYou keep running until your lungs feel like they might burst.

    Do you:
    a.) Do you take a rest by a willow tree
    b.) Do you keep on going a little further
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_VIIIa()
    elif catch_response_AB == b_choice:
        Part_VIIIb()
    else:
        print("Error Part VIIa")
        
def Part_VIIb():
    print("""\n\tYou hit the ground hard and find your body covered in little spikes. You can't
    get up, and the werewolf quickly spots you. You're dead, good job trying to be tough though.

    GAME OVER""")

def Part_VIIIa():
    test_AB("""\n\tYou rest underneath an oddly comforting willow, and nod off for a little while.
    You wake up some time later, it's still pitch black, and you come to think that night
    doesn't end in this twisted dimension. You get a sense that someone is watching  you, but
    you have no clue where they are.

    Do you:
    a.) Sit still and carefully observe your surroundings
    b.) Get up and explore
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_IXa()
    elif catch_response_AB == b_choice:
        Part_IXb()
    else:
        print("Error Part VIIIa")
        
def Part_VIIIb():
    print("""\n\tYou quickly collapse to the ground, and your sight goes black. You wake up to the
    sound of a hair-raising cackle and a green, warty face. You're tied up and hanging over a
    cauldron filled of some boiling liquid. The witch throws her head back and releases one last
    laugh, and you descend into the broth. You die, but good job, you made it pretty far.
    
    GAME OVER""")

def Part_IXa():
    test_ABC("""\n\tYou remain underneath the willow, and scan your surroundings. Also immediately
    you notice a flash of color at the edge of your vision, and quickly look over. Deeper
    within the forest a short, hooded figure is visible.

    Do you:
    a.) Apprehend him/her
    b.) Stay put
    c.) Walk away
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_ABC == a_choice:
        Part_Xa()
    elif catch_response_ABC == b_choice:
        Part_Xb()
    elif catch_response_ABC == c_choice:
        Part_Xc()
    else:
        print("Error Part IXa")
        
def Part_IXb():
    print("""\n\tThe second you get up a headless man on a horse rushes past you...
    And it seems as though you're staring up at your own body, but from the ground...
    And your head is missing!
    You've been decapitated, and your head has been stolen by the headless horseman.
    Well, it looks like you finally got ahead of yourself.
    
    GAME OVER""")

def Part_Xa():
    print("""\n\tYou approach the figure...
    And realize it has vanished! You make one more step, and the next moment you're
    caught in a rope web suspended between two trees. A witch appears out of thin air,
    drags you to a lair hidden beneath the willow under which you were sleeping, and
    cooks you into a mysterious broth. The end.
    
    GAME OVER""")

def Part_Xb():
    test_AB("""\n\tYou remain still, watching the area where you had just seen the movement.
    Suddenly, a witch appears only a dozen feet in front of you, her dark eyes staring
    into yours with a deep hatred. You notice a circle made of oddly shaped stones circling
    the tree, and that the witch is just behind it, seemingly unable to cross.

    Do you:
    a.) Taunt her
    b.) Assume your safe and begin investigating the tree
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_XIa()
    elif catch_response_AB == b_choice:
        Part_XIb()
    else:
        print("Error Part Xb")
        
def Part_Xc():
    print("""\n\tYou decide you don't mess with shadowy figures lurking in dark forests,
    and head in the opposite direction. However, you step into quicksand that had been
    set up seemingly as a trap. You spend your last few moments drowning in sand and
    wondering why you didn't just stay home.
    
    GAME OVER""")

def Part_XIa():
    print("""\n\tYou stare right into the witches eyes and stick out your tongue.
    She gives you a nasty look and makes some symbol with her hands, but cries
    out in frustration when it doesn't work.""")
    global stages_survived
    stages_survived += 1
    Part_Xb()
    
def Part_XIb():
    test_AB("""\n\tYou check out the tree and notice a small crack in the roots of the
    tree closest to the trunk.

    Do you:
    a.) Pry open the root
    b.) Look around some more
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_XIIa()
    elif catch_response_AB == b_choice:
        Part_XIIb()
    else:
        print("Error Part XIb")
        
def Part_XIIa():
    test_AB("""\n\tWith an incredible struggle, you manage to force the root out of the ground,
    and discover an entire cavern filled with potions and elixirs of all sorts. One thing
    stands out, though; a luminescent gate that appears otherworldly (which is saying something
    after your experiences).

    Do you:
    a.) Pass through the gate
    b.) Continue exploring the cavern
____________________________________________________________________________________________________________\n""")
    global stages_survived
    stages_survived += 1
    if catch_response_AB == a_choice:
        Part_XIIIa()
    elif catch_response_AB == b_choice:
        Part_XIIIb()
    else:
        print("Error Part XIIa")
        
def Part_XIIb():
    print("""\n\tYou check out the tree some more and find an interesting rune embedded
    in the bark. You take it out and return to the root
____________________________________________________________________________________________________________\n.""")
    global rune
    rune = True
    global stages_survived
    stages_survived += 1
    Part_XIb()
    
def Part_XIIIa():
    print("""\n\tJust as you're passing through the gate, the witch bursts from the ceiling and charges
    you with a sharp stick in her hand. "Come here """ + name + """!", she screeches. You quickly step through, back into the world of the mortals.
    Good Job. You have survived Halloween...
    This year... MUAWHAHAHA!

    YOU WIN!""")

def Part_XIIIb():
    print("""\n\tAs you look around some more, the witch bursts forth from the cavern ceiling,
    impaling you with a wooden shank. You died, but survived far longer than expected.

    GAME OVER""")
    global rune
    rune = False

#calls first story stage which triggers chain reaction taking user through story
Part_Ia()

#tells user the conclusion of the story and how many rounds they survived
if rune == True:
    print("""After having returned safely to your own realm, you think back on all of the craziness
          and wonder if it was all just an oddly realistic dream. As you ponder this thought, your hand
          falls to your pocket. You find something round and hard there, quickly taking it out to
          see that it's the rune stone you had found by the old willow tree. It gives off an eerie
          phosphorescent light, and you realize that it was not a nightmare, but a twisted reality...""")
    print("You score is " + str(stages_survived) + " stages survived.")
elif rune == False:
    print("You score is " + str(stages_survived) + " stages survived.")
else:
    print("error")
