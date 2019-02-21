label returntohub:
    scene bg club_day
    with wipeleft_scene
    mc "Ah, back to the old club."
    mc "There seems to be things to do today."
    mc "I'll probably just blow them off and go talk to the others, though."
    mc "Who knows."
    menu:
        "Talk to Sayori.":
        "Talk to Natsuki.":
        "Talk to Yuri.":
        "Talk to Monika.":
        "Wait for the club activity.":
            if ClubScenesComplete == 0:
                #first club scene here
                #add different extra dialogue if any scenes are complete to any percentage