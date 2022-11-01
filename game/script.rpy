# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Idol", color="#f96995")
define a = Character("???", color="#a1785c")
define a2 = Character("Abigail Smith", color="#a1785c")

image tutorial sprite = "tutorial_girl.png"

image idol sprite = im.Scale("lvl1 pop star wip.png", 563, 1000)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg interior_sketch

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "*bell rings*"

    show tutorial sprite

    # These display lines of dialogue.

    # ACT 1: The First Encounter

label choices:
    a "Hello...?"

label choices1:
    menu:
        "Hello, how may I help you?":
            jump choices3
        "Hi.":
            jump choices1_a

label choices1_a:
    a "Is this that antique shop that fixes things?"
    jump choices2

label choices2:
    menu:
        "Yes, it is! How may I help you?":
            jump choices3
        "No, you got the wrong store.":
            jump choices2_a

label choices2_a:
    a "Oh, I'm sorry about that..."
    a "Wait a minute- this IS the store!"
    a "No need to lie about that... That's very mean of you."
    "-1 heart"
    jump choices3

label choices3:
    a "Can you help me fix my dolly please?"
    menu:
        "No":
            jump choices3_a
        "Of course, what do you need help with?":
            jump choices3_b

label choices3_a:
    a "Sorry for bothering you... it won't happen again."
    hide tutorial sprite
    "Failed Ending"
    return

label choices3_b:
    "She carefully hands you the doll."
    a "The kids at my school- I mean, my dolly was hurt really bad while protecting me."
    a "She REALLY needs help."
    jump choices4

label choices4:
    menu:
        #slightly altered this line to be shorter
        "No worries, I can heal her in no time!":
            jump choices5
        "How can a doll protect you? It's just a doll.":
            jump choices4_a

label choices4_a:
    a "Yeah... I guess so..."
    a "But Dolly has always been there for me."
    jump choices5

label choices5:
    a "I want to thank you for taking time with my dolly. I don't know what I'd do without her..."
    a "I'm grateful there are people like you who can help me!"
    menu:
        "What's your dolly's name?":
            jump choices5_a
        "Where are your parents?... Can't they fix it for you?":
            jump choices5_b

label choices5_a:
    a "Her name is Princess Coraline! The one and only!"
    menu:
        "And who may court by her side?":
            a2 "It is me of course! Abigail Smith, the strongest knight there is!"
            a2 "Well, at least I try to be."
            menu:
                "Abigail? What a lovely name to have.":
                    a2 "Thank you... it really means a lot to me."
                    "+1 heart"
                    #comment out this return when continuing code
                    return

label choices5_b:
    a "Well, they don't know I'm here."
    a "Though I doubt they'd care..."
    a "It's okay, though. I'm fine! Princess Caroline keeps me company."
    menu:
        "Princess Caroline?":
            "My dolly's name! She is a princess from a far away kingdom..."
            menu:
                "What is your name then?":
                    a2 "My name is Abigail Smith..."
                    #comment out this return when continuing code
                    return

# This ends the game.
return
