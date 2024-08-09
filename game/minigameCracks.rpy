screen cracks_minigame:
    add 'bg tabletop.png'
    add environment_SM

label setup_cracks:
    show screen inventory
    $environment_items = ["full"]

    python:
        for item in environment_items:
            image = Image("images/doll/doll_broken_{}.png".format(item))
            environment_sprites.append(environment_SM.create(image))
            environment_sprites[-1].type = item
            environment_sprites[-1].image = image


            if item == "full":
                environment_sprites[-1].width = 250
                environment_sprites[-1].height = 603
                environment_sprites[-1].x = 470
                environment_sprites[-1].y = 150

    call screen cracks_minigame
    hide inventory