init python:

    def handle_snapping(drag):
        drag.draggable = False
        try:
            store.count = store.count + 1
        except:
            store.count = 1

    def joined_drags(drag):
        xDiff = hair.x - drag.x
        yDiff = hair.y - drag.y
        return [(hair, xDiff, yDiff), (drag, 0, 0)]

    def drag_placed(drags, drop):
        #check if the correct tool
        

        # if not drop or store.tool != "needle":
        #     return
        if not drop:
            return

        if drags[0].drag_name == "hair" and drop.drag_name == "headhb":
            head.snap(drop.x-45,drop.y-190)
            drags[0].snap(drop.x-33,drop.y-90)
            drags[0].bottom()
            head.draggable = False
            handle_snapping(drags[0])

        if drags[0].drag_name == "armL" and drop.drag_name == "armhb":
            drags[0].snap(drop.x-80,drop.y-40)
            # drags[0].bottom()
            handle_snapping(drags[0])

        if drags[0].drag_name == "armR" and drop.drag_name == "armhb":
            drags[0].snap(drop.x+167,drop.y-45)
            # drags[0].bottom()
            handle_snapping(drags[0])

        if drags[0].drag_name == "legL" and drop.drag_name == "leghb":
            drags[0].snap(drop.x+37,drop.y+152)
            drags[0].bottom()
            handle_snapping(drags[0])

        if drags[0].drag_name == "legR" and drop.drag_name == "leghb":
            drags[0].snap(drop.x+126,drop.y+152)
            drags[0].bottom()
            handle_snapping(drags[0])

        try:
            if store.count%5 ==0:
                return True
        except:
            pass
        return 

screen tutorial_doll:
    add 'bg tabletop.png'

    # use toolbar
    add minigameDragGroup

default armL = Drag(d = "images/doll/doll_broken_armL.png", drag_name = "armL", xpos = 150, ypos = 400, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
default armR = Drag(d = "images/doll/doll_broken_armR.png", drag_name = "armR", xpos = 150, ypos = 700, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
default hair = Drag(d = "images/doll/doll_broken_hair.png", drag_name = "hair", xpos = 110, ypos = 140, drag_raise = False, droppable = False, draggable = True, dragged = drag_placed)
default head = Drag(d = "images/doll/doll_broken_head.png", drag_name = "head", xpos = 100, ypos = 50, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed, drag_joined = joined_drags)
default torso = Drag(d = "images/doll/doll_broken_torso.png", drag_name = "torso", align=(0.35,0.50), drag_raise = True, droppable = False, draggable = False, dragged = drag_placed)
default legL = Drag(d = "images/doll/doll_broken_legL.png", drag_name = "legL", xpos = 450, ypos = 300, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
default legR = Drag(d = "images/doll/doll_broken_legR.png", drag_name = "legR", xpos = 450, ypos = 575, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
    
default headhb = Drag(d = "images/hitbox.png", drag_name = "headhb", align=(0.35,0.35), drag_raise = True, droppable = True, draggable = False)
default armhb = Drag(d = "images/hitbox.png", drag_name = "armhb", align=(0.35,0.50), drag_raise = True, droppable = True, draggable = False)
default leghb = Drag(d = "images/hitbox.png", drag_name = "leghb", align=(0.35,0.65), drag_raise = True, droppable = True, draggable = False)

default minigameDragGroup = DragGroup(armL, armR, hair, head, torso, legL, legR, headhb, armhb, leghb)