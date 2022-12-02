# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('[Abigail]', color="#a1785c", image="tutorial_girl")
define i = Character("Idol", color="#f96995", image="pop_star.png")
define doll = Character("Princess Caroline", image = "doll_broken_full.png")
define random = Character("Random")
define other random = Character("Other Random")
define parents = Character("Parents")
define Mother = Character("Mother")
define Father = Character("Father")
default tool = "no tool"


#resizing images
image tutorial_girl neutral = im.Scale("tutorial_girl neutral.png", 440, 709)
image tutorial_girl happy = im.Scale("tutorial_girl happy.png", 440, 709)
image tutorial_girl happy_eyesclosed = im.Scale("tutorial_girl happy eyesclosed.png", 440, 709)
image tutorial_girl sad = im.Scale("tutorial_girl sad.png", 440, 709)
image tutorial_girl shocked = im.Scale("tutorial_girl shocked.png", 440, 709)

image a neutral = im.Scale("side tutorial_girl_neutral.png", 350, 350)
image a happy = im.Scale("side tutorial_girl_happy.png", 350, 350)
image a happy_eyesclosed = im.Scale("side tutorial_girl_happy_eyesclosed.png", 350, 350)
image a sad = im.Scale("side tutorial_girl_sad.png", 350, 350)
image a shocked = im.Scale("side tutorial_girl_shocked.png", 350, 350)


define i = Character("Idol", color="#f96995", image="pop_star.png")
image idol sprite = im.Scale("lvl1 pop star wip.png", 563, 1000)


image table = "bigtable.png"
image broken doll = im.Scale("doll_broken_full.png", 200, 400)


# Variables we may need
define is_currently_minigame = False

transform hop:
    linear 0.5 yoffset -150
    linear 0.5 yoffset 0


# The game starts here.

label start:

    $ hearts = 0
    $ Abigail = "???"


    scene bg interior

    # Testing purposes :D
    # jump tutorial_minigame_assembly

    play music "music/Night-in-Venice.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg interior

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
        a neutral "Hello...?"
        menu:
            "Hello, how may I help you?":
                jump choices2
            "Hi.":
                jump choices2

    label choices2:
        a neutral "Is this that antique shop that fixes things?"
        menu:
            "Yes, it is! How may I help you?":
                jump choices2_common
            "No, you got the wrong store.":
                jump choices2_a

    label choices2_a:
        a sad "Oh, I'm sorry about that..."
        show tutorial_girl shocked at hop
        a shocked "Wait a minute- this IS the store!"
        a sad "No need to lie about that... That's very mean of you."
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
                # jump choices4
                jump tutorial_minigame_assembly
            "How can a doll protect you? It's just a doll.":
                a sad "Yeah... I guess so, but Dolly has always been there for me..."
                # jump choices4
                jump tutorial_minigame_assembly

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
                                a neutral "Thank you... it really means a lot to me."
                                show tutorial_girl happy_eyesclosed
                                "+1 heart"
                                $ hearts += 1
                                jump cutscene1
            "Where are your parents? ...Can't they fix it for you?":
                a sad "Well, they don't know I'm here."
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
                        a shocked "That's what I always hear from others too... It's not like that at all!"
                        a sad "Mommy and daddy are just too budy to play with me, that's the only reason why I have so many toys..."
                        a neutral "But I don't care for them! Just princess."
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
                a shocked "It's true! There were monsters out to get me, but Princess Caroline stopped the enemies before they could hurt me."
                a sad "I couldn't protect her though... I failed as her knight and friend."
                menu:
                    "She's just a doll, she can't do anything.":
                        jump choices8
            "Protect you?":
                a shocked "It all happened so fast..."
                a shocked "I was running away from these mean monsters and I couldn't escape. I didn't know what to do!"
                a happy "Princess Caroline helped me! She stopped the monsters from getting me."
                a sad "...But she got hurt in the process."
                a sad "I failed... I failed as a knight and friend."
                menu:
                    "You and Princess Coraline couldn't do much, it seems like a tough situation here.":
                        jump choices8

    label choices8:
        a neutral "That's the thing, she didn't need to do anything!"
        a sad "I was supposed to protect her... me! I'm the knight, she shouldn't be in danger like that."
        a sad "I lost my only friend."
        menu:
            "You can try moving on...":
                show tutorial_girl sad
                "-1 heart"
                $ hearts -= 1
                a shocked "How can you say that? It's not that easy, you know?"
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
        a sad "You know what? It's okay, I can try fixing Princess Caroline myself. Sorry for wasting your time..."
        hide tutorial sprite
        "Failed Ending"
        return

label act2:
    #act2 starts here
    "She comes from a faraway kingdom… a kingdom you don’t know about (it’s a secret)!!"
    a sad "Well… the princess was always lonely in her tower… the king would work all night while the queen was away playing."
    show tutorial_girl sad
    a sad "The villagers in her kingdom are scared of her because of a curse"
    menu:
        "A curse?":
            a sad "YES! A curse placed on her by the queen herself. Poor Princess Caroline… all alone with no one to love. Not even the King can save her.." 
            "Is there a reason why?"

label act2Sel9: 
    menu:
            "What about the monsters from earlier?"
            "You have quite the imagination":
                jump selection9a

label selection9a:   
        a sad "Yeah, that’s what the adults say too… I try to explain to them, I tried so hard; they all tell me that I’m lying or that it’s all in my head"
        menu:
            "Is it?":
                show tutorial_girl sad
                "-1 heart"
                $ hearts -= 1
            "Why would they say that?"

        
label selection9b:   
        a sad "The adults… they should know..! They saw the monsters and they knew of the curse. I don’t know why they don’t believe me… "

label selection9:   
        a sad "The monsters are the worst. Everyday the Princess gets hurt, every day I fail to protect her"
        menu:
            "Do the adults help you?":
                a sad "No… the adults are the villains"
            "Villains?":
                # a neutral "They’re horrible… even worse than the monsters. They know about the monsters… they know of the queen’s curse… every day the Princess is hurting and every day they [adults] are watching."
                a neutral "They’re horrible… even worse than the monsters. They know about the monsters… they know of the queen’s curse… every day the Princess is hurting and every day the adults are watching."
        menu:
            "You probably deserve it":
                jump selction10a
            "That’s not nice of them to behave this way":
                show tutorial_girl happy
                "+1 heart"
                $ hearts += 1
                jump selection10b

label selection10a:
        a sad "Really? Does Princess Caroline deserve all the hurt?"
        menu:
            "Yes":
                "-1 heart"
                $ hearts -= 1
            "No, she doesn't"
    
label selection10b:
        a sad " I don’t know why everyone is so mean to me and princess…"
        a sad " What did she do to deserve all of this?"
        menu:
            "She doesn’t deserve it, at all"
            "Probably something you did":
                "-1 heart"
                $ hearts -= 1


label badEndingRoute:
    if hearts < 2:
        a neutral "...."
        a neutral "something… I… did?"
        a neutral "oh..."
        menu:
            "I mean… yeah… haven’t you always questioned it?":
                jump badChoice1A
            "People don’t bully for no reason":
                jump badChoice1B

label badChoice1A:
    a sad "Well… part of me was hoping… I was wrong"
    a sad "Sorry… haha… it was a silly thought"
    a sad "..."
    a sad " I just wanted to be saved…"
    menu:
        "Be honest, you’re the reason why the doll is broken? ":
            jump badChoice2A
        "Yeah, it’s really pathetic looking for help from a stranger of all people":
            jump badChoice2B

label badChoice1B:
    a sad "They… don’t…"
    a sad "..."
    a sad "I’m sorry…. I’m really sorry…."
    a sad "I…you’re right.. There’s a reason for everything"
    a sad " All I wanted was to be saved…"
    menu:
        "You’re pathetic aren’t you? Looking for help from a worker. I don’t know you":
            jump badChoice2B
        "There’s a reason why the doll is broken, it’s your fault":
            jump badChoice2A

label badChoice2A:
    a sad " … No…! You’re wrong… she’s not hurt because of me "
    a sad "She wouldn’t blame me..! She understands why I can’t save her this time… right?"
    a sad "…. Princess Caroline? You understand, right?"
    doll "..."
    a sad " I’m sorry! I’m sorry, okay? What more do you want from me?"
    a sad " … Princess Caroline?"
    menu:
        "Who got you the doll again, Abigail?":
            pass
        "Tell me again, so your doll was bought by your parents?"

label badChoice2B:
    a sad " … pathetic?"
    a sad " I’m… pathetic?"
    a sad "… Princess Caroline doesn’t think I am. Right, Princess Caroline?"
    doll "..."
    a sad " You… too? Not you too Princess Caroline…"
    a sad "I’m sorry… I’m so sorry… What do I do now? What do you want from me?"
    a sad " … Princess Caroline?"
    menu:
        "Tell me again, so your doll was bought by your parents?":
            jump badChoice3C
        "Who got you the doll again, Abigail?":
            jump badChoice4C

    
label badChoice3C:
    a sad "…. My parents did buy me her.."
    a sad "…. But… I don’t know why that’s important…"
    menu:
        "You don’t see it at all?":
            jump badChoice3A
        "Are you that dumb?":
            jump badChoice3B

label badChoice3A:
    a sad "….."
    a sad "Oh… you’re right…"
    a sad "I…I’m sorry"
    a sad "I guess they did buy me… princess..caroline"
    a sad " I am ungrateful "
    menu:
        "The bullies too, they have a reason":
            jump badChoice4C

label badChoice4C:
    a sad"Why… Do you keep saying that??"
    a sad "..." 
    a sad "Oh..! I see "
    a sad "I understand what you mean now…"
    a sad "Everything that had happened… every pain I felt" 
    a sad "It all happened for a reason"
    a neutral "Thank you… fixer… I finally understand"
    a neutral "*she pays and leaves*"
    hide tutorial_girl
    hide broken doll
    "few days later"
    "*bell chimes*"

    random "Have you seen our daughter?"
    other random "Abigail?? Abigail Smith?? She was last seen leaving this shop."
    parents "We’re her parents.. Our daughter never came home that day."
    parents "Please… we need to find our precious daughter."
    Mother "She’s been missing for days and the police are utterly useless."
    Father "Do you know why she was here?"
    menu:
        "She came to fix her doll.":
            pass
        "I just did my job."
    Father "Please… if you see her.. Call us."

    Mother "Oh please.. Let her be safe."

    Father "Sorry for interrupting you and your work... we won’t bother you anymore."






label tutorial_minigame_assembly:
    $ is_currently_minigame = True
    show tutorial_girl neutral:
        xalign 0.85
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.6

    # a "testing"
    $ tool = ""
    call screen tutorial_doll
    $ is_currently_minigame = False
    show tutorial_girl neutral:
        xalign 0.5
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.75
    jump choices4
    # jump choices8

label tutorial_minigame_coloring:

# This ends the game.
return
