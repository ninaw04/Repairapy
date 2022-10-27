# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Idol")
define a = Character("???")

image tutorial sprite = im.Scale("tutorial_girl_fullbody.png", 563, 1000)

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

    show eileen happy

    # These display lines of dialogue.

    a "Hello...?"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
