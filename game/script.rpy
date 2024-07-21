
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('[Abigail]', color="#cf850d", image="a", who_outlines=[(3, "#6b301c", 1, 1)])
define i = Character("Idol", color="#f96995", image="pop_star.png")
define doll = Character("Princess Caroline", image = "doll/doll_broken_full.png")
define random = Character("Random")
define friend = Character("Friend", color="#e02589d8", who_outlines=[(3, "#450756", 1, 1)])
define other_random = Character("Other Random")
define parents = Character("Parents")
define father = Character("Father",color="#113799", who_outlines=[(3, "#121c57", 1, 1)])
define mother = Character("Mother",color="#2b8939", who_outlines=[(3, "#0e4338", 1, 1)])
define unknown = Character("???",color="#113799", who_outlines=[(3, "#121c57", 1, 1)])
define unknown2 = Character("???",color="#2b8939", who_outlines=[(3, "#0e4338", 1, 1)])
default tool = "no tool"

# NVL characters are used for the phone texting
define p_nvl = Character("Me", kind=nvl, callback=Phone_SendSound)
define f_nvl = Character("Friend", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#resizing images
image a neutral = im.Scale("tutorial_girl_neutral.png", 440, 709)
image a happy = im.Scale("tutorial_girl_happy.png", 440, 709)
image a happy_eyesclosed = im.Scale("tutorial_girl_happy_eyesclosed.png", 440, 709)
image a sad = im.Scale("tutorial_girl_sad.png", 440, 709)
image a shocked = im.Scale("tutorial_girl_shocked.png", 440, 709)
image a relaxed = im.Scale("tutorial_girl_relaxed.png", 440, 709)

#image a neutral = im.Scale("side tutorial_girl_neutral.png", 350, 350)
#image a happy = im.Scale("side tutorial_girl_happy.png", 350, 350)
#image a happy_eyesclosed = im.Scale("side tutorial_girl_happy_eyesclosed.png", 350, 350)
#image a sad = im.Scale("side tutorial_girl_sad.png", 350, 350)
#image a shocked = im.Scale("side tutorial_girl_shocked.png", 350, 350)

#image tutorial_girl neutral = im.Scale("tutorial_girl neutral.png", 440, 709)
#image tutorial_girl happy = im.Scale("tutorial_girl happy.png", 440, 709)
#image tutorial_girl happy_eyesclosed = im.Scale("tutorial_girl happy eyesclosed.png", 440, 709)
#image tutorial_girl sad = im.Scale("tutorial_girl sad.png", 440, 709)
#image tutorial_girl shocked = im.Scale("tutorial_girl shocked.png", 440, 709)

define i = Character("Idol", color="#f96995", image="pop_star.png")
image idol sprite = im.Scale("lvl1 pop star wip.png", 563, 1000)


image table = "bigtable.png"
image broken doll = im.Scale("doll/doll_broken_full.png", 200, 400)





default heartCount = 0


# Variables we may need
define is_currently_minigame = False

    # starting at top left corner

init python:
    def inventoryUpdate(st):
        pass
    def inventoryEvents(event, x, y, at):
        pass
    def environmentEvents(event, x, y, at):
        pass

transform hop:
    linear 0.5 yoffset -150
    linear 0.5 yoffset 0

# function for displaying gained heart count within a horizontal box.
screen displayHearts(count):
    if(count > 0):
        hbox:
            for i in range(heartCount):
                add im.Scale("heart.png",100,100)

# overlay for the inventory for minigames
screen inventoryUI:
    zorder 1
    image "invetoryUI/inventory-icon-bg.png" xpos 0 ypos 0.8 at half_size
    imagebutton auto "inventoryUI/inventory-icon-%s.png" xpos 0.03 ypos 0.825 at half_size

screen inventory:
    image "inventoryUI/inventory"


transform half_size:
    zoom 0.5

# The game starts here.
label start:
    # $config.rollback_enabled = False
    python:
        environment_SM = SpriteManager(event=environmentEvents)
        inventory_SM = SpriteManager(update = inventoryUpdate, event = inventoryEvents)
        environment_sprites = []
        inventory_sprites = []
        environment_items = []
        inventory_items = []
        inventory_item_names = ["Needle", "Thread", "Glue"]
   
 
    $ heartCount = 0
    $ Abigail = "???"

    scene bg interior
    play music "music/Night-in-Venice.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg interior
    play sound "audio/doorbell.wav"
    pause 1.0

    show a neutral:
        xalign 0.5
        yalign 0.75
        alpha 0
        easein .5 alpha 1

    show table:
        yalign 1.0

    pause .5

# ACT 1: The First Encounter  
label act1:
    # These display lines of dialogue.
    label selection1:
        a neutral "Hello...?"
        menu:
            "Hello, how may I help you?":
                jump selection2
            "Hi.":
                label altSelection1:
                a neutral "Is this a store that fixes thing?"
                menu:
                    "Yes it is! How may I help you?":
                        jump selection2
                    "No, you got the wrong store":
                        label altSelection1B:
                            a sad "Oh... Sorry about that..."
                            pause 1
                            show a shocked at hop
                            a happy "Wait... this IS the store! Why did you lie to me? That's not very nice"
                            "-1 heart"          
                            $ heartCount -= 1
                            show screen displayHearts(heartCount)
                            
                            menu:
                                "Can't take a joke? LOL":
                                    a sad "Oh okay..."
                                    a sad "Anyways..."
                                    pause .5
        
    label selection2:
        a neutral "Can you please help me fix my friend? She's really hurt..."

        show box_v1 at left

        "{i}The girl pulls out a box, inside is a dismembered doll.{/i}"
        pause 
        show box_v1 at left
      
        menu:
            "I don't think so.":
                jump ending1
            "Of course, what fixes do you need help with?":
                jump selection3

    label selection3:
        a sad "She needs help with everything... She fought a long battle against the {b}monsters{/b} to protect me. Please help me... will you help me?"
        menu:
            "It appears that she has been injured really badly... no worries though, she will be healed in no time.":
                # jump choices4
                jump tutorial_minigame_assembly
            "How can a doll protect you? It's just a doll.":
                a sad "Yeah... I guess so, but she has always been there for me..."
                menu: 
                    "I guess that makes sense? I'll see what I can do.":
                        jump tutorial_minigame_assembly
                    "Yeah, I don't think I want to help you.":
                        jump ending1

    label selection4:
        a neutral "I want to thank you for helping my friend. I couldn’t protect her this time… I don’t know what I’d do without her"
        a happy "I'm grateful there are people like you who can help me!"
        menu:
            "What is your friend's name?":
                a happy_eyesclosed "You… Want to know about my friend? No one ever asks me about my friend!"
                "+1 heart"
                $ heartCount += 1
                show screen displayHearts(heartCount)
                a happy "Her name is Princess Caroline! The one and only!"
                menu:
                    "And who may be protecting her?":
                        $ Abigail = "Abigail"
                        a happy_eyesclosed "It is I! Abigail! The strongest knight to protect the princess!"
                        a neutral "Well, at least I try to be."
                        "{i}Abigail takes a moment to look at her doll on the table.{/i}"
                        a neutral "Princess Caroline still doesn’t look very good. Is she going to be okay?" 

            "You need to take better care of your doll then.":
                a sad "Doll? No no… she’s not a doll, she’s my friend. She’s Princess Caroline."
                a sad "...Though I doubt they'd care."
                "-1 heart"
                $ heartCount -= 1
                show screen displayHearts(heartCount)
                a sad "..."
                menu:
                    "What's your name then?":
                        a sad "... Abigail"
                        "{i}Abigail looks uncomfortable and bothered as she answers. Abigail takes another moment to look at her doll on the table.{/i}"

                        a neutral "Hey… Princess Caroline doesn’t look fixed at all."

    label selection5:
        menu:
            "It appears that I don’t have any parts for her eye.":
                a sad "Oh no..."
                a happy "Wait a minute! I have the eye!"
                "{i}Searching through her pocket, Abigail pulls out a single glass eye from the doll and presents it.{/i}"
                a happy_eyesclosed "Ta Da! Princess Caroline’s eyes! … Her wounds from protecting me."
                jump tutorial_minigame_eye
            "She’s going to have a missing eye forever lol.":
                a shocked "NO! Please don’t let that be true"
                show a sad
                "{i}Abigail starts to cry before pausing for a moment.{/i}"
                "{i}Searching through her pocket, Abigail pulls out a single glass eye from the doll and presents it.{/i}"
                a sad "There… Princess Caroline’s eye… Please add the eye for her. I can’t let her go."
                jump tutorial_minigame_eye

    label selection6:
        menu:
            "How long have you had your doll?":
                a sad "I’m telling you right now!!! Princess Caroline is not a doll! SHE IS MY FRIEND"
                "-1 heart"
                $ heartCount -= 1
                show screen displayHearts(heartCount)
                a sad "But.. um.. Mommy and daddy showed me Princess when I was little… I don’t know"

            "How long have you been friends with Princess Caroline for?":
                a happy "Mommy and Daddy gave me Princess Caroline when I was little! Out of all my friends, Princess Caroline is my favorite friend!"
    label selection7:
        menu:
            "You honestly seem lonely.":
                a sad "Lonely?"
                menu:
                    "Yeah do you have any friends at all?":
                        a shocked "No no no! You got it all wrong!"
                        a shocked "Mommy and daddy are too busy to play with me. I only get toys when I’m sad..."
                        a happy "I don't NEED friends! Princess Caroline is enough for me!"
                        pause 1
                        a sad "Am I lonely?"
                        "-1 heart"
                        $ heartCount -= 1
                        show screen displayHearts(heartCount)
            "You must love her a lot.":
                a happy "I do love her!! Mommy and daddy are too busy to play with me.. When I’m sad, another friend appears! I don’t need them though, only Princess!"
                "+1 heart"
                $ heartCount += 1
                show screen displayHearts(heartCount)
    label selection8:
        menu:
            "What happened to her?":
                pause 0
            "How did she rip?":
                pause 0
        a neutral "It happened so fast… I was running away from these mean {b}monsters{/b} and I couldn’t escape. I didn’t know what to do!"
        a happy "Until Princess Caroline {b}saved me…{/b} she stopped the evil monsters from getting me."
        a sad "...She got hurt though."
        a sad "I failed her… I failed to save her. I failed as her knight and friend."
        a sad "And now she’s gone…! I’m going to lose my best friend."
        menu:
            "Let’s try stitching her wounds before we say anything else":
                a happy "You’re right…! I don’t know why I’m sad yet! Princess Caroline is strong! She won’t let these monsters take her yet!"
                a neutral "Thank you…"
                "+1 heart"
                $ heartCount += 1
                show screen displayHearts(heartCount)
                jump tutorial_minigame_stich
            "You can buy another one":
                "How… Can you say that? Buy? I can’t buy another Princess Caroline, there’s only one friend... Please... Help her"
                "-1 heart"
                $ heartCount += 1
                show screen displayHearts(heartCount)
                menu:
                    "Okay":
                        jump tutorial_minigame_stich
                    "No, I dont think so":
                        jump ending1

label act2:
    label selection9:
        menu:
            "Can you tell me the story of Princess Caroline?":
                pause 0
            "Is there a reason why you're so attached to Princess Caroline?":
                pause 0
        a relaxed "Well… she comes from a faraway kingdom. Somewhere where no one knows."
        a neutral "The people in her kingdom were scared of her because of a curse."
    label selection10:
        menu:
            "A curse?":
                a neutral "YES! A curse placed by the queen herself.. I’m not sure what the curse is… but the queen made sure that everyone in the kingdom stayed away from the Princess."
                a sad "Poor Princess Caroline… She's all alone with no one to love. Even the King can’t save her. At least she has her best friend to keep company!"
                menu:
                    "Where's the king?":
                        a sad "The king is so busy! He’s doing his duty for his people that he forgets m-... the princess. Or maybe he hates the Princess too because of the curse too… I’m not sure."
                        menu:
                            "She probably deserved it":
                                a neutral "Really..? Do you think so too?"
                                "-1 heart"
                                $ heartCount -= 1
                                show screen displayHearts(heartCount)
                                a sad "I was hoping you’d understand me… it’s a silly thought really."

                            "Why do you think so?":
                                a neutral "I just know so! The king gets super sad at night and drinks magic potions to feel better. He’s probably upset at the princess… how she can’t be the perfect daughter for him."
            "A kingdom?":
                a neutral "Oh yeah! A kingdom full of people! With a place full of people, no one wants to get near the Princess."
                a sad "No one..."
                a happy_eyesclosed "Except me!"
                menu:
                    "Is there a reason?":
                        a relaxed "I already told you! The curse…! It’s a super duper bad curse.. But I don’t know what it does. All she knows is that the queen did it."
                    "There's probably a reason":
                        a sad "A reason? Why do you think that?"
                        "-1 heart"
                        $ heartCount -= 1
                        show screen displayHearts(heartCount)
                        a sad "I feel like you don't get me at all"
    jump tutorial_minigame_dress
    label selection11:
        pause 1.0
        a sad "I know the curse is bad... I know people avoid her because of it..."
        a sad "But sometime I wish everyone avoids us, it’s a lot better than the monsters."
        menu:
            "The monsters you’ve mentioned before?":
                a neutral "You… remembered?"
                "+1 heart"
                $ heartCount += 1
                show screen displayHearts(heartCount)
                a neutral "these monsters…. They’re the worst. I have to keep protecting Princess Caroline but the monsters won’t stop. They don’t want to stop. They went too far, hurting Princess Caroline though."
                menu:
                    "Is there anyone who can help you?":
                        a sad "No, no one can help me. The grownups are the villains too."
                        a sad "They’re horrible. Maybe worse than the monsters!! They know about the monsters and the curse. Everyday… the Princess is hurting and every day the villains just watch her hurt."
                        menu:
                            "Don't worry, I'll help you":
                                a happy "Really?"
                                a happy_eyesclosed "You're the best!"
                                jump goodEnding
                    "Sounds like a you problem":
                        a sad "What does that mean?"
                        "{i}Abigail thinks for a moment{/i}"
                        a sad "..."
                        a sad "Oh... it's my problem to deal with. Just like the grown ups would tell me."
                        jump badEnding
            "You have an active imagination.":
                a sad "yeah… that’s what they tell me too. I tell the grown ups but they think I’m lying or it’s in my head."
                menu:
                    "Yeah I’m siding with the adults here":
                        a shocked "You too?"
                        "-1 heart"
                        $ heartCount -= 1
                        show screen displayHearts(heartCount)
                        a shocked "..."
                        jump badEnding
                    "I think you're telling the truth":
                        a shocked "Really?"
                        "+1 heart"
                        $ heartCount += 1
                        show screen displayHearts(heartCount)
                        a happy_eyesclosed "That's the first time someone has said that to me!"
                        a happy "I guess there is a first time for everything"
                        a happy "Thank you..."
                        jump goodEnding



label ending1:
    hide box_v1
    a sad "Oh… I'm sorry for bothering you. It won't happen again.."
    show a:
        easein .5 alpha 0
    pause 2
    "{i}Phone rings{/i}"

    nvl_narrator "You have entered the chat"
    f_nvl "Hey! How's running the store?"
    p_nvl "ehh not bad ig"
    p_nvl "some kid came in wanting to get her doll fixed"
    f_nvl "Oh? How did it go?"
    p_nvl "idk turned her away lol"
    f_nvl "What? Why would you do that?"
    f_nvl "You know I haven't had anyone come into the store for a long time now..."
    f_nvl "Why would you turn her away from my business?"
    p_nvl "I'm sorry..."
    f_nvl "I thought you were my friend."
    f_nvl "Just close early. I'm done with you."

    
    pause 1
    "Failed Ending"
    pause 1
    jump closedCutscene

label selection8BadEnd:
    a shocked "No..? I thought you’re a fixer upper person. I thought you could help my friend… I thought you could {b}help me{/b}!"
    hide broken doll
    a sad "It’s okay then… I can try fixing Princess Caroline myself. Sorry I asked for help, you’re just like the other monsters..."
    
    show a:
        easein .5 alpha 0
    pause 1
    "Bad ending"
    jump closedCutscene


label badEnding:
    a happy "Thank you for fixing my doll…"
    a neutral "You've taught me a lot today."
    a neutral "Everything I ever did… everything that happened to me..."
    a relaxed "It happened for a reason."
    a relaxed "I was hoping someone out here would tell me \"It’s not your fault\" or even show kindness to me. "
    a relaxed "I don’t think it’ll happen."
    a sad "I don’t even know you… but you showed me it was my fault"
    a sad "It must be true right?"
    menu:
        "Yeah, it's true":
            pause 0
        "...":
            pause 0
    a sad "Princess Caroline doesn’t think so right?"
    a sad "…"
    a sad "You do Princess Caroline? No.. not you too…"
    a sad "Why is life so unfair to me? What did I ever do..."
    a sad "Thank you for fixing her… I don’t have much, but please take this $30"

    menu:
        "not enough":
            pause 0
        "it's actually $100":
            pause 0
    a sad "Oh... I should've known"
    a sad "Sorry... that's all I have."
    a sad "I need to go now... I don't know where to go though"
    pause 1
    hide broken doll
    show a:
        easein .5 alpha 0
    scene black
    pause 2
    "A few days later"
    scene bg interior
    play sound "audio/doorbell.wav"
    pause .5
    unknown "Have you seen our daughter?"
    menu:
        "Who?":
            pause 0
        "May I help you?":
            pause 0
    unknown2 "Abigail?? Abigail Smith?? She was last seen leaving this shop?"
    unknown "We’re her parents.. Our daughter never came home that day."
    father "Please… we need to find our precious daughter."
    mother "She’s been missing for days and the police are utterly useless!"
    father "Do you know why she was here?"
    menu:
        "She came to fix her doll":
            pause 0
        "I just did my job":
            pause 0
    father "Please... if you see her... Call us."
    mother "Oh please.. Let her be safe."
    father "Sorry for interrupting you and your works… we won’t bother you anymore"
    pause 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    play sound "audio/BadEndingReport.mp3"
    $ renpy.pause(35.0, hard=True)
    return

label goodEnding:
    a neutral "I don’t know why it’s so hard to trust people."
    a happy "You’ve been so kind to me… I don’t know why it’s so hard to trust people."
    a sad "I don’t know what I did to make people hate me"
    menu:
        "It's not your fault.":
            pause 0
        "There was nothing you could’ve done. People are just hateful":
            pause 0
    a neutral "You think so? But I don’t know who to go or what to do now."
    menu:
        "Would you like to start with your mommy and daddy?":
            a neutral "Do you think they’ll hate me?"
            menu:
                "No, not at all":
                    pause 0
                "I don't think mommy and daddy would want to see you hurt":
                    pause 0
            a neutral "… I could try..."
            a happy "Thank you for fixing Princess..."
            a relaxed "No.. Thank you for fixing my doll..."
            a happy "Princess Caroline will always be my friend and I’ll always be her knight..."
            a relaxed "But I want to just be me..."
            a neutral "I want to talk to mommy and daddy."
            a neutral "I don’t have much money.. Will $30 be okay?"
            menu:
                "Sure":
                    pause 0
                "That repair is at least $100. For the doll and my time":
                    a happy "That’s okay..! I’ll give you more tomorrow! Promise!"
                    menu:
                        "Promise":
                            pause 0
                        "Just playing with you!":
                            pause 0
    a happy "Thank you so much for fixing my doll and for talking to me…"
    a relaxed "I thought I would be alone forever… but you showed me it’s okay to open up."
    menu:
        "Of course Abigail":
            pause 0
        "I hope things will be okay Abigail":
            pause 0
    a happy_eyesclosed "Please, call me Abi!"
    a happy "I’ll be going now! I was supposed to be home for a while now!"
    pause 1
    hide broken doll
    show a:
        easein .5 alpha 0
    
    scene black
    pause 2
    "Next Day"
    scene bg interior
    pause 1.0
    play sound "audio/doorbell.wav"
    pause .5
    unknown "You must be the person who fixed our daughter’s toy right?"
    menu:
        "Abi? Yes I am, is there a problem":
            pause 0
    unknown2 "No no... There's no problem at all. We're her parents."
    mother "I just wanted to say… thank you for helping our daughter."
    father "I… We… didn’t know what our child was going through"
    mother "It’s so awful… I couldn’t believe it myself when she came to the kitchen crying."
    father "I’ve been taking overtime shifts, hoping to provide for the family. I thought money was all that was needed to be happy. I was wrong."
    father "All I did was consume work and that left me hurting the one precious person that mattered most to me"
    father "… Anyways… I know it wasn’t easy for her. Believing there was no one to help her"
    father "Thank you for opening your heart for her."
    mother "I didn’t know she had to face such… bullies because of me. When we found out, we fought with the parents and the school for letting this happen."
    mother "She’s moving school soon… it isn’t easy but a huge relief lifted off of her when she heard about"
    father "We know that even this… won’t heal our beautiful daughter."
    father "But… thank you. For giving her the courage to talk to us. We would never want her to be afraid of us."
    mother "I know she probably said so many horrible things about.. us."
    father "And I want to assure you that we are in the process of getting a divorce now."
    father "We probably should’ve done it sooner but we wanted our child to have a functioning family."
    mother "but functional was far from it"
    menu:
        "Where’s Abi?":
            pause 0
    father "She’s in therapy right now"
    mother "We’re on our way to pick her up, we just wanted to stop by to tell you thank you"
    father "And to give you a small tip for helping our daughter."
    "{i}Abi's father leaves $100 on the table {/i}"
    father "It might not be a lot, but we will recommend you over any shop there is in this town."
    mother "So… thank you"
    pause 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    return


label closedCutscene:
    pause 1.0
    scene black
    $ renpy.pause(1.0, hard=True)
    return
label tutorial_minigame_assembly:
    $ is_currently_minigame = True
    show a neutral:
        xalign 0.85
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.6

    $ tool = ""
    call screen tutorial_doll
    $ is_currently_minigame = False
    show a neutral:
        xalign 0.5
        yalign 0.75
    show broken doll:
        xalign 0.40
        yalign 0.75
    
    jump fragment0

label tutorial_minigame_eye:
    "eye minigame"
    jump fragment1
label tutorial_minigame_stich:
    "stitch minigame"
    jump fragment2
label tutorial_minigame_dress:
    "dress minigame"
    jump fragment3



label fragment0:
    scene black
    "{i}...Something weird is happening.{/i}"

    scene bg fragment1

    "{i}There's... kids in a plaground{/i}"

    scene bg fragment1a

    "{i}This... girl is on the ground and surrounded by other kids. She's covering her face.{/i}"
    "{i}And... her doll is broken{/i}"
    "{b}Princess...Caroline...{/b}"
    scene bg interior
    $ Abigail = "Abigail"
    show a happy:
        xalign 0.5
        yalign 0.75
    show table:
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.75
    "{i}What... was that?{/i}"
    jump selection4
label fragment1:
    scene black
    "{i}... this again{/i}"

    scene bg fragment1a

    "{i}Abigail is still hurt and on the ground...{/i}"
    scene
    scene bg fragment 2

    "{i}huh?{/i}"  
    "{i}This sudden change...{/i}"
    
    a "{i}I can't keep these monsters away...!{/i}"

    scene bg fragment 2a

    a "{i}I'm sorry...{/i}"
    
    $ renpy.pause()

    scene bg fragment 2b

    a "{b}Princess Caroline{/b}"
    
    scene bg interior
    $ Abigail = "Abigail"
    show a happy:
        xalign 0.5
        yalign 0.75
    show table:
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.75
    "{i}... am I seeing Abigail's visions?{/i}"
    jump selection6
label fragment2:
    scene black
    "{i}I see... a younger looking Abigail.{/i}"
    "{i}She's hugging her knees while two people are arguing in the background{/i}"
    unknown "I can't believe you did this again (REDACTED). How many times do we have to go through this?"
    unknown2 "Oh, please. Don't act like you're perfect. You're just as awful as me."
    unknown "Excuse me?"
    unknown2 "If you focused on the family more, maybe I wouldn't try to find someone else."
    unknown "Don't you DARE drag our Abi into your mess."
    unknown2 "HA! She's barely yours to begin with."
    "..."
    a "Oh... they're talking about me again..."
    a "...Do they fight because of me?"
    a "I don't know what to do to stop it..."
    "{i}Now her parents are going to her...?{/i}"
    "They're giving Abigail... a doll."
    "She smiles."
    scene bg interior
    $ Abigail = "Abigail"
    show a happy:
        xalign 0.5
        yalign 0.75
    show table:
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.75
    "{i}This is really weird.{/i}"
    jump act2
label fragment3:
    scene black
    "{i}Abigail is around other kids and their parents...{/i}"
    "{i}The parents are muttering amongst themselves{/i}"
    "{i}... and they pull their kids away from Abigail{/i}"
        
    scene bg interior
    $ Abigail = "Abigail"
    show a happy:
        xalign 0.5
        yalign 0.75
    show table:
        yalign 1.0
    show broken doll:
            xalign 0.40
            yalign 0.75
    
    "{i}Is this... like the curse?{/i}"
    jump selection11
# This ends the game.
return
