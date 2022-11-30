﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('[Abigail]', color="#a1785c", image="tutorial_girl")

#resizing images
image tutorial_girl neutral = im.Scale("tutorial_girl neutral.png", 440, 709)
image tutorial_girl happy = im.Scale("tutorial_girl happy.png", 440, 709)
image tutorial_girl happy_eyesclosed = im.Scale("tutorial_girl happy_eyesclosed.png", 440, 709)
image tutorial_girl sad = im.Scale("tutorial_girl sad.png", 440, 709)
image tutorial_girl curious = im.Scale("tutorial_girl curious.png", 440, 709)
image tutorial_girl horrified = im.Scale("tutorial_girl horrified.png", 440, 709)
image tutorial_girl annoyed = im.Scale("tutorial_girl annoyed.png", 440, 709)

image a neutral = im.Scale("side tutorial_girl neutral.png", 350, 350)
image a happy = im.Scale("side tutorial_girl happy.png", 350, 350)
image a sad = im.Scale("side tutorial_girl sad.png", 350, 350)
image a curious = im.Scale("side tutorial_girl curious.png", 350, 350)
image a horrified = im.Scale("side tutorial_girl horrified.png", 350, 350)
image a annoyed = im.Scale("side tutorial_girl annoyed.png", 350, 350)


define i = Character("Idol", color="#f96995", image="pop_star.png")
image idol sprite = im.Scale("lvl1 pop star wip.png", 563, 1000)


image table = "bigtable.png"
image broken doll = im.Scale("doll_broken_full.png", 200, 400)


# Variables we may need
transform hop:
    linear 0.5 yoffset -150
    linear 0.5 yoffset 0


# The game starts here.

label start:

    $ hearts = 0
    $ Abigail = "???"

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

    show tutorial_girl:
        xalign 0.5
        yalign 0.75
    show table:
        yalign 1.0

# ACT 1: The First Encounter  
label act1:
    # These display lines of dialogue.

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
        show tutorial_girl horrified at hop
        a horrified "Wait a minute- this IS the store!"
        a annoyed "No need to lie about that... That's very mean of you."
        show tutorial_girl sad
        "-1 heart"
        $ hearts -= 1
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
                        $ Abigail = "Abigail Smith"
                        a happy "It is me of course! Abigail Smith, the strongest knight there is!"
                        a neutral "Well, at least I try to be."
                        menu:
                            "Abigail? What a lovely name.":
                                a curious "Thank you... it really means a lot to me."
                                show tutorial_girl happy_eyesclosed
                                "+1 heart"
                                $ hearts += 1
                                jump cutscene1
            "Where are your parents? ...Can't they fix it for you?":
                a annoyed "Well, they don't know I'm here."
                a sad "...Though I doubt they'd care."
                show tutorial_girl sad
                "-1 heart"
                $ hearts -= 1
                a sad "..."
                a happy "I'ts okay though, I'm fine! Princess Caroline keeps me company."
                menu:
                    "Princess Caroline?":
                        a neutral "My dolly's name! She is a princess from a far away kingdom."
                        menu:
                            "What is your name then?":
                                $ Abigail = "Abigail Smith"
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
                        show tutorial_girl happy_eyesclosed
                        "+1 heart"
                        $ hearts += 1
                        a happy "I do love her!"
                        a sad "Mommy and daddy are too busy to play with me sometimes... That's why they always buy me toys."
                        a neutral "It's okay though, I don't need any other toys. Just her."
                        jump choices6
                    "You sure are spoiled, huh?":
                        show tutorial_girl sad
                        "-1 heart"
                        $ hearts -= 1
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
                show tutorial_girl sad
                "-1 heart"
                $ hearts -= 1
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
                show tutorial_girl sad
                "-1 heart"
                $ hearts -= 1
                a horrified "How can you say that? It's not that easy, you know?"
                jump checkpoint1
            "Let's try fixing her before saying anything else.":
                show tutorial_girl happy_eyesclosed
                "+1 heart"
                $ hearts += 1
                a neutral "You're right... Someone told me before that a strong heart can heal anything!"
                a sad "Thank you... I'm just scared of losing her."
                jump checkpoint1

label checkpoint1:
    #check hearts to continue/ end game
    if hearts >= 0:
        jump act2
    else:
        a annoyed "You know what? It's okay, I can try fixing Princess Caroline myself. Sorry for wasting your time..."
        hide tutorial sprite
        "Failed Ending"
        return

label act2:
    #act2 starts here
    "She comes from a faraway kingdom… a kingdom you don’t know about (it’s a seret)!!"
    a sad "Well… the princess was always lonely in her tower… the king would work all night while the queen was away playing."
    show tutorial_girl sad
    a sad"The villagers in her kingdom are scared of her because of a curse"
     menu:
            "A curse?":

   a sad "YES! A curse placed on her by the queen herself. Poor Princess Caroline… all alone with no one to love. Not even the King can save her.." 
    menu:
            "A curse?"
            "Is there a reason why?"

label act2Sel9: 
      menu:
            "What about the monsters from earlier?"
            "You have quite the imagination":
                jump selction9a

label selection9a:   
        a sad "Yeah, that’s what the adults say too… I try to explain to them, I tried so hard; they all tell me that I’m lying or that it’s all in my head"
        menu:
            "Is it?"
                show tutorial_girl sad
                "-1 heart"
                $ hearts -= 1
            "Why would they say that?"

        
label selection9b:   
        a sad "The adults… they should know..! They saw the monsters and they knew of the curse. I don’t know why they don’t believe me… "

label selection9:   
        a sad "The monsters are the worst. Everyday the Princess gets hurt, every day I fail to protect her"
        menu:
            "Do the adults help you?"
        a sad "No… the adults are the villains"
        menu:
            "Villains?"
        
        a neutral "They’re horrible… even worse than the monsters. They know about the monsters… they know of the queen’s curse… every day the Princess is hurting and every day they [adults] are watching."
         menu:
            "You probably deserve it":
                jump selction10a
            "That’s not nice of them to behave this way"
                show tutorial_girl happy
                "+1 heart"
                $ hearts += 1
                jump selction10b

label selection10a:
        a sad "Really? Does Princess Caroline deserve all the hurt?"
            menu:
                "Yes"
                    "-1 heart"
                    $ hearts -= 1
                "No, she doesn't"
    
label selection10b:
        a sad " I don’t know why everyone is so mean to me and princess…"
        a sad " What did she do to deserve all of this?"
            menu:
                "She doesn’t deserve it, at all"
                "Probably something you did"
                    "-1 heart"
                    $ hearts -= 1









label tutorial_minigame:
    show tutorial sprite:
        xalign 0.85
        yalign 1.0
    # minigame_window show
    call screen tutorial_doll

# This ends the game.
return
