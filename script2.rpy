# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:
    $ quick_menu = true
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
    call ch3_edited
    call poemresponse_start
    call ch3_end
  
    # Day 4
    $ chapter = 4
    call ch4_main

    return
