init python:
    def handle_snapping(drag):
        drag.draggable = False
        try:
            store.count = store.count + 1
        except:
            store.count = 1

    def drag_placed(drags, drop):
        if not drop:
            return
        
        if drags[0].drag_name == "head" and drop.drag_name == "headhb":
            drags[0].snap(drop.x-55,drop.y-190)
            handle_snapping(drags[0])

        if drags[0].drag_name == "armL" and drop.drag_name == "armhb":
            drags[0].snap(drop.x-90,drop.y-45)
            handle_snapping(drags[0])

        if drags[0].drag_name == "armR" and drop.drag_name == "armhb":
            drags[0].snap(drop.x+135,drop.y-55)
            handle_snapping(drags[0])

        if drags[0].drag_name == "legL" and drop.drag_name == "leghb":
            drags[0].snap(drop.x+30,drop.y+140)
            handle_snapping(drags[0])

        if drags[0].drag_name == "legR" and drop.drag_name == "leghb":
            drags[0].snap(drop.x+110,drop.y+140)
            handle_snapping(drags[0])

        try:
            if store.count ==5:
                return True
        except:
            pass
        
        return 

screen tutorial_doll:
    add 'bg tabletop.png'
    draggroup:
        drag:
            drag_name "armL"
            child "images/doll_broken_armL.png"
            xpos 150
            ypos 400
            droppable False
            draggable True
            dragged drag_placed
            drag_raise True
            focus_mask True

        drag:
            drag_name "armR"
            child "images/doll_broken_armR.png"
            xpos 150
            ypos 700
            droppable False
            draggable True
            dragged drag_placed
            drag_raise True
            focus_mask True

        drag:
            drag_name "head"
            child "images/doll_broken_head.png"
            xpos 100
            ypos 50
            droppable False
            draggable True
            dragged drag_placed
            focus_mask True

        drag:
            drag_name "torso"
            child "images/doll_broken_torso.png"
            xalign .50
            yalign .50
            droppable False
            draggable False

        drag:
            drag_name "legL"
            child "images/doll_broken_legL.png"
            xpos 450
            ypos 300
            droppable False
            draggable True
            dragged drag_placed
            focus_mask True

        drag:
            drag_name "legR"
            child "images/doll_broken_legR.png"
            xpos 450
            ypos 575
            droppable False
            draggable True
            dragged drag_placed
            focus_mask True

        drag:
            drag_name "headhb"
            child "images/hitbox.png"
            xalign .50
            yalign .35
            droppable True
            draggable False

        drag:
            drag_name "armhb"
            child "images/hitbox.png"
            xalign .50
            yalign .50
            droppable True
            draggable False

        drag:
            drag_name "leghb"
            child "images/hitbox.png"
            xalign .50
            yalign .65
            droppable True
            draggable False