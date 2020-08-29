# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:
    $ quick_menu = True
    # Intro
    $ chapter = 0
    "Please select an option."
    menu:
        "Let me play through DDLC from the beginning.":
            call ch0_main from _call_ch0_main
        "Skip me to the new content for 1.0.":
            call newcontent from _call_newcontent
            jump day4
        "Skip me to the new content for 2.0.":
            "You have chosen to skip to 2.0."
            menu:
                "Please, select a character."
                "Sayori":
                    call Sayori2 from _call_Sayori2
                "Natsuki":
                    call Natsuki2 from _call_Natsuki2
                "Yuri":
                    call Yuri2 from _call_Yuri2            
                "Monika":
                    call Monika2 from _call_Monika2
            return
            
    # Poem minigame 1
    call poem from _call_poem_1

    # Day 1
    $ chapter = 1
    call ch1_main from _call_ch1_main
    call poemresponse_start from _call_poemresponse_start
    call ch1_end from _call_ch1_end

    # Poem minigame 2
    call poem from _call_poem_2

    # Day 2
    $ chapter = 2
    call ch2_main from _call_ch2_main
    call poemresponse_start from _call_poemresponse_start_1
    call ch2_end from _call_ch2_end

    # Poem minigame 3
    call poem from _call_poem_3

    # Day 3
    $ chapter = 3
    call ch3_edited from _call_ch3_edited
    call poemresponse_start from _call_poemresponse_start_2
    call ch3_end from _call_ch3_end
  
    # Day 4
    label day4:
    $ chapter = 4
    call ch4_main from _call_ch4_main

    return
