# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("???", color="#a1785c", image="tutorial_girl")
define i = Character("Idol", color="#f96995", image="pop_star.png")

image tutorial sprite = im.Scale("tutorial_girl neutral.png", 440, 709)

image idol sprite = im.Scale("lvl1 pop star wip.png", 563, 1000)

image table = "bigtable.png"

image broken doll = im.Scale("doll_broken_full.png", 200, 400)


# Variables we may need
transform hop:
    linear 0.5 yoffset -150
    linear 0.5 yoffset 0


# The game starts here.

label start:
    play music "music/Night-in-Venice.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg interior_sketch

    # Testing purposes :D
    # jump tutorial_minigame

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play sound "audio/doorbell.wav"
    "*bell rings*"

    show tutorial sprite:
        xalign 0.5
        yalign 0.75
    show table:
        yalign 1.0

    # These display lines of dialogue.

    # ACT 1: The First Encounter


label choices1:
    a curious "Hello...?"
    menu:
        "Hello, how may I help you?":
            jump choices2
        "Hi.":
            jump choices2

label choices2:
    a curious "Is this that antique shop that fixes things?"
    menu:
        "Yes, it is! How may I help you?":
            jump choices2_common
        "No, you got the wrong store.":
            jump choices2_a

label choices2_a:
    a sad "Oh, I'm sorry about that..."
    show tutorial sprite at hop
    a curious "Wait a minute- this IS the store!"
    a annoyed "No need to lie about that... That's very mean of you."
    "-1 heart"
    jump choices2_common

label choices2_common:
    show broken doll:
        xalign 0.40
        yalign 0.75
    a neutral "Can you help me fix my dolly please?"
    menu:
        "Of course, what do you need help with?":
            jump choices3
        "No":
            jump ending1

label ending1:
    show tutorial sprite sad
    a sad "Sorry for bothering you... it won't happen again"
    hide tutorial sprite
    "Failed Ending"
    return

label choices3:
    a sad "The kids at my school- I mean, my dolly was hurt really bad protecting me. She REALLY needs help."
    menu:
        "It appears that she has been injured really badly... no worries though, she will be healed in no time.":
            jump choices4
        "How can a doll protect you? It's just a doll.":
            a sad "Yeah... I guess so, but Dolly has always been there for me..."
            jump choices4

label choices4:
    a neutral "I want to thank you for taking time with Dolly. I don't know what I'd do without her."
    a happy "I'm grateful there are people like you who can help me!"
    menu:
        "What's your dolly's name?":
            a neutral "Her name is Princess Coraline! The one and only!"
            menu:
                "And who may court by her side?":
                    a happy "It is me of course! Abigail Smith, the strongest knight there is!"
                    a neutral "Well, at least I try to be."
                    menu:
                        "Abigail? What a lovely name.":
                            a curious "Thank you... it really means a lot to me."
                            "+1 heart"
                            jump cutscene1
        "Where are your parents? ...Can't they fix it for you?":
            a annoyed "Well, they don't know I'm here."
            a sad "...Though I doubt they'd care."
            "-1 heart"
            a sad "..."
            a happy "I'ts okay though, I'm fine! Princess Caroline keeps me company."
            menu:
                "Princess Caroline?":
                    a neutral "My dolly's name! She is a princess from a far away kingdom."
                    menu:
                        "What is your name then?":
                            a neutral "My name is Abigail..."
                            jump cutscene1

label cutscene1:
    #add cutscene here later
    jump choices5

label choices5:
    "What... was that?"
    menu:
        "How long have you had Princess Caroline?":
            a neutral "I've had Princess Caroline since 4th grade. Out of all my toys, Princess Caroline is my favorite."
            menu:
                "You must love her a lot.":
                    "+1 heart"
                    a happy "I do love her!"
                    a sad "Mommy and daddy are too busy to play with me sometimes... That's why they always buy me toys."
                    a neutral "It's okay though, I don't need any other toys. Just her."
                    jump choices6
                "You sure are spoiled, huh?":
                    "-1 heart"
                    a horrified "That's what I always hear from others too... It's not like that at all!"
                    a sad "Mommy and daddy are just too budy to play with me, that's the only reason why I have so many toys..."
                    a annoyed "But I don't care for them! Just princess."
                    jump choices6

label choices6:
    menu:
        "How did she rip?":
            jump choices7
        "What happened to her?":
            jump choices7

label choices7:
    a sad "She got hurt... really badly... she was trying to protect me."
    menu:
        "C'mon, am I really supposed to believe that?":
            "-1 heart"
            a annoyed "It's true! There were monsters out to get me, but Princess Caroline stopped the enemies before they could hurt me."
            a sad "I couldn't protect her though... I failed as her knight and friend."
            menu:
                "She's just a doll, she can't do anything.":
                    jump choices8
        "Protect you?":
            a horrified "It all happened so fast..."
            a horrified "I was running away from these mean monsters and I couldn't escape. I didn't know what to do!"
            a happy "Princess Caroline helped me! She stopped the monsters from getting me."
            a sad "...But she got hurt in the process."
            a sad "I failed... I failed as a knight and friend."
            menu:
                "You and Princess Coraline couldn't do much, it seems like a tough situation here.":
                    jump choices8

label choices8:
    a curious "That's the thing, she didn't need to do anything!"
    a sad "I was supposed to protect her... me! I'm the knight, she shouldn't be in danger like that."
    a sad "I lost my only friend."
    menu:
        "You can try moving on...":
            "-1 heart"
            a horrified "How can you say that? It's not that easy, you know?"
            jump checkpoint
        "Let's try fixing her before saying anything else.":
            "+1 heart"
            a neutral "You're right... Someone told me before that a strong heart can heal anything!"
            a sad "Thank you... I'm just scared of losing her."
            jump checkpoint

label checkpoint:
    #check hearts to continue/ end game


label tutorial_minigame:
    call screen tutorial_doll

# This ends the game.
return
