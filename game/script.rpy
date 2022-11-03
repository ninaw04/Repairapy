# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("???", color="#a1785c", image="tutorial_girl")
define i = Character("Idol", color="#f96995", image="pop_star.png")

image tutorial sprite = "tutorial_girl.png"

image idol sprite = im.Scale("lvl1 pop star wip.png", 563, 1000)


# Variables we may need


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
    a curious "Hello...?"

label choices1:
    menu:
        "Hello, how may I help you?":
            jump choices3
        "Hi.":
            jump choices1_a

label choices1_a:
    a curious "Is this that antique shop that fixes things?"
    jump choices2

label choices2:
    menu:
        "Yes, it is! How may I help you?":
            jump choices3
        "No, you got the wrong store.":
            jump choices2_a

label choices2_a:
    a sad "Oh, I'm sorry about that..."
    a curious "Wait a minute- this IS the store!"
    a annoyed "No need to lie about that... That's very mean of you."
    "-1 heart"
    jump choices3

label choices_common:
    a neutral "Can you help me fix my dolly please?"

# This ends the game.
return
