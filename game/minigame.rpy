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
    $environment_items = ["armL", "armR", "hair", "head", "torso", "legL", "legR"]
    
    python:
        for item in environment_items:
            image = Image("images/doll/doll_broken_{}.png".format(item))
            environment_sprites.append(enviroment_SM.create(image))
            environment_sprites[-1].type = item
            environment_sprites[-1].image = image

            if item == "armL":
                environment_sprites[-1].x = 150
                environment_sprites[-1].y = 400
            if item == "armR":
                environment_sprites[-1].x = 150
                environment_sprites[-1].y = 400
            if item == "hair":
                environment_sprites[-1].x = 110
                environment_sprites[-1].y = 140
            if item == "head":
                environment_sprites[-1].x = 100
                environment_sprites[-1].y = 50
            if item == "torso":
                environment_sprites[-1].x = 200
                environment_sprites[-1].y = 200
            if item == "legL":
                environment_sprites[-1].x = 450
                environment_sprites[-1].y = 300
            if item == "legR":
                environment_sprites[-1].x = 450
                environment_sprites[-1].y = 575

    # use toolbar
    add minigameDragGroup

default armL = Drag(d=environment_sprites["armL"].image, type = "armL", drag_name = "armL", xpos = 150, ypos = 400, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
default armR = Drag(d=environment_sprites["armR"].image, type = "armR", drag_name = "armR", xpos = 150, ypos = 700, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
default hair = Drag(d=environment_sprites["hair"].image, type = "hair", drag_name = "hair", xpos = 110, ypos = 140, drag_raise = False, droppable = False, draggable = True, dragged = drag_placed)
default head = Drag(d=environment_sprites["head"].image, type = "head", drag_name = "head", xpos = 100, ypos = 50, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed, drag_joined = joined_drags)
default torso = Drag(d=environment_sprites["torso"].image, type = "torso", drag_name = "torso", align=(0.35,0.50), drag_raise = True, droppable = False, draggable = False, dragged = drag_placed)
default legL = Drag(d=environment_sprites["legL"].image, type = "legL", drag_name = "legL", xpos = 450, ypos = 300, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
default legR = Drag(d=environment_sprites["legR"].image, type = "legR", drag_name = "legR", xpos = 450, ypos = 575, drag_raise = True, droppable = False, draggable = True, dragged = drag_placed)
    
default headhb = Drag(d = "images/hitbox.png", drag_name = "headhb", align=(0.35,0.35), drag_raise = True, droppable = True, draggable = False)
default armhb = Drag(d = "images/hitbox.png", drag_name = "armhb", align=(0.35,0.50), drag_raise = True, droppable = True, draggable = False)
default leghb = Drag(d = "images/hitbox.png", drag_name = "leghb", align=(0.35,0.65), drag_raise = True, droppable = True, draggable = False)

default minigameDragGroup = DragGroup(armL, armR, hair, head, torso, legL, legR, headhb, armhb, leghb)