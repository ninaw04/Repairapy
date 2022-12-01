screen toolbar:
    #change our variable
    #saw

    #pliers

    #hammer
    imagebutton auto "%s_paintbrush.png" xpos 500 ypos 750 focus_mask True action SetVariable("tool", "hammer")

    #needle
    imagebutton auto "gui/button/%s_thread_and_needle.png" xpos 100 ypos 750 focus_mask True action SetVariable("tool", "needle")
    
    $ tool = ""