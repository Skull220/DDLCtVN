label sayoriroute:
    $ SayoriVar = 0
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "I walk into the literature club and the usual scene greets me." 
    "Yuri’s sitting at her desk, reading a book, and Natsuki and Sayori are talking about something. Monika’s late again."
    "I walk over to Natsuki and Sayori, asking what they're on about."
    show sayori 2c at t21 zorder 2
    show natsuki 4b at t22 zorder 3
    s "Natsuki thinks cupcakes are better than cookies!"
    n "I don’t think they are, Sayori, I know they are!"
    s 1g "I think they’re both really good!" 
    s 1h "But I mean, cookies taste better to me…"
    n 4g "To you!" 
    n 2k "Sayori, maybe I just have better taste." 
    n "After all, how could I be good at baking if I didn’t have good taste?"
    mc "Natsuki, Sayori!"
    mc " Why are you getting so heated over this?"
    "They both look at me."
    n 12c "She started it!"
    s 5d "I just wanted to explain…"
    mc "Alright, that’s enough, both of you."
    mc "This argument is absolutely ridiculous."
    mc "One of you likes cupcakes more, one of you likes cookies more." 
    mc "End of story."
    n 1b "And which one do you like more, [player]?"
    "Again, both pairs of eyes land on me."
    show sayori 5c at t21 zorder 2
    mc "Uhh…"
    "Well, seeing as how this might affect my relationship with whoever I do (or don’t) side with, I might have to choose my words carefully."
    menu:
        mc "Well..."

        "Cupcakes.":
            mc "Well, for the record, I think cupcakes are better."
            n 2d "Hah, see!" 
            n "Even [player] thinks so!"
            s 1g "Aw, maybe you’re right, then…"
            mc "Well, It's not like what I think matters."
        "Cookies.":
            mc "I’ll admit, I do prefer cookies over cupcakes."
            s 4r "Yay!"
            s "That means I’m right!"
            n 4o "All it proves is that I’m in the company of TWO people with bad taste!"
            mc "Well, It's not like what I think matters."
        "Refuse the question.":
            mc "It doesn't matter which one I like."
            
    mc "That's not the point, Natsuki."
    mc "This argument is ridiculous in the first place."
    mc "Just drop it, alright?"
    s 1d "Alright, sorry!"
    n 1g "Well, I’ll drop it."
    n "But only because I know I’m right, and it’s pointless convincing her!"
    "The two girls look to each other one last time." 
    "Natsuki’s glare is lost on Sayori’s cheerful grin." 
    
    "Monika walks into the room."
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide sayori
    hide natsuki
    show yuri 2e zorder 3 at t22
    show monika 2k zorder 2 at l21
    m "Sorry that I'm late, everyone!"
    m 3e "I swear, one of these days I'll have to get a watch or something."
    show monika 2a
    "She takes a moment to gather herself and then continues."
    m 4b "Okay, so does anyone notice anything unusual about the club today?"
    show monika 4a
    "We all exchange blank stares as we feign ignorance before turning back to Monika."
    m 4b "Something important, perhaps?"
    show monika 2a at t31 
    show yuri at t33
    show natsuki 2y at f32 zorder 4
    "Natsuki walks up, smug."
    show monika 2m
    n "Yeah, you're always late!"
    show monika at t31
    show natsuki at t32
    show yuri 2l at f33
    y "I don't think that's what she meant, Natsuki."
    show monika at t31
    show natsuki at f32
    show yuri at t33
    n 5m "Well, it IS something important about the club."
    show monika at f31
    show natsuki at t32
    show yuri at t33
    "Monika lets out a deep sigh."
    m 4l "Other than {i}that{/i}, have you noticed anything that hasn't changed?"
    show monika 2m at t31
    show natsuki at t32
    show yuri at f33
    "This time it's Yuri's turn to be smug."
    y 2s "Natsuki, apparently."
    show monika at t41
    show sayori 1a at t43
    show natsuki at f42 zorder 5
    show yuri at t44
    n 5p "Hey! THAT'S not what she meant either, doofus!"
    show monika at f41 zorder 6
    show sayori at t43
    show natsuki 5n at t42
    show yuri at t44
    m 3l "Alright everyone, calm down please."
    m 4l "What I was getting at is that when I said {i}'Everyone'{/i}, that still only includes the 5 of us."
    m "So... let's talk about that festival, shall we?"
    show monika 4m at t41
    show sayori 1p at d43
    show natsuki 1v at d42
    show yuri 3o at d44
    "The other three girls let out a collective groan."
    "Even if I don't voice it, I feel the exact same way."
    "None of us really want to think about it..."
    show monika at f41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    m 3p "I know, I know."
    m "Its kind of a touchy subject, but we need to talk about it if we're ever going to get things straightened out between all of us."
    m "You were all there, but does anyone need a refresher?"
    show monika 3o at t41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    stop music fadeout 4.0
    "The festival..."
    "It's a day that ALL of us would be all too happy to forget..."
    "...At least that's what the looks on Sayori, Natsuki, and Yuri's faces tell me."
    "But if Monika's insistent on bringing it back up, I guess we have no choice but to remember..."
   
    scene bg house_morning
    with dissolve_scene_half
    "It’s Monday, and time for the school festival." 
    "I’ve always enjoyed these, as they were essentially a day off from school, but I never got involved in anything like this." 
    "I can’t believe I have to read out a poem!" 
    "I’m still not even that proud of the one I chose!" 
    "All of a sudden, my mind jumps to Sayori, who hasn’t come out." 
    "I was waiting outside her door for her to come out, but it seems she overslept again." 
    "Anxious, I walk into her house once more." 
    scene black
    "I still don’t feel very comfortable doing it, but I’m not going to be late because of her."  
    "Besides, it's what a boyfriend would do, right?"
    "I walk upstairs to her room."
    "I set my bookbag down outside the door."
    "I begin to knock on the door, yet I'm still met with no response."
    "Geez, come on, Sayori, are you dead or something?"
    "Wake up!"
    "Ugh, guess I can't do much else."    
    "{cps=*.33}I gently open the door...{/cps}"
    scene bg sayori_bedroom_morning
    "To see her asleep." 
    "I walk over and tap her on the shoulder." 
    "I see her turn over."
    play music t3
    show sayori m1bk at t11 zorder 2
    s "[player]...?" 
    s "What's wrong?"
    "She lets out a huge yawn."
    "Did she forget what today is?" 
    "I want to be mad at her, but instead I find myself stunned." 
    "She looks so cute!" 
    mc "Hey, Sayori. It’s time to get up, okay?" 
    mc "We’re gonna be late to the festival."
    s m1bv "Whaa- The festival!" 
    s m1bw "Ah, [player] will be mad if I don’t get up!"
    "She throws the covers off her, gets up, and opens her eyes to the best of her ability."
    s m1by "Oh, [player]!" 
    s m2bv "You’re here already…"
    s "Sorry, I must have overslept…"
    mc "It’s okay, you still have time." 
    mc "I’ll be waiting outside, okay?"
    s m3bm "Outside? [player], oh no, you’ll be cold!" 
    s m3bl "Go downstairs." 
    s "I'll be right out, okay?"
    scene bg h_livingroom
    "I'm confused by Sayori’s request, but I oblige."
    "It's not that big of a deal to wait for her inside the house." 
    "After a few minutes I see Sayori come down the stairs." 
    "She walks over to the kitchen to pour herself a bowl of cereal."
    s m5a "T-Thanks for waking me up, [player]." 
    s m5b "You really are always looking out for me, ehehe."
    "I still lack the energy to be reprimanding."
    mc "No problem, Sayori." 
    mc "Now, let’s get going, shall we?"
    s m5c "As soon as I'm done with breakfast!"        
    s m5a "You know how I get if I skip it."
    mc "Fine..."

    scene bg class_morning
    with wipeleft_scene
    "We arrive at the festival, and get to our setup."
    "We're about 15 minutes late, but we don't miss much."
    "Of course, the first thing Sayori does is take a huge bite out of one of Natsuki's cupcakes, and I grab one as well."
    "Instead of the traditional swirl, the icing is shaped sort of like a closed book, fitting of the theme."
    show sayori m2q zorder 2 at t21
    show natsuki m5t zorder 3 at t22
    s "Wow, Natsuki, these are really good!"
    n "Thanks!"
    n "I just hope everyone else will enjoy them!"
    mc "It's impressive how the icing's done. Something like this must have taken a lot of time, effort, or both."
    n m2q "Well, duh! I've got a lot of practice with this kind of thing."
    n m2m "It's really not that hard once you get to know it."
    "Yuri and Monika come over, getting a taste, and they seem to enjoy it."
    show yuri 2m zorder 4 at t44
    show monika 2j zorder 3 at t43
    show sayori 2q zorder 5 at t41
    show natsuki 1j zorder 2 at t42
    "They too express their gratitude to Natsuki."
    show monika at t43
    show sayori at t41
    show natsuki at f42
    show yuri at t44
    n m3z "I’m glad you guys enjoyed them."
    n "Just make sure there’s enough for everyone else, alright?"
    show monika at t43
    show sayori at t41
    show natsuki at t42
    show yuri at t44
    mc "Ah, speaking of anyone else, is there someone who signed up to join the club, yet?"
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    hide yuri
    hide natsuki
    hide sayori
    show monika 5a at f11 zorder 1
    m m5a "Nope, not so far."
    m "But the festival hasn’t really picked up yet."
    m m3e "In due time, I guess."
    m m4d "Oh, that’s right, and we haven’t read the poetry yet."
    m m5a "Speaking of which, have you got your poem with you, [player]?"
    mc "Oh yea, it’s right in my bookba-"
    "I cut myself off."
    "I realize by the now apparent emptiness behind me that I didn’t bring my bookbag with me."
    "Great."
    mc "I mean... I did..."
    m m3d "Well... that isn’t very good."
    m "Anyone have a poem they can lend [player]?"
    m "He seems to have forgotten his..."
    m m2m "You know, the main event of the day and everything..."
    "Monika guilt trips me."
    "Hey, I didn't do it on purpose!"
    "Sayori steps in... in my defense?"
    show monika at t21
    show sayori at f22
    s m4p "Hey, don’t be so mean to him!"
    s m5c "For the record, I forgot my poem too, so it really isn’t just him!"
    show monika at t21
    show sayori at f22
    m m5b "Sayori! That's not something you should feel proud of!"
    show monika at t21
    show sayori at f22
    s m5b "B--But!! I just... I forgot, eheheh..."
    show monika at f21
    show sayori at t22
    m m5b "Well, you can’t do that!"
    m "Now TWO of us won’t be able to read anything!"
    m "How will we attract newcomers now?"
    play music t7
    show monika at t21
    show sayori at f22
    s 5d "W-well, my reading wasn’t going to attract anyone new anyway, so really, I don’t count!"
    show monika at f21
    show sayori at t22
    m "Sayori, did you leave it behind just so you didn’t have to read?"
    show monika at t21
    show sayori at f22
    s m1w "What?"
    s m1v "No, why would I do that?"
    s "I wouldn’t lie!"
    show monika at f21
    show sayori at t22
    m "You are lying right now, Sayori!"
    m "I am ashamed of you, Vice President!"
    "At this point, a crowd has gathered at the door, interested."
    "They slowly enter the classroom."
    "A couple of the smarter ones picked up cupcakes, and they’re pointing and laughing at us."
    "Natsuki steps in."
    show monika at t31
    show sayori at t33
    show natsuki at f32
    n m2w "Hey, leave Sayori alone!"
    n "I didn’t want to read these dumb poems either."
    n m2x "In fact, none of us did!"
    n "It was only you who wanted this dumb idea!"
    show monika at f31
    show sayori at t33
    show natsuki at t32
    m "I’m sorry, Natsuki, I thought you were confident enough to read, but I guess not!"
    "I really haven’t seen this side of Monika before."
    "It seems rather... angry, to say the least."
    "Natsuki isn’t having any of that."
    show monika at t31
    show sayori at t33
    show natsuki at f32
    n m5e "I’m sorry, Monika, I thought you listened to your club members when they voiced a concern, but I guess not!"
    n m5f "Some damn president YOU are!"
    show monika at f31
    show sayori at t33
    show natsuki at t32
    m "Natsuki, in case you weren’t listening, there was no one asking for your opinion."
    m "You have no reason to give it."
    show monika at t31
    show sayori at f33
    show natsuki at t32
    s m1v "Well, here, I-i’ll ask now!"
    s "Natsuki, what’s your opinion?"
    show monika at t31
    show sayori at t33
    show natsuki at f32
    n m2y "I’m glad you asked, Sayori!"
    n m2x "In my opinion, Monika’s being an awful president!"
    show monika at f31
    show sayori at t33
    show natsuki at t32
    m "Ah, good to see that you’re both wrong."
    m "Maybe that can change someday, but I doubt it!"
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at f44
    y m2n "G-guys..."
    $ m_name = "Everyone"
    show monika at f41
    show sayori at f43
    show natsuki at f42
    show yuri at t44
    m "Quiet, Yuri!"
    $ m_name = "Monika"
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide monika
    hide sayori
    hide natsuki
    show yuri 1o at t11
    "Yuri squeals softly and backs away."
    show yuri 1p at t11
    "She, however, notices the crowd and is even more scared."
    show yuri at thide zorder 1
    hide yuri
    show natsuki 2x at t32
    show sayori 4p at t33
    show monika 5b at t31
    "I turn to the other club members."
    "Welp, here goes nothing..."
    mc "GUYS!"
    mc "You’re making a mockery of your own club!"
    mc "Stop your bickering!"
    "At once, they all quiet down."
    show natsuki m42b at t32
    show sayori m5b at t33
    show monika m1o at t31
    "Natsuki opens her mouth to defend herself, but she takes one look at me and closes it."
    "At this point, the crowd mostly dissipates."
    "It’s noticeable that still not one signature is on our signup sheet."

    stop music fadeout 2.0
    pause 1.5
    scene bg club_day 
    with dissolve_scene_full
    play music t8

    show monika 3o at f11
    m "So, does everyone understand why this club’s still the way it is?"
    show monika 1o at t41
    show sayori 1k at t43
    show natsuki 1q at t42
    show yuri 1l at t44
    "All 3 of the girls in question look down in disappointment."
    "Monika does, too."
    "She was part of the problem, after all."
    "Even if she doesn't care to admit it."
    "She seems to be thinking a moment..."
    "And she speaks up."
    show monika at f41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    m "I... I’m sorry I snapped at you two, [player] and Sayori."
    m "I really shouldn’t have."
    m "In fact, I should have listened to you the first time around."
    m "And I’m sorry for yelling at you, Yuri."
    "I'm a bit taken aback."
    "Didn't expect that one out of Monika..."
    "But I guess there's a first time for everything."
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    "I guess that means I should also man up and take responsibility."
    "Here goes..."
    mc "I suppose I have to... apologize, too."
    mc "I did cause this, after all."
    show monika at t41
    show sayori at t43
    show natsuki at f42
    show yuri at t44
    "Natsuki steps forward."
    n 3x "Well, you both need to stop being so hard on yourself, it’s dumb!"
    n "It’s not either of your faults, so stop feeling so guilty about it."
    n "It’s...\"{space=5000}{w=0.5}{nw}"
    n "It’s...{fast} I really...\"{space=5000}{w=0.5}{nw}"
    n 12d "It’s... I really...{fast} I’m the one..."
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    "Through the rushing of her words and the shakiness of her voice, it's clear Natsuki struggles to apologize."
    show sayori at t11
    "Sayori comes up and wraps her arms around Natsuki."
    show monika at t41
    show sayori at t11
    show natsuki at t42
    show yuri at t44
    s 3t "I forgive you, Natsuki."
    s "And you too, Monika."
    s "And [player]."
    s 2j "It’s not that big a deal, as long as we’re all still friends, right?"
    show monika at t41
    show sayori at t43
    show natsuki at f42
    show yuri at t44
    "Natsuki looks up."
    n 1j "Yeah."
    n 1t "The club might not have more members, but at least we have us!"
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at f44
    "Yuri stops looking at the floor, and begins to speak up."
    y 3s "I... I like the club better this way."
    y "I know you wanted more members, Sayori and Monika."
    y "But I... I don’t, really."
    y "It’s great to be just us, where we all like each other just the way we are and don’t have any real drama."
    y "Besides, if there’s 5 of us and we sometimes argue, imagine if there were more?"
    show monika at t41
    show sayori at f43
    show natsuki at t42
    show yuri at t44
    "Sayori thinks for a second, an action I rarely see out of her."
    s 1u "Well... I don’t wanna add more members if our current, original members don’t like that idea."
    s "I guess I agree with you guys."
    show monika at f41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    "Monika takes a look at everyone, processing this. She seems to connect this idea."
    m 1p "I... guess it’s settled then."
    m "No more members, huh?"
    m "Okay, everyone."
    m "Are we sure the club is good as it is?"
    show monika at t41
    show sayori at t43
    show natsuki at f42
    show yuri at t44
    n "Absolutely!"
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at f44
    y "I don’t mind this."
    show monika at t41
    show sayori at f43
    show natsuki at t42
    show yuri at t44
    s 1x "It’s great with just you guys!"
    s "I wouldn’t change this for anything!"
    show monika at f41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    m 3b "Alright."
    m "Then, the literature club stays how it is."
    m "Well, no poems this week."
    m 3j "Take it as a show of good faith from me, I guess."
    show monika at t41
    show sayori at t43
    show natsuki at f42
    show yuri at t44
    n 1a "Woo! Thanks, Monika!"
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at f44
    y 2q "Aww, well, alright."
    show monika at t41
    show sayori at f43
    show natsuki at t42
    show yuri at t44
    s 1q "Oh, good, no need to worry about that..."
    show monika at t41
    show sayori at t43
    show natsuki at t42
    show yuri at t44
    "Yuri looks at me."
    "I smile."
    "She returns it, and we all leave the club."
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide yuri
    hide monika
    "Me and Sayori leave together."
    show sayori lt zorder 2 at t11
    s 1t "[player], am I still coming over Sunday?"
    mc "I'd love to have you!"
    show sayori 1c zorder 2 at t11
    "She beams."
    "I'm so ready for Sunday."
    scene black
    with dissolve_scene_full




    scene bg corridor
    play music t5_sayori
    "It's the beginning of lunch period."
    "I’m at my locker when unbeknownst to me, Sayori shows up behind it." 
    show sayori 4t at t11 zorder 2
    s 4t "Found any good books in there?"
    "I recoil at her voice, startled. I sigh."
    mc "If you count math textbooks, sure." 
    mc "But I sure don't."
    s 1l "Hehe, fair point."
    mc "What are you doing here anyway?" 
    mc "Isn't your locker two hallways down?"
    s 2c "I don't need anything from it." 
    s 4l "Thought I might come down here and talk until the bell rings."
    "I roll my eyes."
    mc "Skipping Class? Sayori, I am ashamed." 
    "I say, sarcastically." 
    "Lunch period isn’t taken seriously by the teachers anyway." 
    "As long as you get back on campus before the next class, they couldn’t care less."
    s 5c "I'm NOT skipping!" 
    s 5d "Lunch doesn’t count..."
    mc "You're not actually thinking of going out, are you?" 
    "She thinks about the idea for a moment."
    s 5a "Mmm... maybe?" 
    s "Normal lunch is boring anyway."
    mc "Well, go with someone else." 
    mc "I'm not going to get in trouble with you."
    s "Aww, come on." 
    s "It might be fun." 
    s 2t "Please?"
    "She uses {i}those{/i} eyes. The ones every girl uses when she wants something."
    menu:
        mc "Well..."

        "Go with Sayori.":
            $ SayoriVar += 1
            mc "Fine." 
            mc "If we get in trouble, it's all your fault."
            s 4r "YAY!" 
            s "You're the best, [player]!"
            mc "Yeah, yeah." 
            mc "So, what do we do now?" 
            mc "Just leave?"
            s 2o "I don't know." 
            s "I've never actually done this before." 
            s "I think that's it, though."
            "I ponder this for a moment."
            mc "So where do you wanna go?"
            s 1x "Ooh!"
            s "Let's go exploring in the woods behind the school!"
            mc "...You're just full of bad ideas today, aren't you?"
            s 2o "Hey, what else would we do?"
            "I begrudgingly agree." 
            scene bg residential_day
            #change this later
            "We make our way to the woods within the minute, and before I know it Sayori's almost out of view." 
            "I catch up with her."
            mc "Wait!" 
            mc "Are you not scared that there might be something here?" 
            mc "A bear or a rabid animal or something?!"
            show sayori 3l at t11 zorder 2
            "Sayori chuckles at my concern."
            s 3l "Come on, [player], don’t be so scared!" 
            s "You were never like this when we were kids."
            mc "Hey, if being a wuss stops us from being killed, I'm glad to have changed."
            s 5d "You're no fun now..." 
            s 5b "It's alright, nothing will happen!"
            "With that, she walks off."
            show sayori at thide zorder 1
            hide sayori
            "Begrudgingly, I follow her." 
            "I'm glad I did, as next I see her she's falling on her back into a creek."
            show sayori 2p at t11 zorder 2
            s 2p "Oww!"
            mc "Sayori, are you alright?"
            s "No, help!"
            s "I might drown!"
            "I contain the urge to laugh." 
            "She's barely halfway submerged."
            "I pick her up."
            mc "Sayori..." 
            mc "You..." 
            "I sigh." 
            mc "Nevermind."
            s 1t "Th-Th-Thanks [player]."
            "She says, shivering."
            mc "Here, take this." 
            "I say, talking off my light jacket and handing it to her." 
            "It's not much, but it should help." 
            "As she takes it and puts it on, I remember every cheesy romance scene in every movie."
            "Where the boyfriend takes off his jacket and gives it to his girlfriend on a cold winter night."
            "Being in that position, it isn't as romantic as they portray it to be." 
            "Or at least, that’s what I think." 
            "Something changes about her expression when she puts on my jacket."
            s 1q "Aah." 
            s "You really are the best, [player]."
            mc "You're welcome."
            mc "Now let's head back." 
            mc "If we hurry, we can make it to 4th period and not get in trouble." 
            "I say, checking my watch."
            s 1l "And then next is math."
            s "At least it's a class we share."
            "It's one we've shared for five months, but for some reason her statement-of-the-obvious makes her look... content about something."
            mc "Why do you point that out?"
            s 2j "That way you can't tell anyone about what happened without me knowing."
            s "Don't tell anyone, by the way."
            "I never planned to, but she makes me promise anyway." 
            "I do so, and with that we head back."
            "Even still, we’re about 5 minutes late."
            scene bg corridor
            #change above later if possible. If not, change below
            "We're inside the building when Natsuki sees us, and laughs at Sayori."
            show sayori 2j at t21 zorder 2
            show natsuki 1l at t22 zorder 3
            n "What happened to you?"
            "She asks after her laughter subsides." 
            "Sayori struggles for a second to make up an excuse."
            s "It's his fault." 
            "She says, pointing to me." 
            s 4p "[player] made me wet!" 
            "At this point, Natsuki can hardly contain herself, and laughs harder than a kid at the circus."
            mc "Sayori? Do you understand what that means?" 
            "I whisper to her."
            "She whispers back."
            s 2o "What do you mean by that?"
            "I explain to her why her double-entendre got such a reaction out of Natsuki."
            
            "Her face turns a pink only rivaled by Natsuki’s hair."
            s 2w "I-I..." 
            s 2p "That's not what I meant!"
            n 1z "Yeah, sure it isn't." 
            n 1y "I'd tell you two to get a room if there was one without a teacher in it." 
            n "Bye lovey doveys~"
            show natsuki at thide zorder 1
            hide natsuki
            "Sayori buries her face in her hands, clearly embarrased."
            "I don't blame her." 
            "Even I get a bit red after hearing Natsuki's statement."
            show sayori at thide zorder 1
            hide sayori
            "We both head to our classes."
            scene bg class_day
            "Other than being late to fourth hour, I speed through the next few periods."
            "When I get to seventh, over the intercom I hear:"
            "[player], Sayori. Please make your way to the main office at the end of the hour."
            "Great." 
            "So, seventh period ends."
            "I go to the office to see Sayori sitting there, waiting for the principal to show up."
            mc "So, your teacher told on you too, huh?"
            show sayori 1a at t11 zorder 2
            "She nods."
            mc "Great."
            s 5b "At least we won't be alone in detention, hehe..."
            "I'm amused she can still take solace in such a fact." 
            "She really does take joy in the little things..."
        "Refuse.":
            mc "Sorry Sayori."
            mc "Find someone else."
            mc "I'm not going to risk getting caught."
            s 5c "Buzzkill.... When I have a fun time, and you don't, I’m gonna make fun of you for it."
            mc "And when you get in trouble, and I don't, I’m gonna make fun of you for it."
            s 5d "You meanie..."
            "She closes with that and walks off."
            "Other than being late to fourth hour, I speed through the next few periods."
            "When I get to seventh, over the intercom I hear:"
            "[player], Sayori. Please make your way to the main office at the end of the hour."
            "Great." 
            "So, seventh period ends."
            "I go to the office to see Sayori sitting there, waiting for the principal to show up."
            mc "Sayori, why am I here?"
            show sayori lv at t11 zorder 2
            s 1v "Sorry!" 
            s 1u "I don't wanna go through detention alone..." 
            s "Will you play along?"
            mc "What... you set me up?"
            s 1t "Pleaaaseee.... I'll owe you one."
            mc "I would make fun of you if I weren't this upset."
            show sayori 5d at t11 zorder 2
            "Sayori looks down with regret written on her face."
            "Great." 
            "Damned if I did, damned if I didn’t." 
            "Against my better judgement, I agree to it." 
    "I sit in the chair next to her and the waiting game ends when the principal shows up." 
    "Long story short, we both have detention as predicted." 
    "That's going to be fun... And as a bonus, we get to miss the literature club." 
    "Thanks a lot, Sayori."
    
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3
    
    scene bg livingroom_morning
    play music t2
    "It’s  a Sunday like any other."
    show sayori 4bd at t11 zorder 2
    "Sayori, as usual, walks  right into my house."
    s m4bd "Hey, [player]~!"
    "She walks  up to me and… pokes me on the nose."
    s m2br "Boop!"
    mc "W-what? What was  that?"
    s m2bq "I booped you, silly!"
    mc "… What does  that mean?"
    s m2bd "Well, this!" 
    "She smiles, and pokes my nose once more." 
    "I give up trying to understand her and direct us both to the couch."
    mc "Well, what do you want to do today?"
    s "Oooh." 
    s m1bc "We can play cards!"
    "She pulls  out a deck of cards from her back pocket."
    mc "Where did you get those?"
    s m1bb "They were just sitting around, in my room." 
    s "I thought if we had nothing to do today, might as  well be this!" 
    s m1ba "What should we play?"
    mc "Uhh… Go Fish?"
    "It’s the only card game I know."
    "Content with this choice, Sayori smiles and sits down on the floor, and I sit across from her." 
    "She deals the cards, and we begin playing."
    s m2bn "Uuh… got any red cards?"
    mc "Sayori, you have to ask for a card of a specific type. Like ones  or threes."
    s m4bl "Oh, okay!" 
    s m4bc "Got any ones or threes?"
    "My hand makes sudden and unexpected contact with my face."
    mc "Sayori, ask for one card type at a time. And it has to be a card that you have!"
    s m2bk "S… sorry. I've just never played this before, eheheh."
    "Instantly, I feel bad for Sayori." 
    "It should have clicked for me that she’s never played this..." 
    "Right now all I’ve been doing is getting angry with her for something that’s not her fault."
    menu:
            "Aww, Sayori..."

            "Forgive her.":
                $ SayoriVar += 1
                mc "Sorry for being so rude."
                mc "Should have realized you hadn't played it."
                s m1bd "Oh, it’s  alright~!" 
                s m1bi "We can do something else." 
                s m3ba "Here, let’s watch tv!"
                "I don’t disagree, instead getting up to reach for the remote." 
                "Sayori moves up to the couch, and when I return I sit there myself."
                mc "So what do you want to watch?"
                s m1bo "I don’t know, [player]." 
                s m4bl "It’s up to you."
                s m2bq "Your tv, your pick right?"
                mc "Wait, D/V/D is  showing!" 
                mc "Wanna watch that?"
                "I switch to the channel, then get up to turn off the lights and close the blinds." 
                "A little bit into the movie, Sayori begins to object."
                s m1bm "A-A horror movie?" 
                s m1bp "[player], those scare me a lot!"
                "She begins to recoil."
                "It’s here that I realize that I should probably comfort her somehow."
                mc "Sayori…"
                mc "… If you’re that scared, then come here." 
                mc "Don’t worry, I’ll protect you… from the TV."
                "I outstretch my arms to the side of myself, realizing how dumb my idea and what I just said sounded." 
                "To my shock, Sayori embraces them, and hugs me like I’m the last man on earth."
                mc "Hey.. careful!"
                s m2bj "[player]…?"
                mc "Hmm? What’s up?"
                s m2bk "Thank you…" 
                s m2bl "I really am scared, and I’m kinda glad that you’d do this with me."
                mc "Sayori, you get scared over every little thing." 
                mc "But you’re welcome." 
                mc "I lo-- e-enjoy cuddling like this."
                s m1bt "Hehe..." 
                s "I… I really like it too." 
                s m1bj "And not every little thing, meanie..."
                "Me and Sayori take one last look at each other and go back to it." 
                "After a while, the movie ends, and we both get up." 
                "Sayori’s ready to leave."
                s m3bk "That was really scary…"
                s m3bd "but it wasn't that bad with you."
                s m3bt "I’m glad I come over every Sunday!"
                mc "So am I, Sayori." 
                mc "I- you’re the best, you know that?"
                s m4bq "You too!" 
                s m2br "Boop!"
                "She pokes me once more on the nose and smiles to herself."
                mc "Hey..." 
                mc "Knock it off!"
                s m4bs "But you're so cute when I boop your nose!"
                mc "You're weird, Sayori."
                s m1bq "Hehe..."
                s m1bb "Well, Thanks for playing cards and watching TV with me, [player]." 
                s m1ba "I'll see you tomorrow, alright?" 
                mc "Sure thing."
                mc "Later, Sayori."
                "There, things are back to normal." 
                "We say our goodbyes and Sayori leaves."
                show sayori at thide zorder 1
                hide sayori 
                "I notice that even now I still can’t tell her I love her." 
                "I still lack the confidence even after all this time."
            "Reprimand her.":
                mc "You should have told me you didn't know."
                s m2bf "Oh, I-I guess you’re right…" 
                s m2bh "I’ll tell you next time, okay?"
                "With that, we go back to the game, this time a strange tension over the room." 
                "I win every round, save for the first one where I let her win, and before we know it it’s time for her to go." 
                s m2bb "Thanks for playing cards with me, [player.]"
                s m1ba "I’ll see you tomorrow, alright?" 
                mc "Sure thing, later Sayori."
                "There, things are back to normal." 
                "We say our goodbyes and Sayori leaves."
                show sayori at thide zorder 1
                hide sayori
                "I mentally kick myself for being so mean to her."
    "That sucks." 
    "At least she doesn’t seem to mind."
    
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3
    
    scene bg bedroom_morning
    play music t3m
    "It’s Sunday, and once again Sayori walks into my house, and up to my room."
    show sayori m1ba at t11 zorder 2
    s "Hey! What’s up, [player]?"
    mc "Hi, Sayori. Just watching some anime."
    mc "Ready to have some fun?"
    s m2bu "Eh- About that."
    s "I wanted to come over to say I… want to cancel." 
    s m2bv "I know it’s a bit late, but I really don’t feel up to it today."
    s "Sorry."
    "Her expression seems to match her words." 
    "However, it doesn’t seem like the Sayori I’m used to." 
    "While I stare, confused, Sayori walks back out." 
    "I begin to get up and I follow her."
    "She’s about to open the door, but I tap her on the shoulder and stop her."
    mc "Sayori, what’s going on?"
    s m1bl "Oh, ehehe…"
    s "No need to worry about it."
    s "It’s just me being silly."
    s m3bk "It’s nothing important."
    mc "Sayori, something’s wrong, so as long as that’s true, it’s important." 
    mc "It makes me feel much worse to let you go than it does to find out what’s wrong..." 
    mc "so if something’s wrong, you tell me."
    s m4bk "Dang it, [player], you keep doing this to me..." 
    s m2be "The truth is that I really don’t like taking time away from you and the others in the literature clu—"
    mc "Come on, Sayori, that’s not it." 
    mc "What is it really?" 
    mc "I know this didn’t start 5 days ago."
    "I don’t really know that, but I’m trying my best to stay confident in this." 
    "If I want to help Sayori, I need to do it as gracefully as possible."
    "Sayori looks at me one more time, as if to beg ‘please don’t make me do this’, but at last she begins to speak."
    stop music
    play music t10
    s "..."
    s m1bv "I keep having those thoughts, [player]." 
    s "The kind I keep telling myself I really shouldn’t be having, but I have them no matter what I do." 
    s 1by "The thoughts that I hate myself or that I’m not allowed to be happy or that the universe hates me." 
    s 1bu "I never tell anyone because I don’t want to make them sad, but... I guess that already happened, right?"
    "I realize why it always seemed so out of character for Sayori to be like this;" 
    "it’s because she has a different character around me." 
    "I almost feel betrayed." 
    "It’s like there’s a whole other side to my sweet childhood friend that I didn’t notice." 
    mc "Sayori… why did you not say anything sooner?" 
    mc "Why’d you try and hide your emotions like that?"
    s m4bp "See! I just made you angry."
    s "I always mess this up." 
    s m3bw "I shouldn’t have said anything."
    mc "Sayori…"
    "She looks at the floor, seemingly ashamed of herself."
    mc "I’m not mad at you."
    mc "And I won’t be."
    mc "Just tell me what’s wrong."
    "She doesn’t seem to want to give an answer."
    "I repeat myself."
    mc "Sayori, seriously."
    mc "If something’s up, I want to know about it."
    s m1bv "I just...I don’t want to make everyone else sad."
    s "I’m not worth it."
    s m1bu "If I can make other people happy..."
    s "At least I won’t feel so guilty."
    mc "Sayori, I can’t be happy if you’re not."
    mc "You’re not protecting me by keeping your sadness a secret." 
    mc "I want to help you." 
    "I still have no idea if I’m helping or not."
    "I feel like I’m walking a minefield."
    "One wrong move and Sayori might never speak to me again, in more ways than just one." 
    "I grab her head and turn it so she’s looking directly in my eyes."
    mc "Sayori…"
    "We kinda just stand there for a bit, looking into each other’s eyes."
    "When I snap into reality, I try to help the only way I know how."
    mc "What do you dislike about yourself, Sayori?"
    "I decide to tackle it one problem at a time, hoping it will help."
    s m1bk "Well, where to begin?"
    s "I’m an idiot, [player]."
    s m1bj "You’ve said so, and you aren’t the first or last to say it."
    s "No one likes to be around an idiot."
    mc "Sayori, I’ve been your friend for as long as I remember, and I can tell you that’s not the case."
    mc "Besides, I don’t mind you being a bit on the slow side."
    mc "It’s really… cute."
    s m3bh "Really?"
    mc "Why would I lie about that?"
    s m2bf "Ah- I guess."
    s 1bf "But I realize you’ve never truly complimented me ‘til now." 
    s "It’s just kind of weird to hear."
    mc "Sayori, there’s so much to compliment you for."
    mc "You’re fun to be around, you’re really nice, you s—"
    s "[player]…" 
    s m1bg "It’s not me you have these feelings for."
    s "It’s a different version of me."
    s "I don’t know if it’s even me that you love."
    mc "Sayori, of course it is!"
    mc "You’re still you, in the end, even if what I’ve seen isn’t the full picture." 
    mc "Besides, this is the same version of you."
    mc "Just with a hidden aspect."
    s m1be "I… I really don’t know how to talk about this."
    s "I don’t want to, either."
    s "I’m going home, [player]."
    "I don’t know how to respond to that." 
    "On the one hand, maybe some alone time is what she needs, but that might just make things worse for her."
    "On the other, I can tell her to stay, and I know she’ll not like it..."
    "Yet chances are she’ll do it anyway, so I can get to the bottom of things."
    menu:
        "But in the end, I decide to—..."

        "Tell Sayori to leave.":
            mc "Fine, Sayori." 
            mc "As much as I don’t want to do it, you can go."
            mc "I WILL see you Monday, got it?"
            s m4bd "Thanks, [player]." 
            s m4bc "I knew you would agree in the end."
            s "I’ll think about everything that’s happened here later." 
            "Perhaps the most terrifying thing was that she didn’t say ‘yes’ upon leaving..."
            show sayori at thide zorder 1
            hide sayori
            "But when she leaves I feel awful." 
            "Was that really the right idea?" 
            "Should I go after her?" 
            "Instead, I simply end up walking back upstairs and thinking to myself how maybe this’ll all fix itself."
            "But that just seems like wishful thinking."

        "Continue Talking.":
            $ SayoriVar += 1
            mc "No, Sayori."
            mc "You’re not making me sad." 
            mc "And you aren’t leaving until I know you’re sound."
            mc "I can’t force you to stay, but I’m asking you that you don’t."
            "Sayori looks at me and realizes I’m serious." 
            "Defeated, she walks away from the door and sits on the bed." 
            "I sit in the chair next to her."
            mc "Sayori, when DID this begin?"
            s m2be "I dunno..."
            s m1bf "I guess it’s been here since I remember." 
            s "I always remember never wanting to be negative, because all the other kids would complain about things..."
            s m1bg "and I hated that." 
            s "I hated being so negative around others."
            mc "We all need to vent sometimes, Sayori." 
            mc "You need to get that idea out of your head." 
            mc "If there’s something you need to complain about, I want you to come to me from now on, alright?"
            "Sayori looks at me, expressionless."
            "I'm getting afraid that she's not listening to me." 
            "She stays quiet for a while, but eventually her face changes a little and she breaks the silence."
            s m1bh "Okay... I guess I'll do that."
            s "Thank you, [player]."
            mc "Sayori… I know it seems weird." 
            mc "And I know you don’t WANT to talk about it."
            mc "But you want to see your friends happy, right?"
            "She looks down, then raises her head to look in my eyes, and nods slowly." 
            mc "Nothing could make me happier than you doing this, then." 
            mc "I lo..." 
            mc "You’re my girlfriend, Sayori, so seeing you unhappy doesn’t make me happy at all."
            "What’s wrong with me?" 
            "Even now, I couldn’t say the word." 
            "Even when Sayori needed it most." 
            "Even when I wanted nothing more but to say it." 
            "What kind of boyfriend am I?"
            s m1bv "Sorry..." 
            s "I guess I didn’t really think of it like that, heh." 
            s m1bw "It seems like no matter what I do, I just end up making the people I care about unhappy anyway."
            mc "No, Sayori!"
            mc "It’s not like that, I swear!"
            mc "I’m not unhappy right now, I didn’t mean it that way..." 
            mc "I just--- ah!"
            "As I stumble over my words, she giggles." 
            "For the first time this afternoon, a genuine smile comes over her face."
            s m1bs "Ha-haha!" 
            s "It’s really silly to see you flustered like that, [player]." 
            s m1bt "..."
            s m1bt "It’s okay, I think I know what you mean."
            mc "You do?" 
            mc "Then... I… I’m glad, Sayori." 
            mc "I just want to help you."
            "She silences me and motions me upstairs."
            "I follow her."
            scene bg bedroom
            with wipeleft_scene
            "She takes a seat on my bed, and I sit at my desk chair."
            "She opens her mouth and begins to speak."
            show sayori m2bk at t11 zorder 2
            s m2bk "[player]..."
            s "You ever feel like every action you take is wrong?"
            s m1bj "Like just now."
            s m3bu "If I had refused to come up here, and shown myself the door..."
            s "I would have worried you with whether or not I was okay."
            s m3bv "And yet, now that I'm up here, talking to you about it..."
            s "I'm getting you worried directly."
            s "I've been nothing but a negative on my friends all the time."
            s m1bh "Making things uncomfortable between you and Yuri..."
            s "Stealing that cookie from Natsuki..."
            s m1by "Even if it was really good..."
            s m2bg "Forgetting my poem, and then arguing with Monika about it..."
            s "I'm not a good friend, [player]."
            s m2bh "All I do is hurt others. Drive them away."
            s "That's all I've ever done."
            "Why is Sayori saying all these things about herself?"
            "I'm almost... unprepared for it."
            "But that's not really true, is it?"
            "She... has me..."
            mc "Sayori."
            mc "Not only do you have one friend in particular that'll never leave until one of us are dead..."
            mc "But you also have lots who love you for exactly who you are and no one else."
            mc "Sayori, you didn't apologize to Monika on that day. She did to you."
            mc "Why?"
            mc "If all you're good for is hurting others..."
            mc "Why would she bring herself to apologize?"
            mc "Why would she take that step to fix your friendship?"
            show sayori m2bv at t11 zorder 2
            "Sayori struggles to think of a response."
            "I get up and wrap my arms around her."
            show sayori at thide zorder 1
            hide sayori
            scene black
            mc "Don't you ever think those things about yourself Sayori, because they'll never be true."
            "She reciprocates."
            s "I... thank you, [player]. That's really nice, coming from you."
            "We stand like this, for some time."
            "Eventually, I release my hold on her, and she does the same."
            "She looks at me one last time."
            "She cups a hand to my face..."
            "And turns around, leaving the room."
            "I hope I did at least SOMETHING right."
            "Sayori really needs me right now."
            "I hope to god I can be there for her."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3
    
    scene bedroom
    with wipeleft_scene
    play music t5_sayori
    
    "It’s just like any other Sunday, me waiting patiently for Sayori to show up." 
    "We’ve done this quite a few times now, and it’s starting to set in as commonplace." 
    "It’s still exciting each time, and it’s kind of become a factor of motivation for the rest of the week, but it’s a different kind of excitement now."
    "As I ponder this, Sayori knocks on my door." 
    show sayori 1ba at t11 zorder 2
    s 1ba "Hi, [player]!"
    "She’s in casual clothing as usual." 
    "I can’t help but notice she seems cheerier than normal."
    "She immediately takes one look at me and frowns."
    s 1bc "[player]…  look at your hair, it's all messy!"
    mc "Ah, no, I seem to have forgotten to brush it. Sorry about that."
    s 1bd "Aww, don’t feel bad!" 
    s "Sometimes I forget to brush my hair, too~!" 
    s "Here, I’ll make us even."
    "Sayori puts both her hands in her hair, and rustles them around until her hair is messy."
    s 1br "There! Now we’re even~!"
    mc "Sayori…"
    "I suppress the urge to burst out laughing." 
    "Has Sayori always been this cute?"
    mc "Well, now that’s settled, would you like to come inside?"
    "She nods and follows me in." 
    s 2bo "Hey, [player]!" 
    s 4bq "I hope we’re doing something fun today!"
    mc "Have I shown you video games, yet?"
    "She looks excited, which is not what I was expecting, but I don’t mind it."
    s 3ba "Oooh, video games!"
    s 3br "Sounds good, [player]!" 
    s "I’ll wait for you down here."
    show sayori at thide zorder 1
    hide sayori
    "I go upstairs and grab the wires, console, controller, and a couple of games."
    "I remember as well to fix my hair."
    "I don’t know which game I should show Sayori, though."
    "If I pick correctly, it might make her more interested in the hobby…"
    "I go downstairs." 
    "I hook up the wires to the television and grab the games."
    show sayori 1ba at t11 zorder 2
    "Right as I do this, she joins me in the living room."
    s "So, what game are we playing, then?"
    mc "Hmm…"
    "I ponder this for a moment. Getting this right will be crucial." 
    "All the games will be really fun..." 
    "But I know that one of them is the one that Sayori wants to play the most."
    menu:
        "But which?"
                
        "An Ultra-violent shooter.":
            "I grab {i}Damned{/i}’s box and pop the disk in the tray."
            "I dim the lights, and we both sit on the couch."
            "While she does pay attention, she doesn’t seem to enjoy it."
            s 1bm "[player]! Did you have to pick something so violent?"
            "I want to be mad, but I can only enjoy Sayori’s innocence."
            "She’s really grossed out by it, and I really don’t blame her."
            "Even if it’s not all that realistic, it’s still graphic."
            "I continue playing, but she rests her head on my shoulder and closes her eyes, falling asleep in no time."
            "Eventually, the sun starts to set, so I gently wake her up, and she begins to leave." 
            s 1by "Bye, [player]."
            mc "Bye, Sayori." 
            "As Sayori starts to leave, she turns around and walks back to me."
            s 2bu "Umm, [player]?"
            s "Do you think we can do something different next week?"
            mc "O-Oh..."
            mc "Sure thing, Sayori! I’ll see you Monday."
            show sayori at thide zorder 1
            hide sayori
            "It's clear Sayori didn't enjoy herself today." 
            "What was I thinking, choosing a game she clearly didn't enjoy?" 
            "I'll definitely have to pick a different one next time."  
        "A Player vs Player game.":
            "I grab {i}Rumble 3{/i}’s box and pop the disk in the tray."
            "I dim the lights, and we both sit on the couch."
            "While she does pay attention, she doesn’t seem to enjoy it."
            s 1bm "[player]! Did you have to pick something so violent?"
            "I want to be mad, but I can only enjoy Sayori’s innocence."
            "She’s really grossed out by it, and I really don’t blame her."
            "Even if it’s not all that realistic, it’s still graphic."
            "I continue playing, but she rests her head on my shoulder and closes her eyes, falling asleep in no time."
            "Eventually, the sun starts to set, so I gently wake her up, and she begins to leave." 
            s 1by "Bye, [player]."
            mc "Bye, Sayori." 
            "As Sayori starts to leave, she turns around and walks back to me."
            s 2bu "Umm, [player]?"
            s "Do you think we can do something different next week?"
            mc "O-Oh..."
            mc "Sure thing, Sayori! I’ll see you Monday."
            show sayori at thide zorder 1
            hide sayori
            "It's clear Sayori didn't enjoy herself today." 
            "What was I thinking, choosing a game she clearly didn't enjoy?" 
            "I'll definitely have to pick a different one next time."

        "A Co-Op game.":
            $ SayoriVar = 4
            mc "Here, let’s play this."
            "I grab {i}Wormhole 2{/i}." 
            "A little bit of Co-op never hurt anyone."
            "I pop the disk in and hand her my second controller." 
            "I dim the lights, and we both sit on the couch."
            scene bg livingroom_evening
            "Having played through most of these puzzles before, I get back into the rhythm in no time." 
            "But Sayori seems to struggle."
            "I should have seen that coming, as she isn’t the brightest..."
            "But she seems just fine listening to me dictate what to do." 
            s e2bo "[player], you must be really smart, because you’re soo good at this."
            mc "Well, I’ve played this before."
            mc "I was just as clueless as you are when I first did this."
            s e1bu "Are you sure? I don’t know..." 
            s e1bv "I feel like I’m just bad at this."
            "Sayori looks down, disappointed with herself."
            s e4bw "Am I holding you back, [player]?"
            s "I'm so sorry..."
            stop music fadeout 1.0
            play music t9
            "She puts her hands in her face and starts to cry."
            mc "Sayori..?"
            s e4bu "I'm so bad at this..."
            s "You must think I'm awful!"
            mc "Sayori, stop it!"
            "I set down my controller and quickly hug her."
            "She seems shocked by this at first, but eventually returns my embrace." 
            s e1bv "[player]…?"
            mc "Sayori..." 
            mc "Why does it matter if you're bad at this game?" 
            mc "I already know you aren't good at games!"
            mc "You don't play them normally..."
            mc "So of course you aren't going to be the best at it!"
            mc "The point is..."
            mc "I wanted to play this game with you..."
            mc "I just wanted to be with you..."
            s "Are you sure, [player]?"
            mc "Of course, Sayori!"
            mc "Even if I were to play this with somebody else who was good..."
            mc "It wouldn't have felt as great as playing with you."
            mc "You've always been the best part of my life."
            "With that, she hugs me a bit tighter than before, burying her face in my chest."
            "I can feel her tears running down onto my shirt..."
            mc "Sayori..."
            mc "I'll always be here for you."
            "We hug for a bit until she finally pulls back."
            s e2bt "Umm, [player]?"
            mc "Yes, Sayo-"
            show sayori 2bt at face zorder 1
            "In an instant, Sayori's lips meet mine."
            show sayori at thide zorder 1
            hide sayori
            scene black
            "My heartbeat starts increasing erratically."
            "Is she kissing me?"
            "She pushes against my lips even further."
            "Suddenly, she pulls back."
            scene bg bedroom
            #fix this to be his living room
            show sayori 1bw at t11 zorder 2
            s "Oh my gosh, [player]!"
            s "I don't know what came over me, I'm so sorry!"
            s e2bp "I won't ever do it again, I promise I wi-"
            "I interrupt her apology with a kiss of my own."
            scene black
            "I wrap my arms around her and don't let go."
            "My mind starts to goes blank."
            "The feel of her body pushed up against my own..."
            "The smell of peaches that come from Sayori's perfume..."
            "The sensation of her lips interlocking with mine..."
            "This is all I can think about as we continue."
            "She begins to wrap her arms around me."
            "Her hug feels delicate, yet firm."
            "I reciprocate with a hug of my own."
            "This feels so great..."
            "After what seemed like an eternity, we both release each other to catch our breath."
            scene bg bedroom
            show sayori e1bw at t11 zorder 2
            s e2by "[player]… My god, that was so…"
            mc "Amazing."
            "We stare at each other for a bit more before finally I begin to move."
            "I pick up my controller, and Sayori scoots next to me."
            "I switch back to single player mode and wrap an arm around Sayori."
            "We continue like this until she gets tired." 
            s e2bx "Well, I don't want to go... but it’s getting late for me, [player]."
            s "We’ve got school tomorrow."
            "As she's walking out, she starts yawning, then turns to me." 
            mc "I don't want you to go either... but I guess you should."
            s e2bl "[player]… Thank you. So very much."
            s "I’ve never felt this great in my life." 
            s "I seriously don't know how you've done it!"
            mc "Sayori, if you hadn’t admitted to me that Sunday all those weeks ago, this wouldn’t have happened." 
            mc "You’ve done it as much as I have."
            "She smiles at me, knowing that what I’ve said was true." 
            mc "And I feel the exact same way, so..."
            mc "Thank you, as well. I’ll see you tomorrow."
            "She runs back up to me, hugs me, and walks out."
            show sayori at thide zorder 1
            hide sayori
            mc "Well... I guess I should get ready too. Later... Sayori."
            "I say that last part mostly to myself, as I know Sayori's too far to hear me."

                
        "A story-driven game.":
            "I grab {i}Gone Nuclear: Vegas Blues{/i}’s box and pop the disk in the tray."
            "I dim the lights, and we both sit on the couch."
            "While she does pay attention, she doesn’t seem to enjoy it."
            s 1bm "[player]! Did you have to pick something so violent?"
            "I want to be mad, but I can only enjoy Sayori’s innocence."
            "She’s really grossed out by it, and I really don’t blame her."
            "Even if it’s not all that realistic, it’s still graphic."
            "I continue playing, but she rests her head on my shoulder and closes her eyes, falling asleep in no time."
            "Eventually, the sun starts to set, so I gently wake her up, and she begins to leave." 
            s 1by "Bye, [player]."
            mc "Bye, Sayori." 
            "As Sayori starts to leave, she turns around and walks back to me."
            s 2bu "Umm, [player]?"
            s "Do you think we can do something different next week?"
            mc "O-Oh..."
            mc "Sure thing, Sayori! I’ll see you Monday."
            show sayori at thide zorder 1
            hide sayori
            "It's clear Sayori didn't enjoy herself today." 
            "What was I thinking, choosing a game she clearly didn't enjoy?" 
            "I'll definitely have to pick a different one next time."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3
    
    scene bg kitchen_sunset
    play music t2
    "It’s Sunday, and for some reason I feel particularly off." 
    "I’m excited for Sayori’s visit, but I feel ill..." 
    "I walk over to the kitchen and grab the thermometer off the counter."
    "I place the thermometer in my mouth and wait about a minute before it starts beeping."
    "101.2 degrees? Great." 
    "I go into the cabinet to pull out some medicine, but the door bell conveniently rings."
    "I put down the medicine, run over to the door, and open it."
    "As expected, Sayori is here."
    "She looked happy at first, but after taking a glance at me, she began to look worried."
    mc "Hey, Sayori..."
    show sayori s2bo at t11 zorder 2
    s s2bo "[player]? You look awful!"
    mc "Yeah, seems I've caught a cold..."
    s s4bm "That's terrible!"
    s s1bj "You need some proper care, [player]! I'll help you get all better!"
    mc "I’ll be fine. I’m more concerned about you getting sick."
    s s2bh "Silly [player]! You need someone else to take care of you!"
    s "What would I do if something happened to you?"
    mc "Sayori..."
    "Sayori worries so much for me..."
    "I find it great that she cares so much, but I don't want her to get sick!"
    menu:
        "I guess I might as well..."
            
        "Let Sayori in.":
            $ SayoriVar += 1
            mc "Alright, fine."
            mc "However, if you get sick, the blame is not on me."
            s s2bj "Trust me, [player]! I'll nurse you to good health!"
            s "Now, go lay down already so I can help you."
            "I obey her command and I lay down on the bed in my room."
            scene bg bedroom
            show sayori 1bi at t11 zorder 2
            "She throws the covers over me and makes sure I stay warm."
            s s1bi "There we go! Now, I’m going to get you something warm to put in you, so you can feel better. Stay here, alright?"
            "Did she just say \'something warm to put in you\'?"
            show sayori at thide zorder 1
            hide sayori
            "I don't have time to question her as she's already left."
            "I sit here for about a minute until I see her come back in, medicine in hand."
            show sayori 1bc at t11 zorder 2
            s s1bc "Hey [player], this medicine is yours, right? I found this on the counter." 
            mc "Sayori, who else would the medicine be for?"
            mc "I'm the only one here."
            s s4br "Oh right, my bad! Ehehe~"
            "Sayori hands me the little cup filled with medicine."
            "I brace myself..."
            "Grape flavored. Never liked this stuff."
            "I swiftly down the medicine as quickly as possible."
            "Disgusting, but I know this will make me feel better."
            "I quickly notice afterwards that Sayori is holding my once empty hand."
            mc "Sayori?"
            s s1bn "Oh, I'm sorry [player]!"
            s s2bc "I’m just trying to… keep your pulse in check."
            mc "Sayori..."
            mc "You know that's not how pulses work, right?"
            s s2bo "Ah..."
            s s3bt "I'm just trying to warm you up!"
            s s3bs "I wouldn't want you to get even worse..."
            "I smile at the fact that Sayori is trying so hard to hide her true intentions."
            "I squeeze her hand and she starts to blush."
            s "[player]..."
            mc "It's okay, Sayori." 
            "She smiles at me for a bit, but a huge sneeze ruins the moment."
            "She pulls her hand back immediately."
            s s2bw "Oh my gosh, you need tissues!"
            s s1bg "Where do you keep them?"
            mc "Right there, over on my desk."
            "Oh no..."
            "I left the lotion next to the tissues!"
            "I pray to every god I can think of that she doesn't notice why it's there."
            "She goes up to my desk, grabs the tissues, and returns to my bed."
            s s1ba "Here you go, [player]!"
            mc "T-Thanks..."
            "It seems like she didn't notice..."
            "I sigh a huge breath of relief."
            "After that, Sayori grabs the TV remote and turns the TV on."
            s s2bd "Watching some of my favorite shows always cheers me right up when I'm sick!"
            mc "Great, now this really is a hospital."
            mc "Bedbound, TV on, nurse tending to my needs."
            s s1bq "Well you ARE sick, silly~!"
            s s1br "What show do you wanna watch?"
            mc "It doesn't matter to me." 
            mc "You can pick if you like."
            "With that, she flips over to Italyball." 
            "Not exactly my kind of show, but the humor isn’t half bad." 
            "She seems to really like it."
            "I guess when I see her like it, it makes me a bit happy." 
            "The way she smiles when a stupid joke comes on."
            "How she seems to get confused when there’s a WWII reference she doesn’t get." 
            "It's kind of adorable." 
            s s1bu "[player]?"
            "I suddenly jump back into reality."
            mc "Huh? Oh, Yes, what’s up, Sayori?"
            s "You've been staring at me..."
            s s1bn "Is something wrong?"
            mc "Ah, sorry..." 
            mc "I just spaced out..." 
            mc "Did I make you uncomfortable?"
            s 2bs "Oh no! You didn't make me uncomfortable!"
            s 2bt "I was just wondering, that's all!"
            mc "Ah, okay."
            "With that, we turn back to the TV and continue watching."
            "I actually get somewhat warped into the show."
            "It's pretty good, now that I pay more attention to it."
            "This doesn't last long, as a feeling in my hand takes me out of it."
            mc "Sayori?"
            "I glance over to see Sayori holding my hand."
            "I look up and see her blushing extremely hard."
            s s1bl "[player]…" 
            s s4bd "Thank you for letting me take care of you." 
            s "I really wouldn't know what to do if I hadn't been able to help you..."
            s "Even if it takes me getting sick, I'd always want you to feel better."
            mc "Sayori..."
            mc "Of course I'd let you help me."
            mc "I just don't want you getting sick, so please be careful, alright?"
            s s1br "Don't worry, [player]!"
            s "I'm sure I have a strong immune system!"
            s "I definitely won't be getting sick!"
            mc "I'll be holding you to that, then."
            "We sit like this and continue watching the show."
            "Time flies, and before I know it, the sun starts setting."
            s s2bv "The sun is going down already?" 
            mc "Seems to be so."
            mc "Sayori, you should go home now, it's not safe to be out late at night."
            s s1bu "Awww, alright..."
            s s1br "Bye, [player]. Get well soon, alright?"
            mc "I’ll get better as long as YOU don’t get sick. That work?"
            s "Yeah! It's a promise~!" 
            s s1bs "Alright, then see you tomorrow!"
            show sayori at thide zorder 1
            hide sayori
            "With one last smile, she lets go of my hand and starts walking down the stairs."
            "She walks to the door, but not before letting a sneeze out."
            "I hear her quickly open and shut the door."
            "Great."
        "Tell her to come back next week.":
            $ SayoriVar += 1
            mc "Sayori, I won't have you getting sick!"
            mc "You should go home."
            s s1bv "Awwww, alright..."
            s s1bw "Just, please feel better okay?"
            mc "Don't worry about me."
            mc "I'll be just fine." 
            "She starts to walk off."
            "As she's walking, she looks back at me."
            "I can tell she's extremely worried for me."
            "I start to feel bad for her."
            "It's for her own good, though!"
            "She cannot be getting sick under any circumstances!"
            "I hope she'll be okay..."
    
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    pause 3
    
    scene bg livingroom_sunset
    play music t2
    "It's yet again the first day of the week, and I've been sitting on my couch waiting for about an hour now."
    "I was about to text Sayori, asking her what's taking so long, when I get a notification telling me that she's already given an answer."
    s "Hey, sorry, I won't be able to show up. I'm a bit sick today."
    "I read over the text one more time."
    mc "Do you want me to come help you?"
    s "[player]... I'll be fine. I think."
    "I mull over her text in my head. Should I listen to her, or should I go over and help her? She does keep her door unlocked, after all..."
    menu:
        "I decide to..."
            
        "Go help Sayori.":
           $ SayoriVar += 1
           "I text her back."
           mc "Don't be silly. I'll be over in 5 minutes. The door's unlocked, right?"
           "I wait one or two minutes. I imagine she's thinking over her response."
           s "You really don't have to... but yes, it's unlocked. I'll see you here."
           scene black
           "Without hesitating, I walked over to her house and opened the door."
           "I went directly to her bedroom."
           scene sayori_bedroom_sunset
           show sayori s1bc at t11 zorder 2
           play music t8
           "I open the door to see Sayori laying in bed, room messy as ever."
           "I walk over to her and crouch by her side."
           "Hey, Sayori?"
           "What's wrong?"
           s s2bf "My... my head, [player]..."
           "Before I let her finish, I put my hand on her head. She's burning up..."
           mc "Oh, god, Sayori, yea, you are sick..."
           mc "Do you have a thermometer or something like that?"
           s s2bh "In the drawer, maybe."
           "She points to her dresser and moans slightly, probably from pain."
           "I can tell it's straining her just to talk."
           "I go over to the drawer, and slide it open."
           "The stuff inside nearly jumps out at me."
           "I suppose a mess is no less than what I should have expected from Sayori."
           "I rummage around, hoping my hand won't be lost forever in the abyss that I'm staring long into."
           "I feel around for what seems like a thermometer, and luckily enough that's exactly what it was."
           "I uncap the end and stick it in Sayori's mouth."
           s s2bc "Mmph!"
           "The device beeps."
           "101.4!"
           mc "Jesus, Sayori, you're on fire!"
           s "Unf... is it really that bad?"
           mc "Yeah, no kidding!"
           "I shuffle Sayori's blanket off of her as quickly as possible, which makes her shudder."
           show sayori s1bp
           "I try to think back to all the home remedies that my mom used on me."
           mc "Let me get a towel to put on your forehead."
           mc "I assume there are some in the closet here?"
           "I go to open the door to the closet when Sayori screams out... to the best of her ability, anyway."
           s s1bm "NODON'TGOINTHERE!"
           "I turn back, confused."
           s s1bl "I mean... the towels are over in my bathroom. Ehehe..."
           "She seemed a bit... enthusiastic about telling me that information."
           "So much so that it overrode her sickness."
           "I decide it'd be better for both of us if I don't think about the contents of this closet."
           "I go over to the bathroom and soak the towel in cold water."
           "I come back and cover her head with the towel."
           s s1bq "Mmm... thank you, [player]..."
           mc "You're welcome."
           mc "Hey, should I make you something to eat?"
           s s1bb "You know I could never say no to food!"
           mc "Alright, let me see if you have anything downstairs then."
           hide sayori
           scene bg h_livingroom
           "I go downstairs to her living room."
           "Now that I'm awake enough to observe it, something about it seems familiar..."
           "Eh, it's probably nothing."
           "I go into her kitchen..."
           scene bg h_kitchen
           "Which also looks strangely familiar."
           "Hmm."
           "Anyway, I open up her cabinets, and see some chicken soup."
           "Should I really give this to someone with a fever?"
           "..."
           "Eh, it'll be fine."
           "I warm up the soup on the stove."
           "It doesn't take too long. I put it in a bowl, grab a spoon, and return upstairs."
           scene bg sayori_bedroom_sunset
           show sayori s1bh at t11 zorder 2
           s "Oh!"
           s "Thank you, [player]."
           "I hand her the soup."
           mc "Careful, it's a bit..."
           s s1bp "Owowowowoowowowowow!"
           mc "... hot."
           "Sayori starts fanning her tongue with her hand."
           "I grab the soup from her and put it on her dresser."
           mc "Let's just wait for this to cool off."
           "I take Sayori's temperature again. Despite the burn on her tongue, she's down to about 99 degrees."
           mc "Alright, Sayori, if you're not feeling better by tonight, text me again, okay?"
           mc "You're at a safe temperature, so I'm going to go home."
           s s1bl "Thank you for coming over, [player]..."
           s s1bk "I just hope you don't get sick..."
           "I go over to Sayori and kiss her on the forehead."
           "I have no idea what came over me, it just sort of happened."
           "..."
           "An expression of shock, then acceptance, goes over her face."
           mc "I'll be alright, Sayori, don't worry."
           s s1bg "A-alright. Goodbye."
           mc "Sayonara, Sayori!"
           "I leave her house."
        "Listen to her and stay home.":
            "I listen to what she asks of me and sit at home."
            "I get up to my normal activites, watching TV, lazing around on the internet, things of that nature."
            "I can't help but feel a sense of guilt in the back of my mind."
            "A feeling that maybe I should have helped her out..."
            "Oh well. She'll be fine..."
            "Right?"

   
    scene bg residential_day
    play music t5_sayori
    "Sundays have been amazing."
    "It’s our 6 month anniversary and to be honest..."
    "That kind of feels like an achievement or something." 
    "It’s hasn't been too long since she's been coming over."
    "However, it's felt like it's been forever." 
    "Even if we’ve been friends since childhood..." 
    "This feels… completely different." 
    "That's what love is, isn't it?"
    "A doorbell suddenly interrupts my thinking."
    "I walk over to the door and open it."
    "As expected, Sayori is standing there."
    "She looks as cheerful as ever." 
    show sayori 1br at t11 zorder 2
    s "[player]!" 
    mc "Hey, Sayori!"
    s 1bc "[player], guess what?"
    mc "… what’s up?"
    "Her eyes seem to be lighting up."
    s 1bd "Come on, you have to guess!"
    mc "You could at least give me a hint…"
    s 1bx "It’s about us!"
    "It's about us?"
    "I can't figure out what she's talking about." 
    mc "Sorry, Sayori..."
    mc "I really have no idea."
    show sayori 1bs at face zorder 2
    scene black
    "Sayori runs up and grabs me unexpectedly."
    show sayori at thide zorder 1
    hide sayori
    s "Today's our 6 month anniversarrrry!"
    "Sayori hugs me even harder than before, almost lifting me up."
    "I didn't think she was this strong."
    "She lets go, and I take a breath and speak up."
    scene bg residential_day
    show sayori 1ba at t11 zorder 2
    mc "Yeah, it is!"
    mc "You seem extremely excited about this."
    s 1bq "Yup, I am!" 
    s 2br "Cause now that we're here..." 
    s "We get to shoot for one year!"
    s 1bs "Then maybe even one hundred years!"
    s "AND THEN, maybe even one thousand years!"
    mc "Sayori..."
    mc "It's rare for a human to live to one hundred years, let alone a thousand of them."
    s 1bt "I don't know, but we can sure try!"
    mc "Maybe you should just start coming over on other days, too..."
    "I say that out loud without thinking."
    "I realize that may have been a bit weird to say..."
    s 3bx "Yeah, you're right, [player]!"
    "She doesn't seem to think so."
    "That makes me happy."
    mc "Maybe..."
    mc "Maybe you could come every day of the week?"
    s 4bt "Of course, [player]!"
    s 4br "I'd love to spend any day with you~!"
    mc "I'd love that, myself."
    mc "Let's go inside, now."
    s 2ba "Alright!"
    scene bg livingroom
    with wipeleft_scene
    "We both walk in to the living room and sit down on the couch."
    "Sayori seems a bit off..."
    "She's somewhat glaring at me."
    mc "Everything alright, Sayori?"
    s 3bc "Oh, I’m alright, [player]."
    s "Just… wondering what we’re gonna do today, ehehe!"
    mc "Oh! Yeah..." 
    mc "Want to just go upstairs and watch some anime?"
    s 2bd "Sure thing!"
    "With that, we both head upstairs." 
    "I keep my eye on Sayori as we walk up." 
    "Her answer didn't seem genuine..." 
    scene bg bedroom
    with wipeleft_scene
    "We finally end up in my room."
    "I grab the TV remote and turn the channel to something that looks interesting."
    "Sayori sits down on my bed and I sit down on my desk chair."
    show sayori 1bb at t11 zorder 2
    s 1bb "[player]! Don’t you want to sit next to me?"
    mc "O-on my bed, Sayori?"
    s 3ba "Of course!"
    "I realize she probably doesn’t get the implications."

    "I get up and sit next to Sayori on the bed." 
    "We’ve both got our backs against the wall, so that our legs just barely dangle over the end of the bed." 
    "Sayori pulls me in closer and hugs me tightly."
    mc "Sayori...?"
    s 2bg "Oh, sorry [player]..."
    s 2bk "I just wanted to cuddle a bit..."
    "She lets go and puts her arms to her sides."
    mc "Oh no, It's not that I have a problem with it..."
    mc "It just caught me off guard."
    mc "We can cuddle all you want."
    show sayori 2bd at t11
    "Sayori smiles and puts her arms around me again."
    "This feels so warm..."
    "But in any case, I want to focus on the show." 
    if SayoriVar >= 3:
        "As we watch the show, I notice that she doesn't seem to be paying attention." 
        "She seems to be thinking about something."  
        "She looks kinda happy?"
        "I decide to finally stop questioning and just ask."
        mc "Hey, Sayori?"
        s 2bf "Yeah, [player]?"
        mc "Are you doing okay?"
        s 1bt "Oh yeah, I'm doing just fine, don't worry!"
        mc "Sayori, I don't think I can believe you."
        mc "You haven't been paying attention to the show at all."
        mc "You need to tell me what you've been thinking about."
        mc "Or do you want me to stop hugging you?"
        s 2bw "No, please don't!"
        "Sayori holds me tighter than she ever has before."
        s 2bp "Please don't leave..."
        mc "I won't, I won't."
        mc "But please explain to me what's going on..."
        show sayori 2bv at t11
        "Sayori thinks for a moment."
        "She lets out a huge sigh."
        stop music fadeout 1.0
        play music t10
        s "[player]..."
        s "The rainclouds haven't gone away."
        s 2bu "I still feel pain every time I wake up."
        s "It hurts so much, forcing myself to get up everyday..."
        "My heart plummets when I hear this."
        "I haven't exactly forgotten that she deals with depression..."
        "But it's so hard to tell with how happy she looks and sounds."
        mc "Sayori..."
        mc "I'm so sorry..."
        mc "I should've known better than to threaten to get up."
        s "No, it's not your fault!"
        s "The reason I say this..."
        s 1bt "There's a reason why I force myself to get up every morning."
        s "A reason why I can deal with the pain I feel..."
        mc "B-Because of school...?"
        s 1br "Of course not, ehehe!"
        s "I do it because of you."
        mc "M-Me?"
        mc "You get up because of me?"
        s 1bq "Of course."
        s "When I struggle to get up out of bed..."
        s "I just think of how you're going to be there, at school, waiting for me."
        s 1bx "I think of what's going to happen on Sunday."
        s "I think of how happy it makes me to be with you."
        s "Even at my lowest points, when I feel like ending it all..."
        s 1bt "My thoughts of you keep me from dangerous things like that."
        s "I guess you could say you're the reason I'm alive."
        "Hearing this stuns me."
        "I'm the reason she's alive...?"
        mc "Sayori..."
        mc "Thank you for not ending your own life..."
        s 2bu "Oh no, don't thank me, [player]!"
        s "You're the reason I didn't do it."
        s "You should be thanking yourself!"
        "I have no idea what to think."
        "Sayori could've died."
        "And yet, she's alive, thanks to me..."
        s "[player]...?"
        mc "Yeah, Sayori?"
        s 1br "I love you."
        "My heart starts to beat frantically."
        s "I love you so, so much."
        s 1bs "I love you till the ends of the universe!"
        mc "I..."
        mc "I love you too Sayori."
        mc "I'm so glad that I was the reason you didn't do anything rash."
        mc "I don't know what I would've done if you were gone..."
        s "R-Really?"
        mc "Of course."
        mc "Ever since we were kids, I've always loved you."
        mc "It wouldn't be right if you weren't here with me."
        mc "Things just wouldn't be the same..."
        s 1bt "You've loved me for that long...?"
        mc "Yes, I have."
        mc "And that love I feel has never gone away, not even slightly."
        s "You've loved me for that long."
        s 2bc "I guess I have, as well."
        s "I just never realized it."
        s "I've always wanted to do something for a while, as well."
        mc "Oh? What's that?"
        scene black
        show sayori at thide zorder 1
        hide sayori
        "She suddenly springs up and kisses me on my lips." 
        "I get caught by surprise, Sayori usually isn't this forward."
        "I slowly ease into it, however."
        "Her lips taste like strawberry."
        "Did she take the time to put on lip gloss?"
        "I can tell Sayori is really into it."
        "Her eyes are closed and her breathing is shallow."
        "I can hear her make small noises."
        "I put my arms around Sayori and start to push my body against hers."
        "This feels incredible..."
        "We finally release, catching our breath."
        scene bg bedroom
        show sayori 4bs at t11 zorder 2
        "She looks at me and smiles."
        "I smile back."
        mc "I could get behind doing this for a million years..."
        s 4bs "That would be amazing!"
        mc "It's too bad we can't live that long..."
        s 4bo "You don't think we can live for that long?"
        mc "Well, of course not."
        mc "What IF we can't?"
        "Sayori gets closer to me. The look she's giving... something's off about it."
        s 1by "Hey, [player]? We are on your bed..."
        mc "S-Sayori...?"
        s 4bx "Maybe I can put what Yuri taught me to good use~!"
        "I gulp. What did Yuri teach her?"
        scene black
        with dissolve_scene_full
        stop music fadeout 2.0
        play music tbc
        window hide
        pause 2.902
        show tbc at r11 zorder 2
        show image "mod_assets/pink.png"
        pause 10.0
    elif SayoriVar >= 0:
        "We continue to watch the show."
        "It doesn't seem like Sayori is paying attention, but I didn't want us to stop cuddling."
        "It feels so warm and amazing."
        "Before I know it, the sun is setting."
        s 4bx "Well, [player], it's time for me to go!"
        s 1by "Thanks for having me again, I loved it so much~!"
        mc "Sure thing, but maybe I should choose a different show next time!"
        mc "You seemed more focused on the cuddling than the show itself!"
        mc "Not that I didn't mind the cuddling, of course."
        mc "That felt amazing."
        s 1bh "Oh, sorry [player]!"
        s "I didn't dislike the show..."
        s 2bj "I just had a few things on my mind."
        mc "Alright, as long as you're okay."
        s "I am just fine, [player]!"
        s 2ba "You worry so much about me, ehehe~"
        mc "We are a couple, so of course."
        mc "If I don't worry about you, who will?"
        s "I... guess you're right!"
        "What I said sounded completely different in my mind..."
        s 1by "Bye, [player]!"
        mc "See you, Sayori!"
        mc "I'll see you tomorrow, right?" 
        "I feel uneasy saying that."
        "However, that feeling goes away as Sayori seems to be back to normal."
        s 1bd "You'll be there when I wake up, right?"
        mc "Make breakfast for us and it's a deal!"
        s "Deal!"
        show sayori at thide zorder 1
        hide sayori
        "With one last hug, she leaves." 
        scene black
        with dissolve_scene_full
        stop music fadeout 2.0
    else:
        hide sayori
        scene black
        "No, you know what, stop the mod."
        "You got NONE of the damn choices correct."
        "Are you fucking serious?"
        "You download a goddamn mod to turn DDLC into a normal fucking VN, and you fuck up your choices."
        "You goddamn limpdick retard."
        "Its not hard to do a route. All you gotta do is think for once in your goddamn life and press a button or two correctly."
        "You've got to be mentally disabled or some shit to mess up that badly!"
        "Here, let me explain something, you dumb cunt."
        "This mod has been tested with every age group, multiple times."
        "So, you can be excused if you are in the following age groups:"
        "1.{i}The Infantile{/i}."
        "2.{i}The Elderly{/i}."
        "3.{i}Fuck you, there is no three{/i}."
        "If you're one of those two, and you got here, that's understandable."
        "This next part doesn't apply to you."
        "If you're literally any other age group, though..."
        "Then, holy shit, you have to be every type of disabled possible."
        "Listen up, Dicksuck McCocklicker."
        "I understand that some of these questions were a bit of a hard decision."
        "In fact, I gave you two choices of leeway to account for this."
        "That's right, cum gargler."
        "You could have gotten two of them wrong, and you'd still be fine."
        "But nope."
        "But you decide to fuck off and be a socially disabled cuck who can't even get a girlfriend in a goddamn dating sim."
        "How fucking pathetic are you?"
        "You managed to get EVERY FUCKING ONE wrong."
        "I've met fucking vegetables who are smarter than you!"
        "Frankly, i'm surprised that you were smart enough to install the mod."
        "You came in here expecting your doki to go all like:"
        "\"Oh [player]! I love you! I love you, I love you, I love you!\""
        "But you had to go and get everything utterly fucking wrong like a retard!"
        "I bet you have more fucking chromosomes than brain cells!"
        "For real, what the fuck is wrong with you?"
        "Did you just do this out of interest?"
        "Did you just want to see what I would say?"
        "Well, great going asshole."
        "Here's what I have to say:"
        "You are a fucking dumbass."
        "And guess what, mega cuck?"
        "You don't even get to go on to the next episode."
        "Fuck you."
        "Eat my dick, ass chewer."
return

