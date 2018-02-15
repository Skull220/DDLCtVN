label start:

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    #    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    
    # Intro
    $ chapter = 0
    call ch0_main
    
    # Poem minigame 1
    call poem

    # Day 1
    $ chapter = 1
    call ch1_main
    call poemresponse_start
    call ch1_end

    # Poem minigame 2
    call poem

    # Day 2
    $ chapter = 2
    call ch2_main
    call poemresponse_start
    call ch2_end

    # Poem minigame 3
    call poem

    # Day 3
    $ chapter = 3
    call ch3_main
    call poemresponse_start
    call ch3_edited
