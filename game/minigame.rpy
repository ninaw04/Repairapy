init python:
    def drag_placed(drags, drop):
        if not drop:
            return
        
        if drags[0].drag_name == "head":
            drags[0].snap(drop.x-15,drop.y-215)

        try:
            store.count = store.count + 1
        except:
            store.count = 1

        if store.count ==5:
            return True
        
        drags[0].draggable = False
        return 

screen tutorial_doll:
    add 'bg tabletop.png'
    draggroup:
        drag:
            drag_name "armL"
            child "images/doll_broken_armL.png"
            xpos 100
            ypos 100
            droppable False
            draggable True
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "armR"
            child "images/doll_broken_armR.png"
            xpos 150
            ypos 100
            droppable False
            draggable True
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "head"
            child "images/doll_broken_head.png"
            xpos 125
            ypos 50
            droppable False
            draggable True
            dragged drag_placed

        drag:
            drag_name "torso"
            child "images/doll_broken_torso.png"
            xalign .50
            yalign .50
            droppable True
            draggable False

        drag:
            drag_name "legL"
            child "images/doll_broken_legL.png"
            xpos 150
            ypos 100
            droppable False
            draggable True
            dragged drag_placed

        drag:
            drag_name "legR"
            child "images/doll_broken_legR.png"
            xpos 150
            ypos 100
            droppable False
            draggable True
            dragged drag_placed