# Helper Functions
init python:
    def dropMusic(drags, drop):
            if not drop:
                print(drags[0])
                return
            return True

# RepairPy Minigame Screens
screen tutorial_minigame:
    add "bg interior_sketch.png"
    draggroup:
        drag:
            drag_name "box"
            child "Sound Off 10-15-22.png"
            xpos 100 ypos 100
            droppable False
            dragged dropMusic

        drag:
            drag_name "musicBox"
            child "Sound On with Notes 10-15-22.png"
            draggable False
            xpos 1000