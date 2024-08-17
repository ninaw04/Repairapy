screen cracks_minigame:
    add 'bg tabletop.png'
    add environment_SM

label setup_cracks:
    show screen inventory
    $environment_items = ["crack1234"]

    python:
        # Delete any potential items from other scenes carrying over.
        for item in environment_sprites:
            item.destroy()
            environment_SM.redraw(0)
        environment_sprites = []

        # Reset 'i_overlap' and 'ie_overlap' to False to make sure clicks are detected on items in the environment correctly after switching scenes.
        i_overlap = False
        ie_overlap = False

        for item in environment_items:
            image = Image("images/doll/doll_broken_{}.png".format(item))
            t = Transform(child = image, zoom = 0.4)
            environment_sprites.append(environment_SM.create(t))
            # environment_sprites.append(environment_SM.create(image))
            environment_sprites[-1].type = item
            environment_sprites[-1].image = image


            if item == "crack1234":
                environment_sprites[-1].width = 300
                environment_sprites[-1].height = 603
                environment_sprites[-1].x = 200
                environment_sprites[-1].y = 100
                # environment_sprites[-1].x = 470
                # environment_sprites[-1].y = 150
    
    call screen cracks_minigame
    hide inventory