label natsukiroute:
    $ NatsukiVar = 0
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "I walk into the literature club and the usual scene greets me." 
    "Yuri’s sitting at her desk, reading a book, and Natsuki and Sayori are talking about something. Monika’s late again."
    "I walk over to Natsuki and Sayori, asking what they're on about."
    call groupStart()
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
    call groupClear()
    call groupStart()
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
    
    
    call groupClear()
    scene bg house 
    with dissolve_scene_half
    pause 1.5

    play music t3
    "It’s Monday, and time for the school festival."
    "I’ve always enjoyed these, as they were essentially a day off from school, but I never got involved in anything like this."
    "I can’t believe I have to read out a poem!"
    "I’m still not even that proud of the one I chose!"
    show natsuki 1a at t11 zorder 2
    "Natsuki’s over, helping me carry the cupcakes to school."
    "It’s so many though, that we need help even from Sayori."
    "We’re standing outside her door, and so far, she hasn’t come out."
    "It seems she overslept again."
    "I suggest moving on."
    "I still don’t feel very comfortable doing it, but I’m not going to be late because of her."
    show natsuki 1z zorder 1 at t42
    n "I’ll go wake her up, [player]."
    n "I’m good at this type of thing."
    "I nod, and she goes in."
    "I set my bookbag down, lay against the fence and start to doze off."
    show natsuki at thide zorder 1
    hide natsuki
    
    "Just about 30 minutes later they come out, ready to help."
    "They pick up their trays and we walk together to the festival."
    stop music fadeout 2.0

    scene bg club_day
    with wipeleft_scene
    play music t3
    
    "We arrive at the festival 20 minutes late and immediately set Natsuki's cupcakes on a nearby table."
    "Thankfully not much happened during our absence, but some of the stage was already set up."
    "How Monika, Yuri, and Natsuki got a piano into the room is a mystery for the ages."
    "..."
    
    scene black
    with dissolve_scene_full
    
    scene bg club_day
    with wipeleft_scene
    
    "Half an hour later and we're finished."
    "To celebrate our good work Sayori and I both take one of Natsuki's cupcakes."
    "Sayori immediately stuffs it into her mouth while I take a moment to inspect Natsuki's latest design."
    "Instead of the traditional swirl or kittens on top, she's shaped the icing into closed books," 
    "Each one uniquely decorated to mimic the cover of famous novels from around the world."
    "Quite fitting of the club's theme."
    call groupStart()
    show sayori 3r zorder 2 at f21
    show natsuki 5j zorder 3 at t22
    s "Wow, Natsuki, these are really good!"
    show natsuki 5k
    s "They might even be your best batch yet!"
    show sayori 3q at t21
    show natsuki 5t at f22
    n "{i}Aww{/i}, thanks!"
    show natsuki 5s at t22 
    mc "Seriously."
    mc "I'm impressed with how the icing's done."
    mc "Something this intricate must've taken a lot of time, effort, or both."
    show natsuki 2q at f22
    n "Well, duh!"
    n "I've gotten a lot of practice with this kind of thing by now."
    n 4l "It's really not that hard once you've done it a few times."
    n 2i "Don’t sell yourself short, either."
    n 2q "You did g-{nw}"
    n 2w "You did g-{fast} alright, too."
    show natsuki 5s
    "Natsuki suddenly turns a bright shade of red and speaks under her breath."
    show natsuki 5q at d22
    n "I just hope that everyone else is as impressed by them as much as you guys are."
    show natsuki 5s
    "Yuri and Monika both walk over and each take a cupcake as well."
    show yuri 2m zorder 4 at t44
    show monika 2j zorder 3 at t43
    show sayori 3q zorder 5 at t41
    show natsuki 4h zorder 2 at t42
    "We all take a few moments to enjoy their rich flavor and show Natsuki our gratitude."
    show monika at t43
    show sayori at t41
    show natsuki at f42 zorder 6
    show yuri at t44
    n 2y "Geez, I’m glad that you guys like 'em so much..."
    n 2z "...Just make sure that you save enough for our guests too, alright?"
    show monika at t43
    show sayori at t41
    show natsuki at t42
    show yuri at t44
    mc "Speaking of guests, has anyone signed up to join the club yet?"
    show monika 3l at f11 zorder 1
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show sayori at thide zorder 1
    hide yuri
    hide natsuki
    hide sayori
    m 1n "No, not so far."
    m 2b "But then again, the festival hasn’t really picked up yet either."
    m 3g "All in due time, I suppose."
    m 2e "..."
    m 2d "We haven’t started to read any of our poetry yet either."
    m 4d "Speaking of which, do you have your poem on you, [player]?"
    show monika 4c
    "I finish the last bite of my cupcake and reply."
    mc "Oh yeah, it’s right here in my bookba-"
    "I cut myself off."
    "I suddenly come to realize the now apparent emptiness where my bookbag should be."
    show monika 1f
    mc "Err... I mean... {i}I did...{/i}"
    show monika 1e
    mc "I must've set it down somewhere when I was waiting for Sayori."
    m 4d "Well... that isn’t very good."
    m 2d "We don't have time for you to run back and grab it..."
    show monika 2c
    "Monika turns from me to address the rest of the club."
    m 2d "Does anyone have a poem that they can lend to [player]?"
    m 4d "He seems to have forgotten his."
    show monika 2m
    "She casts me a quick aside glance as she continues."
    m 2n "You know, the main event of the day and everything...?"
    show monika 2m
    "Monika's having fun guilt tripping me, I think."
    "Its not like I did it on purpose..."
    "Suddenly Sayori steps into the conversation in my defense."
    show monika 1d at t21
    show sayori at f22
    s 4p "Hey, there's no need to pick on [player] like that!"
    show monika 1g
    s 5c "For the record, I forgot my poem too, so he's not the only one!"
    show monika at f21
    show sayori at t22
    m 2i "Sayori, that's not something that you should feel proud of."
    show monika at t21
    show sayori at f22
    s 5b "{i}B-But!!{/i} I just... forgot. Ehehe~"
    show monika at f21
    show sayori at t22
    play music t7
    m 4i "You can’t just go forgetting things like that Sayori!"
    m "Not only are you both late because {i}YOU{/i} overslept, but now {i}TWO{/i} of us don’t even have anything to read to our guests!"
    m "You're supposed to help me run the Literature Club, but the truth of the matter is that in the end you not only skirt your responsibilities, I even get stuck pulling your slack on top of that!"
    m "When you do things like that do you ever think about how much work you're leaving for everyone else?"
    m "How are we supposed to attract new club members now?"
    show monika 2h at t21
    show sayori at f22
    s 5d "W-well its not like my reading was going to attract anyone new to the club anyway, so really, I don’t count!"
    show monika 2p at f21
    show sayori 4n at t22
    m "Sayori, did you leave your poem behind just so that you wouldn’t have to read it in front of everyone today?"
    show monika at t21
    show sayori at f22
    s 1v "What?"
    s 1w "Of course not, why would I do that?!"
    s "I didn't even sleep in today, I actually got up early for once!"
    s "I was late this morning because I couldn't find where I left my poem!"
    s "I even told [player] that when I was apologizing to him!"
    s 1v "I wouldn’t lie about something that..."
    show sayori at t22
    "Oh... so that's what she mentioned she was looking for earlier..."
    "She was speaking so fast I didn't even catch that."
    show monika at f21
    m 2l "...Don't play dumb with me."
    m "You're just trying to save face in front of the club right now, aren't you?"
    show sayori 4w at h22
    m 5b "I'm honestly ashamed of your behavior, {i}ex-{/i}vice president!"
    "At this point a crowd of students has been gathering at the door, taking an interest in the unfolding drama."
    "Several of them slowly file into the classroom for a better view."
    "A couple of the braver ones sneak further in and enjoy one of Natsuki's cupcakes as they snicker at us."
    "Natsuki steps in."
    show sayori at thide zorder 1
    hide sayori
    show monika 2d at h21
    show natsuki at f22 zorder 5
    n 2w "Hey, you leave Sayori alone!"
    n "I didn’t want to read any of these dumb poems either."
    n 2x "In fact, none of us did!"
    n "You're the only one who wanted to go through with this dumb idea in the first place, Monika!"
    show monika 1h at f21 zorder 6
    show natsuki 1u at t22
    "Monika glares at Natsuki for a moment before speaking again."
    m 2i "I’m sorry; Natsuki, and here I thought that you were confident enough to read in front of everyone, but I guess that's not really the case after all."
    show monika 2h
    "Wow, I've never seen this side of Monika before."
    "Honestly, I'm pretty shocked."
    "She seems rather... irritable, to say the least."
    "Perhaps it's because she's under pressure?"
    "Being in public like that..."
    "And Natsuki isn’t having any of that."
    show monika 2h at t21
    show natsuki at hf22 zorder 7
    n 5e "Oh? {i}OH?!{/i}"
    n "I’m sorry; Monika, and here I thought that you were the kind of leader that listened to her club members when they voiced a concern, but I guess not!"
    n 5f "Some club president YOU are!"
    show monika at f21 zorder 8
    show natsuki at t22
    m 2i "Natsuki, in case you weren’t listening, no one's asking for your opinion."
    show natsuki 4r
    m 5b "{cps=*.5}So if you don't want to do anything for the festival, then why don't you just go read manga by yourself in the corner like you usually do?!{/cps}"
    "Okay, things are getting {i}way{/i} too out of hand here!"
    "I'm trying to think of a way to stop the argument but I don't even know where to step in."
    "Thankfully, Sayori tags back in for Natsuki."
    show monika 2h at t31
    show sayori 1v at f33
    show natsuki at t32
    s "Well then, I-I’ll ask her now!"
    s "Natsuki, what’s your opinion?"
    show monika at t31
    show sayori at t33
    show natsuki at f32 zorder 9
    n 4y "Why, I’m glad that you asked, Sayori!"
    n "At least {i}SOMEBODY{/i} cares about the rest of the club's opinions..."
    n 2x "...And in my opinion, Monika’s being an awful jerk!"
    show monika at f31 zorder 10
    show sayori at t33
    show natsuki at t32
    m 2i "And in {i}MY{/i} opinion neither of you really care all that much about the Literature Club after all!"
    m "Maybe that can change someday in the future, but I doubt it."
    show monika at t41 zorder 1
    show sayori at t43 zorder 3
    show natsuki at t42 zorder 2
    show yuri at f44 zorder 4
    y 2n "G-guys..."
    $ m_name = "Everyone"
    show monika 5b at f41
    show sayori 4j at f43
    show natsuki 1e at f42
    show yuri at t44
    m "Stay out of this, Yuri!"
    $ m_name = "Monika"
    show monika at thide zorder 1
    show sayori at thide zorder 1
    show natsuki at thide zorder 1
    hide monika
    hide sayori
    hide natsuki
    call groupClear()
    show yuri 1o at t11
    "Yuri squeals and quietly backs away from the other girls."
    show yuri 1p at t11
    "As she backs up she accidentally bumps into one of the other students and finally takes notice of the growing crowd, furthering her embarassment."
    show yuri at thide zorder 1
    hide yuri
    call groupStart()
    show natsuki 2x at t32
    show sayori 4p at t33
    show monika 5b at t31
    "I turn to the other club members and gather my confidence."
    "There's only one thing to do..."
    "...Welp, here goes nothing..."
    stop music fadeout 5.0
    show natsuki 1o at h32
    show sayori 4m at h33
    show monika 1d at h31
    mc "{i}HEY!{/i}"
    "The sudden shout jolts them out of their squabble."
    mc "You’re making a mockery of your own club!"
    mc "We've succeeded in drawing a crowd, but not in the way we wanted to!"
    mc "So can all of you stop your pretentious bickering and get your acts together?!"
    "Wow, I-I think I actually did it."
    show natsuki 5q
    show sayori 5b
    show monika 1q
    "Natsuki opens her mouth to retort, but she takes one look at me and quickly closes it."
    show natsuki 12b
    "At this point the crowd has mostly dispersed already, although a few students stuck around to thank Natsuki for the cupcakes."
    "Even from here it’s noticeable that our signup sheet was just as empty as when we started..."
    call groupClear()
    pause 1.5
    scene bg club_day
    with dissolve_scene_full
    play music t8

    show monika 3i at f11
    m "So, does everyone understand {i}why{/i} this club’s still at square one?"
    call groupStart()
    show monika 1h at t41
    show sayori 1k at t43
    show natsuki 1u at t42
    show yuri 1l at t44
    "The rest of us look down at the floor in disappointment."
    show monika 1o
    "Monika follows suit."
    "She knows that she was part of the problem, after all..."
    "...even if she doesn't want to admit it."
    show monika 1f
    "Monika's eyes move up to the back of the room, lost deep in thought."
    "She takes a moment and lets out a sigh before continuing."
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    hide natsuki
    hide yuri
    show monika 1p at f21
    show sayori 3n at t22
    m "Sayori, [player]... I... I’m really sorry that I snapped at the both of you."
    m 3l "Look, I know that Sayori didn't intend to oversleep or lose her poem or whatever yesterday, and I know that you were both busy with bringing the decorations here too."
    show sayori 1n
    m "I even noticed the effort that Sayori had put into her hygiene yesterday, I was honestly impressed."
    m "Given that, I can understand how you might lose track of things when your mind's so preoccupied."
    m 1r "And if I'm being honest, I share some of the blame for that too."
    m "As the one in charge of the events I should've had you both email me your poems last night, just in case."
    m "Or something to that effect."
    m 1r "I hate to admit it, but as club leader I failed you both."
    show sayori at thide zorder 1
    hide sayori
    show monika 1q at f31
    show natsuki 5g at t32
    show yuri 4b at t33
    "She turns to the other two girls and continues monologuing."
    m 2i "And I’m sorry for yelling at the both of you too, Yuri, Natsuki."
    m 4g "I really shouldn’t have, I stepped way out of line."
    show monika 1o at f11
    show natsuki at thide zorder 1
    show yuri at thide zorder 1
    hide natsuki
    hide yuri
    "Monika turns to address the whole group again."
    m 2r "I should have listened to all of you the first time around."
    m 1p "{i}..It's just...{/i}"
    show monika 1o
    "She takes a moment to gather her thoughts again and continues."
    m 2d "...I've been working {i}so{/i} hard on getting preparations set up for this festival."
    m "I've been practicing piano for 6 hours straight {i}every single day{/i} for the past 2 weeks, plus any free time I had after class was over."
    m "I've practiced reading my poem in front of the mirror {i}nearly a hundred times{/i} to make sure that I had it memorized by heart."
    m "I posted a few dozen fliers of my own design around the school to advertise our event."
    m 1g "I even composed my own song to play as background music for everyone's poems to help them keep a rhythm to their words."
    m 1r "I had to call in a favor to borrow a piano from the music department..."
    m "...and I even spent my own money to rent a microphone, a stage light, and a video camera to make sure that this whole event would be something {i}worth remembering.{/i}"
    m 2k "I know that none of you were all that interested in performing for the festival at first..."
    m "...but I was really hoping that my enthusiasm would prove to be infectious."
    m 4k "I thought that maybe if I showed you all how much effort I was putting in that it would inspire you all to do the same!"
    m 1r "{i}...I just wanted everything to be perfect...to prove just how awesome our club is...{/i}"
    m 1q "..."
    m 1r "{i}...but I let that get in the way of what matters most.{/i}"
    m 1p "...And for that... all that I can say is... {i}I'm sorry.{/i}"
    show monika 1o
    "{i}I'm utterly taken aback.{/i}"
    "I never realized just how much effort Monika had been putting into the festival behind the scenes."
    "No wonder she was always so late to the club."
    "To think that it had kind of become a running gag for us..."
    "And on top of all that, I never expected to hear such a heartwarming apology out of her."
    "I think that we all seriously underestimated just how much the school festival really meant to her..."
    show monika at t41
    show sayori 1t at t43
    show natsuki 1n at t42
    show yuri 4a at t44
    "I want to man up and take my share of the responsibility, but how am I even supposed to follow up something like that?"
    "Oh well, here goes nothing..."
    mc "..."
    mc "I suppose I have to... apologize, too."
    mc "It was my mistake that caused everything to spiral out of control in the first place, after all."
    mc "I should've double-checked myself instead of surfing the web when I was waiting for Sayori."
    mc "So... yeah."
    mc "I'm sorry, everyone."
    show monika at t41
    show sayori at t43
    show natsuki at f42
    show yuri at t44
    "Natsuki steps forward."
    n 3w "Well, you both need to stop being so hard on yourselves, it’s dumb!"
    n 3x "Neither of you are at fault anyway, so stop feeling so guilty about it."
    n 1q "...I can understand Monika wanting everything to go smoothly for the festival, and its not really fair that we let her shoulder so much of the burden..."
    n 1x "...and even after she did all of that we {i}STILL{/i} couldn't bother to..."
    n 12a "{i}It’s...{/i}\"{space=5000}{w=0.5}{nw}"
    n 12c "It’s...{fast} {i}I really...{/i}\"{space=5000}{w=0.5}{nw}"
    n 12f "It’s... I really...{fast} {i}I’m the one who...{/i}"
    show monika at t41
    show sayori at t43
    show natsuki at d42
    show yuri at t44
    "Through the rushing of her words and the shakiness of her voice, it's clear that Natsuki's really struggling to apologize."
    show sayori 3t at t11
    "Sayori comes over and wraps her arms around Natsuki."
    show monika at t41
    show sayori at t11
    show natsuki at t42
    show yuri at t44
    s 3v "I forgive you, Natsuki."
    show monika 1g
    s "And you too, Monika."
    show monika 1f
    s "And [player]."
    s 4j "It doesn't matter that we all made some mistakes yesterday."
    s "It's not a big deal {i}as long as we’re all still friends{/i} when it comes down to it."
    show monika at t41
    show sayori 4q at t43
    show natsuki 1u at f42
    show yuri at t44
    "Natsuki dries her eye and the faintest hint of a smile starts to grace her lips."
    n 1q "{i}Yeah, well...{/i}"
    n 1t "The club might not have any new members, but we make up for quantity with quality... {i}right?{/i}"
    show monika at t41
    show sayori at t43
    show natsuki 1n at t42
    show yuri at f44
    "Yuri stops looking at her shifting feet and finally breaks her silence."
    show monika 1m
    y 2t "I... I like the club better this way."
    y 3j "I know you wanted more members, Sayori and Monika."
    y 2t "{i}But I...{/i} I don’t, really."
    y "It’s great for there to be a place just for us, where we all like each other just the way we are, and don’t have any serious drama."
    y 2j "Besides, if we can still get that heated when there's just the five of us, just imagine what could happen if there were even more?"
    show monika at t41
    show sayori 4y at f43
    show natsuki at t42
    show yuri 3i at t44
    "Sayori seriously ponders that line for a moment, something I rarely see out of her."
    s 1v "Well... I don’t wanna take on any more members if our founding members aren’t completely onboard."
    s "So, I guess that I agree with you guys."
    show monika at f41
    show sayori 1t at t43
    show natsuki at t42
    show yuri at t44
    "Monika takes a look at everyone, processing everything that's happened over the last several minutes."
    "She seems to slowly soften to the rest of the club's outlook."
    m 1p "...So I'm the only one left, {i}huh?{/i}"
    m "{i}I... guess that settles it then.{/i}"
    m 1n "No more new club members... {i}at least for the time being.{/i}"
    m 1r "..."
    m 2b "Okay, everyone."
    m "If this is the club's final decision, then that's good enough for me."
    m 4b "But I want us all to be completely open with our hearts: Are we totally sure that the Literature Club is good as is?"
    show monika 4a
    "..."
    "I decide to speak first myself for once."
    show monika 1e
    show sayori 1a
    show natsuki 1c
    show yuri 3c
    mc "I like spending every afternoon with all of you."
    mc "I don't think it could get any better than it already is, even if we had a hundred club members."
    show monika at t41
    show sayori at t43
    show natsuki 5d at hf42
    show yuri at t44
    n "{i}Absolutely!{/i}"
    n "Who needs a hundred club members when each of us is a hundred times more fun anyway?!"
    show monika at t41
    show sayori at t43
    show natsuki 1a at t42
    show yuri 2d at f44
    y "I don’t mind this at all..."
    y "...in fact, I prefer it."
    show monika at t41
    show sayori 4r at hf43
    show natsuki at t42
    show yuri 3a at t44
    s 1x "It’s honestly great just hanging out with all of you everyday!"
    s "If there were more of us then we wouldn't be able to spend all of that time together... and I wouldn’t trade that for anything!"
    show monika 1c at f41
    show sayori 1a at t43
    show natsuki at t42
    show yuri at t44
    m "..."
    m 2b "Alright everyone, its official:"
    m 4b"The Literature Club will retain its 5 member count."
    m 4b"That's just how it is."
    show monika 2a at t41
    show sayori 4q at t43
    show natsuki 5z at t42
    show yuri 3c at t44
    "Everyone beams at the news."
    m 3b "Well, no poems this week."
    m 3k "Take it as a show of good faith from me, I guess."
    show monika 1a at t41
    show sayori at t43
    show natsuki 1d at hf42
    show yuri at t44
    n "Woo! Thanks, Monika!"
    show monika at t41
    show sayori at t43
    show natsuki 4a at t42
    show yuri 2q at f44
    y "Aww. Well, alright."
    show monika at t41
    show sayori at f43
    show natsuki at t42
    show yuri 3a at t44
    s 1r "I like writing poems fine, but getting a break now and then is nice too!"
    show monika at t41
    show sayori 4q at t43
    show natsuki at t42
    pause 1
    show monika at thide zorder 1
    show yuri at thide zorder 1
    show sayori at thide zorder 1
    hide monika
    hide yuri
    hide sayori
    call groupClear()
    show natsuki 2a at t11
    "Natsuki looks over at me and we both smile."
    "We all leave the club together, before Natsuki and I split off from the others."
    
    scene bg corridor
    with wipeleft_scene
    
    show natsuki 4w at t11
    n "[player]!"
    mc "Eh?"
    n "You didn't forget about Sunday, did you?"
    mc "How could I forget that?"
    "I wink at her."
    show natsuki 1c zorder 2 at t11
    "She blushes and my heart skips a beat."
    
    scene black
    show natsuki at thide zorder 1
    hide natsuki
    with dissolve_scene_full
    
    "She walks off, heading home."
    "Even if I have been crushing on her a bit, here I was thinking Natsuki hated me."
    "Who knew that this is what she wanted?"
    "A smile begins to spread over my lips."
    "I'm so ready for Sunday."
    
    stop music fadeout 2.0
    pause 3
    scene black
    with dissolve_scene_full
    
    scene bg class_day
    with wipeleft_scene
    stop music fadeout 1.0
    play music t5_natsuki
    "I arrive at second hour, science, and walk in the doorway when I see a familiar face."
    show natsuki 1g at t11 zorder 2
    n "[player]? You’re in this class?"
    mc "Yea, always have been." 
    mc "And you? This is a second-year class."
    n 2y "No, I came because I love to walk right into other people’s classes."
    n 2w "Of course I am!"
    n 2o "I am the youngest in the club, b-but not by THAT much."
    n "..."
    n 3q "How come we never noticed each other?"
    mc "We aren’t really the kind to just walk up to each other under normal circumstances." 
    mc "I guess that’s why."
    n 1e "That only applies to you, you know!"
    n 1c "After all, I came to talk with you."
    mc "That doesn’t count, we already know each other."
    n 2h "Anyways, unless you have someone else you sit with, I-I’ll come sit with you." 
    n 3y "This is just a guess, but you’ve been sitting alone this entire time, right?"
    mc "I-I may have, but I have plenty of friends!"
    mc "They’re just not in this class!"
    n 1z "Ooof course, [player], we all do." 
    n 1t "Gosh, there’s no need to lie to me, you know."
    mc "Wow, thank you for your trust, Natsuki. You’re the best girlfriend ever. Now come sit down already."
    "I try to make sure my sarcasm is as obvious as possible. With a short giggle, she sits down, and shortly after class begins."
    show natsuki at thide zorder 1
    hide natsuki
    "About a quarter into the lecture, I feel drozy."
    "Using what's left from my strength, I gently tap Natsuki's shoulder."
    "Curious as to what I want, even when she knows we shouldn’t be doing this, she looks at me."
    "I then started whispering."
    mc "Hey, are you bored?"
    show natsuki 1s at t11 zorder 2
    n "Of course I am, but we have to pay attention."
    mc "Just for a little time..."
    mc "I feel sleepy."
    mc "I could really use some of your energy right now..."
    n 1x "{i}uuugh.{/i}"
    "Natsuki drops the pen on her notebook, and looks at me again."
    n 3u "Did you read the 3rd book of Parfait Girls?"
    mc "Actually, no I didn’t."
    mc "Something else was distracting me."
    "Natsuki and I both know what I was distracted by, but she insists on questioning me about it."
    n "What was it you were distracted by?"
    n 3y "Your hentai collection?"
    mc "Wha- I do not have a hentai collection!"
    "I yell-whisper."
    "Natsuki laughs softly."
    n 2z "Well you are a massive pervert, so it was just a safe guess."
    n 2q "What were you so distracted by then, anyway?"
    mc "I guess it was just too much video games and anime."
    "It’s a lie, but admitting I spent it all thinking about her might come across the wrong way and prove her point."
    n 1n "You’re lucky."
    n 42c "I was never allowed to play video games."
    "I’m almost sad for her."
    "A life without videogames?"
    "How could someone live on like that?"
    mc "You’ve never played video games?"
    mc "Oh man, are you missing out!"
    n 42c "I’ve played a few at the houses of a few friends."
    n "But it’s mostly that {i}jumperman{/i} game and stuff like that."
    mc "Oh man, you ARE missing out!"
    mc "Here, next Sunday I’ll show you some, alright?"
    n 2l "Wow, [player], you really like video games, huh?"
    mc "Yea."
    mc "Why, something wrong with that?"
    n 2w "No. I’m not saying that, idiot."
    n "You know I wouldn’t make fun of you for things you like."
    mc "That’s true."
    mc "Then what’s so bad about me liking video games?"
    n 1s "Nothing, I guess."
    n "It’s just that it’s nice to see you like something as passionately as I like manga."
    n 4r "It makes me feel less...weird."
    mc "I wish I could just give you the games and let you take them home, then."
    mc "But clearly that doesn’t work."
    n 2q "Shame, too. I guess that means I’ll only play it at your house."
    mc "Are we really going to meet up every Sunday?"
    n "Why not?"
    n 2w "You think that’s a problem or something?"
    mc "No!"
    mc "I just think it’s kinda funny how you can seemingly hate my guts yet still have a date with me every week."
    n 3m "I-I don’t actually hate you, idiot."
    n 3w "Though if you keep acting so stupid, I might."
    mc "Could have fooled me, but alright."
    n 2b "It’s really stupid to say, 'I love you' to someone, anyway."
    n "It’s in every romance novel and everyone does it."
    n 3d "It’s more fun to insult you, you know?"
    mc "And why’s that?"
    n "Because you get so flustered over it!"
    mc "I DO NOT!"
    "I begin to prove her point when I realize that I might have yell-whispered a bit too loud, as the teacher is now looking at us angrily."
    $ y_name = "Teacher"
    y "Natsuki, [player], hush! Pay Attention!"
    $ y_name = "Yuri"
    "She turns back to what she was doing."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki and I take one look at each other, laugh quietly, and she goes back to paying attention."
    "Another few minutes pass by when Natsuki whispers to me."
    show natsuki 12b at t11 zorder 2
    n 12b "[player]."
    mc "Hmm? What’s up?"
    n 12c "Do you think you could..."
    "She stops mid-sentence."
    mc "What?"
    "She looks down, embarrassed about something."
    n 12e "Did you write a poem last night?"
    mc "Yea. You?"
    n 12d "I kinda... didn’t. At all. Can I... use yours?"
    mc "Mine?"
    mc "Natsuki, you and I have wildly different handwriting."
    n 12a "I know, I know."
    n "I was going to copy yours down."
    n "Our handwriting is different, but our writing style is...similar."
    mc "We can’t both have the same poem, the club will know something’s up."
    n "I was kinda going to ask you to...not use yours."
    n "I understand if you won’t, but I don’t want to let the club down."
    n "Please?"
    menu: 
        "I feel bad for Natsuki, yet I really shouldn’t enable this kind of behavior. Either way, I decide that I’ll..."
        "Give up your poem.":
            $ NatsukiVar += 1
            mc "Okay, fine."
            mc "I really shouldn’t, but I will."
            n 12a "Really??" 
            n "I-I mean, you’re too nice for your own good, [player]."
            n 12b "Still, th-thank you."
            mc "You’re welcome."
            mc "But what do I say when I show up to class without a poem?"
            n "W-Well, maybe I shouldn’t..."
            mc "No, don't worry."
            mc "I'll come up with something."
            mc "I mean, I forgot mine at the school festival."
            mc "It's actually believable that I might as well have forgotten it today too."
            "She looks at me, surprised."
            n 2u "W-Well, I guess I might bake you something as a thanks."
            mc "Really??"
            n 2b "Shush, I just said I {i}might{/i}."
            mc "You’re a tiny little ball of evil, you know that?"
            n 1e "Call me ‘tiny’ or ‘little’ again and I’ll show you proof of that idea."
            mc "Okay, okay, I won’t. Sorry."
            "Natsuki returns to her notebook."
            "This time, with my poem on one side, and her blank piece of paper on the other."
            "I guess she's really going for it."
        "Scold her.":
            mc "Sorry Natsuki, but I’m not going to do that."
            mc "Write it during lunch, or just admit you didn’t do it."
            mc "I’m not going to cover for you."
            n 2f "Seriously??"
            n "..."
            n 2g "Well, at least I tried."
            n 2q "I was going to do so anyways."
            mc "Then why even ask?"
            n "I--Well..."
            mc "Huh?"
            n "Look."
            n 1q "Maybe I enjoy your writing more than my own, or something."
            n 2o "So I kinda hoped you to allow me to use one of your poems!"
            n 2w "There, I said it."
            "With that, she takes out a sheet of paper and starts writing on it."
            mc "B--But..."
            n 2i "Shush, don't talk to me."
            n 1h "You were right about this, I need to practice to get better."
            n 3g "So, don't disturb me while I'm doing it."
            "Every few seconds, she’ll get frustrated, erase for a second or two, and go back to writing."
            "Despite my stonewalling earlier, I start to feel a little bad for her."
            "I think about whether or not I should offer my poem to her after all..."
            
    "I must have lost track of time, because to my surprise, the bell rings."
    "We both pack up and leave the class."
    n 2i "Bye, [player]!"
    n 2l "See you at the literature club, alright?"
    "I wave goodbye and walk off."
    "Man, I hope Natsuki gets a little bit more honest, or else..."
    "..."
    "Come to think of it, I don't think I mind either way."
    stop music fadeout 2.0
    pause 3
    scene black
    with dissolve_scene_full
    
    with wipeleft_scene
    stop music fadeout 1.0
    
    play music t2
    scene bg bedroom
    "It’s a Sunday like any other."
    "As usual, my hopes are high for Natsuki to come over."
    "It’s only been a week, but it always ends up feeling longer, compared to the seemingly short time we spend together." 
    "Even if it’s several hours, really."
    "A knock on the door brings me back to reality, and I go to answer it."
    show natsuki 2ba at t11 zorder 2
    n "Hey."
    "Natsuki walks in as if it was routine."
    "Which at this point, it basically is."
    "I wonder how long we’ll keep this up?"
    n 2bb "H-hey!"
    n "Stop staring at me like that."
    n 2be "You’re being gross again!"
    "I realize that while I spaced out, my eyes must have rested on Natsuki."
    mc "I wasn’t staring!"
    mc "I just...got lost in thought."
    n 2be "I don’t want to know what you were thinking about, you pervert."
    n 2bw "Now, do you want to read, or did you not finish the 4th book yet?"
    mc "I...might not have gotten it done just yet..."
    n "I knew it!"
    n "Well, if you’re not gonna read it on your own, I guess I have to read it with you..."
    "She sits on the end of the bed, and I get the 4th book out from my backpack, sitting next to her."
    "I scoot pretty close, and before I know it it’s just like the literature club."
    "Laughing at the odd joke, smiling when I laugh at a joke, explaining one to me when I don’t, things like that."
    "I only notice how close we are to each other when I finally close the book."
    n 1bm "Well? What did you think?"
    mc "You have pretty good taste in manga, even if I didn’t believe it at first."
    mc "Did you bring the 5th book?"
    n 4bn "...N-No?"
    mc "What? What did you expect to do here all day?"
    n 5bw "Look, I didn’t forget it on purpose, so don’t blame me!"
    mc "Well, what do you want to do now?"
    n 2bm "Hey, you have a TV here. Let’s watch something."
    "I don’t disagree, instead getting up to reach for the remote."
    "I notice Natsuki’s a bit discomforted by my absence, but seems better when I get back."
    mc "So what do you want to watch?"
    n 1ba "There might be some anime airing."
    n "Let's watch that!"
    mc "Wait, how about a horror movie?"
    #come back here
    n "Uu..."
    n "W--Well, if you want to..."
    n "I mean, you've read my manga with me, so I guess I could..."
    "I switch to the channel, then get up to turn off the lights and close the blinds."
    n "Is this really needed?"
    mc "Horror movies are all about the atmosphere, so yeah."
    "Natsuki opens her mouth to object, but quickly closes it."
    "We missed about 5 minutes of the movie, but nothing important."
    "Its only when things really pick up that she really starts to make her presence known."
    "However, instead of speaking up about it, she puts both her arms around me and closes her eyes, seemingly out of fear."
    "It’s only when I turn around and look at her when she realizes what she’s done and moves away."
    n 42bb "I--I...I wasn't afraid!"
    n 42bc "Nor trying to get comfort by hugging you or anything like that!" 
    n "I mean it!"
    "She goes back to watching the movie."
    "I contemplate whether to save the situation or let it play out."
    menu:
        mc "Natsuki..."
        "Bring her closer.":
            $ NatsukiVar += 1
            mc "Here."
            "I bring Natsuki closer to me, circling her petite body with my arms."
            "She stays completely frozen, but moments later, she allows herself to be embraced."
            mc "If you’re scared, that’s fine."
            mc "I don’t know how I can protect you from a television, but I will if I have to."
            "With that, she looks away and back at me."
            "I smile and go back to watching the movie."
            n 2bu "[player]...?"
            mc "Hmm?"
            mc "What’s up?"
            n 2bs "Thanks..."
            n "I...I really am scared and I’m kinda glad that you’d do this for me."
            mc "You know I would, anytime. I lo...Uh, you’re the best, Natsuki."
            n 2bu "You...you are too."
            "I think that marks the first time Natsuki’s given me an actual compliment."
            "The movie ends, and we both get up."
            "Natsuki’s ready to leave."
            n 2bj "This was a lot of fun, [player]."
            n "I’m glad I come over every Sunday."
            "Natsuki’s being really nice to me."
            "What’s going on?"
        "Change the channel.":
            mc "...do you want me to change the channel?"
            n 4br "No, I-I’m fine. I wasn’t really scared, ya know. Movies don’t scare me."
            mc "If you say so. I’m continuing the movie."
            "The tension remains, but it slowly dies down as the movie continues."
            "By the time it ends, Natsuki gets up to leave."
            "She turns to me. "
    n "I’ll give you the next book tomorrow."
    n 4bw "Don’t forget to read it this time, okay?"
    n "I know you will, but don’t!" 
    "There, things are back to normal."
    show natsuki at thide zorder 1
    hide natsuki
    "We say our goodbyes and Natsuki leaves."
    "I notice that even now I still can’t tell her I love her."
    "I guess that’s alright, she doesn’t want to hear it anyway, but I still lack the confidence."
    "That sucks."
    "At least she doesn’t mind."


    scene black
    with dissolve_scene_full
    stop music fadeout 1.0
    
    
    scene bg bedroom
    with wipeleft_scene
    play music t3
    "Sunday."
    "Easily one of my favorite days of the week, for reasons that should be obvious."
    "I really should start setting an alarm, though, because I somehow managed to wake up at 11:45 today."
    "Natsuki usually shows up past noon."
    "Great." 
    "I rush through dental hygiene and struggle to get my hair combed and my face washed."
    "Once I finally end up downstairs, it’s 12:04."
    "Oh, thank god, I still have time to eat breakfa-{nw}"
    show natsuki 1bd at t11 zorder 2
    n 1bd "Hey, [player]!" 
    "Natsuki greets, opening the door."
    "I forgot I leave that open."
    "I put on my best smile and wave to her."
    mc "Hello, Natsuki."
    mc "You’re here a bit early."
    n 2bc "Well, I woke up a bit late, so I came here as soon as I could."
    n "Guess I overcompensated."
    mc "Ah, not by too much."
    mc "Well, I haven’t eaten yet, so if you’d like to sit in the living room I’ll fix myself something quick."
    n 2bq "Uhh...actually, I haven’t eaten breakfast either."
    mc "You left without eating?"
    mc "Natsuki, you have to have breakfast, it’s important."
    n "I know that, dummy!"
    n "It’s just...I uh, I wanted to show up here quick!"
    n 1bg "So shut it!"
    "Natsuki’s response is unusual, lacks the confidence her insults normally do."
    mc "Natsuki...something tells me that’s not really the reason."
    n 4bo "Well, whatever’s telling you that, it’s wrong!"
    n "That is the reason, okay?"
    n 4br "S-stop being so stupid and pay attention!"
    menu:
        mc "Natsuki..."
        "Insist.":
            $ NatsukiVar += 1
            mc "Natsuki, please."
            mc "I want the real reason."
            mc "If something’s up, I need to know."
            "She starts to get angry again, clenching her fist and almost raising it, but instead unclenches it and looks down, as if ashamed."
            stop music fadeout 1.0
            play music t10
            n "And to think I was about to hurt the person I love."
            n 2bu "I’m becoming just like him..."
            mc "’Him’? Who’s ‘he’?"
            n 1bq "My...My dad, [player]."
            n "He does that to me all the time."
            mc "Y...your dad hurts you?"
            n "Not really physically..."
            n 1bm "Well, physically too, I guess."
            n "It’s..."
            n "He got mad at me yesterday, so he hid all the food where I can’t reach it."
            n 2bh "He always takes food away from me when I make him mad, [player]."
            n "There are entire days where I don’t eat, no matter how much I apologize."
            "I’m in shock."
            "I knew that Natsuki’s father was strict, but that much?"
            "It explains her small figure, it explains her harsh persona, even her confidence issues, that she hides under a self-centered act..."
            mc "Natsuki...I..."
            "I have no idea what to do, other than walk over to her and hug her."
            "She returns the hug, buries her head into my shoulder, and begins to cry."
            "We stand like this for some time."
            pause 2.0
            mc "Natsuki."
            n 2bu "Y-yes, [player]?"
            "She speaks through tears and sniffs."
            mc "Listen...how many meals would you say you skip, a week?"
            n 2bs "S-seven."
            n "M-m-maybe more."
            n "At least o-o-o-ne a day."
            mc "Well, that’ll change."
            mc "Starting tomorrow, I’m bringing you in food, alright?"
            n "[player]..."
            n 2bq "You’ll r-really do that for me?"
            mc "Of course, Natsuki."
            mc "You’re my girlfriend, and beyond that, I would do it for you anyway, because I care about you."
            "I expected that to cheer her up, but instead she seems to cry even harder."
            n 42bf "Damn it, [player]."
            n "You’re so nice to me, and I’ve been nothing but mean to you all this time."
            n "I have to be the worst girlfriend ever."
            "I put a hand on her head."
            mc "Natsuki, I'm not stupid."
            mc "I know how to back off from something I don't like."
            mc "So, you can only guess my answer to that by looking where I am now, and what I am to you."
            "She giggles."
            n 1ba "You’re a masochist, aren’t you, [player]? I guess it explains a lot."
            "The happiness in her voice begins to return."
            "Hey, at least she got humor out of something."
            "I pat her on the back before releasing her."
            mc "Hey, neither of us have eaten, have we?"
            mc "Come on, let me make you something."
            mc "You don’t have to be a master chef to know eggs, after all."
            "She agrees, but seems sad that I let go of her."
            "I go to cook the eggs, and she follows me." 
            n 4bw "I can cook my own food, you know!"
            "I don’t object, and we get to cooking."
            "I somehow manage to burn mine, but Natsuki’s turn out fine."
            "We both sit down to eat, and finish rather quickly."
            "Before either of us get up, I stop her."
            mc "Natsuki."
            mc "Listen, right now, tell me EVERYTHING about your life at home."
            mc "I need to know these kind of things."
            n 1bm "W-well... alright."
            "And she does, in fact, tell me everything."
            "It takes quite a while to get out, and I do interject to ask a question once in a while."
            "But for the most part it’s Natsuki talking about how terrible things are with her dad, and how her mom isn’t in the picture to stop it."
            "She talks about how he neglects her, or won’t let her do 'anything a girl wouldn’t do'."
            "He gets angry when she takes more than a minute to answer a text of his, and she better not fail to answer a call."
            "And the reason as to why she's in my class?"
            "She had to study so hard that the school allowed her to skip an entire year."
            "But when she didn't skip another one right at the next year, her father got mad at her again."
            "I’m completely shocked by everything."
            mc "Natsuki, you need to get out of there."
            n "Yea?"
            n 2bc "I’m not an adult."
            n 2bb "I don’t have a job."
            n "I don’t have any money, and I have no idea how to sustain a house."
            n "I'm not even old enough for any of that!"
            n 2bh "I’m trapped, [player]."
            mc "You know, Natsuki, there is someone who can do all that stuff."
            mc "Might I also mention you come over to this person’s house every Sunday anyway?"
            n 1bu "[player]...Are you asking me to move in with you?"
            mc "Well, if we’re serious about dating, then it was bound to happen anyway."
            mc "You need to leave ASAP, and if I can provide, why wouldn’t I?"
            n "...But I can’t tell my dad I’m moving in with some boy, he’ll freak out."
            mc "Hmm...We’ll cross that bridge when we get there."
            mc "For now, think about it, alright?"
            mc "Tell me what your plan is."
            n 1bv "I’ll think about it, but there’s no promises, and-! {i}*mumble mumble*{/i}"
            mc "...What?"
            n 1br "N-Nothing! I was just saying I’ll think about it, nothing else!"
            mc "Oh, alright."
            mc "Well, the sun’s setting."
            mc "Listen, be safe, alright?"
            n "There’s nothing dangerous on the walk back."
            "I hug her once more."
            mc "I wasn’t talking about that, though."
            "Her eyes lit up as if the meaning clicked in her head, and she looked at me one last time."
            n 2bn "Thank you, [player]."
            n "The answer is yes, I will."
            n 1bm "It won’t be instant, but soon, alright?"
            n "M-maybe in a couple weeks."
            "That’s the most genuine I think Natsuki’s ever been."
            "I smile, kiss her on the head, and let go."
            "She walks out the door."
        "Drop it.":
            mc "Alright, whatever you say."
            "Natsuki comes in, and sits in the table."
            "She watches me cook some breakfast, as she tries to open her mouth constantly."
            "But her voice never came out."
            "Once I finish, I sit down and eat breakfast."
            "The sound of something vibrating stopped me on my tracks."
            "Natsuki takes her phone out, as her expression turns into a scared one for a fraction."
            n 2bu "Urgent text from my dad."
            n "He’s, uh, sick, so I need to go help him."
            mc "Oh, sorry."
            mc "By the way, I did notice that you might want something to eat, so here."
            "I stuff a toast with some ham on it to her hands."
            "She takes it, and faster than I could ever imagine, she dumps it in."
            n "T-Thanks for that, but now I really must leave."
            n 2bm "Bye!"
            "She rushes out the door, and with that, things are done."
            "That’s probably a record for her shortest visit, but if it’s important, it’s important."
            "Best to just let her be."
            "She can count on me after all."
            "I mean, I guess she does know."
            "She does, right?"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "It’s just like any other Sunday, me waiting patiently for Natsuki to show up."
    "We’ve done this quite a few times now, and it’s starting to set in as commonplace."
    "It’s still exciting each time, and it’s kind of become a factor of motivation for the rest of the week, but it’s a different kind of excitement now."
    "As I ponder this, Natsuki knocks on my door."
    show natsuki 1ba at t11 zorder 2
    n 1ba "Hi, [player]!"
    "She’s in casual clothing as usual, and this time holding the next Parfait Girls under her arm."
    "She immediately takes one look at me and frowns."
    n 2be "Did you even comb your hair when you woke up this morning?"
    mc "Ah, no, I didn’t."
    mc "Sorry, must have forgotten."
    n "Well it looks awful!"
    n 2bg "Here-"
    "Natsuki stands on her tiptoes and tries to adjust my hair."
    show natsuki 2bh at t11
    "She tries to comb it with my hand, but it just won’t go down."
    "Finally, she licks her hand and combs it once more, successfully getting it down."
    show natsuki 2bi at t11
    "It’s only after her task is finished that she realizes what she’s done and blushes."
    n 2bk "There!"
    n "T-That should fix your hair!"
    n 1bq "Now, next time, comb your hair yourself."
    mc "Alright, alright."
    mc "Would you like to come inside?"
    "She nods and follows me in."
    scene bg kitchen
    with wipeleft_scene
    "When we walk by the kitchen, she pipes up."
    n 1bt "Hey, [player]."
    n "Should I make some cookies for the two of us?"
    mc "Good idea."
    mc "You want some help?"
    n "Nah, I can handle this myself."
    n 1bd "I’m making half a dozen, that’s all, it’s not like the cupcakes!"
    mc "Well, alright. I’ll get today’s activity set up."
    "I start to walk away when I hear Natsuki pipe up."
    n 2bm "Aren’t we going to read today?" 
    "She asks, pointing to her manga."
    mc "Well, manga is an interest of yours that you showed me, right? Well, there’s an interest of mine I want to show you." 
    mc "Remember how I said I wanted to play some video games with you, a while ago?"
    "A look of realization slowly hits her."
    n 2bx "Now, [player]? Couldn’t it have been a day where I didn’t have my Manga to read?"
    mc "Trust me, it’ll be fun. I’ll be right back, alright?"
    "She looks concerned, but otherwise goes back to her cookies."
    scene bg bedroom
    show natsuki 2bc at t11 zorder 2
    "I go upstairs and grab the wires, console, controller, and a couple of games."
    "I don’t know which one I should show Natsuki, though."
    "If I pick correctly, it might make her more interested in the hobby..."
    "I go downstairs and see her still hard at work on our deserts."
    "I hook up the wires to the television and grab the games."
    "Right as I do this, she puts the cookies in the oven and joins me in the living room."
    n 2bc "So, what game are we playing, then?"
    mc "Hmm..."
    "I ponder this for a moment."
    "Getting this right will be crucial."
    "All the genres will be really fun, but I know that one of them is the one that Natsuki wants to play the most."
    menu:
        "But which?"
        "An Action game.":
            $ NatsukiVar += 1
            mc "Here, let’s play this."
            "I grab the latest release of my favourite shooting game."
            "A game of ultra-violence and non-stop action is definitely what Natsuki’s been missing out on."
            "I pop the disk in and she grabs the cookies and sets them on the coffee table."
            "I dim the lights, and we both sit on the couch."
            "After a few minutes of playing through the game I look to Natsuki, holding one of the cookies in her hand." 
            "She’s absolutely mesmerized."
            mc "You seem to be enjoying this."
            n 1bd "It’s awesome, [player]!"
            n "I’m so glad you showed me this."
            n 3bj "I guess now I understand why guys like you stay in your room so much..."
            "I can’t tell if that’s meant to be a compliment or an insult, but I take it as the former."
            "As I continue, I notice her reacting to the game as if it was one of her manga."
            "Scared when my health is low, happy when I beat a level, annoyed by the antagonist."
            "It’s only once I finally die that she makes a suggestion."
            n 3bk "Can I try?"
            "I’m taken slightly aback, as I didn’t think Natsuki would get that into it, but I nod and hand her my controller."
            "Grabbing one of the cookies for myself."
            "For a first timer, she does alright."
            "She doesn’t get nearly as far as I do, and her aim is absolutely awful, but she’s still making it through."
            "We start to turn this into a routine."
            "Every time each of us dies, the other takes a turn."
            "This system works great until Nat gets a bit closer to me, within arm’s reach."
            "That’s when I made the mistake of putting an arm around her, positioning myself so I can still hold the controller."
            "That’s when she immediately starts pressing buttons to mess me up, and she succeeds."
            n 3by "I guess that means it’s my turn!" 
            "She says, a certain pride in her voice for her cleverness."
            "However, shortly after she takes control, I return her gesture by putting my hand over her eyes."
            n 2bc "Hey! Stop that!"
            "She says between giggles."
            "I watch as the character dies and take the controller back from her."
            mc "Guess that means it’s my turn, huh?"
            "I say, taking the controller for myself."
            "She then gets the bright idea of grabbing hold of my thumbs, so I can’t use the sticks."
            "She’s surprisingly strong, and at this point I die, yet don’t hand her the controller."
            n 2be "Hey! It’s my turn!"
            mc "You’ll get this back when you play fair." 
            "I hold the controller out of her reach."
            n "Well if you won’t give it to me, I’ll get it myself!"
            "With that, she drops the cookie she’s holding and practically gets on top of me to try and grab the remote."
            "To stop her, I lock my arm around her midsection."
            n 2bo "Not fair!"
            n "Let go of me!"
            "She tries, weakly, to push herself out of my grip."
            "When she stops struggling, I bring the controller back down and get back in the game."
            "My grip on her loosens, but instead of getting away she instead turns to see the tv."
            "She’s now sitting on my lap, watching me play. I don’t mind, though."
            "Her head barely goes up to my nose, so she’s not blocking my vision any."
            "When we both settle in, and I say my prayers that my blood flow doesn’t betray me in a particular way."
            "After a few minutes, she finally speaks up."
            stop music fadeout 1.0
            play music t9
            n 2bq "[player]. I hate this."
            "She gets off my lap."
            mc "Did I do something wrong?"
            n 1br "No, dummy, it’s just..."
            mc "What’s up?"
            n 1br "Nothing, it’s fine!"
            n "Just continue!"
            mc "Nope. What is wrong?"
            "She hesitates."
            "Then, she speaks up."
            n 1bs "I...I hate how good this feels."
            n "I don’t deserve to feel like this, especially with you."
            n 2bs "I’ve been nothing but mean to you since we’ve met."
            n "I’m sorry."
            mc "Don’t be, Natsuki."
            mc "I know you don’t really mean any of it."
            mc "If you did, why would you date me?"
            mc "That seems like a bad idea, doesn’t it?"
            "She looks down, ashamed with herself."
            show natsuki 1bu at t11 zorder 2
            n "Yea, but that’s not an excuse."
            n "When I first came in here, I completely dismissed this, didn’t even consider it a good idea."
            n 12bd "I’m lucky you even showed it to me."
            mc "Listen."
            "I bring her up to me, so that we’re looking each other in the eyes."
            show natsuki 2bn at t11
            "I wipe her eyes, and she looks at me."
            mc "This has really been one of the best days of my life, Natsuki."
            mc "I don’t know what else to say other than thank you."
            mc "For being here, for being you."
            mc "Thanks."
            "We’re face to face now, and I’m holding her with both hands."
            "Naturally, she closes the gap between us."
            "I’m shocked at her forwardness at first, but I eventually return the kiss."
            "We’ve both never done this, but somehow it feels perfect."
            "Our lips eventually part, and she looks at me with those beautiful eyes of hers."
            "Those pink eyes I fell in love with all that time ago."
            "It seems like an eternity before she speaks."
            n 1bs "[player], I hate you."
            n 1bq "I hate how you make me feel like this."
            n 1bj "I never want it to end."
            mc "Neither do I."
            "She returns to her spot on my lap, and I put my arms back around her."
            "For the next hour or so, we stay like this."
            "My performance drops, and she’s quick to point this out, but not in her normal mocking tone; instead, almost sad to see me fail."
            "Finally, it begins to get dark out, and she gets ready to leave."
            n 1bk "[player]...Thank you so much."
            n "For having me over, for being my boyfriend, for everything."
            n "It really is some of the best time of my life."
            mc "Natsuki, I feel the exact same way."
            mc "It’s been nothing but happiness every weekend ever since you admitted your feelings." 
            mc "Thank you, by the way."
            mc "If you hadn’t done that, none of this would be happening."
            n 2bj "Well you’re welcome."
            n 2bl "I’ll see you tomorrow at school, alright?"
            "She gives me one last hug and walks out."
        "A Player VS Player game.":
            "I grab {i}Rumble III{/i}'s box and pop the disk in the tray."
            show natsuki 1ba at t11
            "Natsuki grabs the cookies from the kitchen and sets them on the coffee table."
            "I dim the lights, and we both sit on the couch."
            "While she does pay attention, she doesn’t seem to enjoy it."
            show natsuki 2bi at t11
            n 2bb "I still think we should have read, instead."
            mc "Aww, come on! I’m enjoying this!"
            n 2bg "Alright, fine. But I’m going to read, okay?"
            "With that, she comes a bit closer to me, leaning against me." 
            "She takes out Parfait Girls and her phone light, starting to read." 
            "We go back to our own activities, once in a while grabbing cookies from the plate, until eventually things start to get dark out."
            n 1bc "Bye, [player]."
            n "No offense, but let’s do something different next week, alright?"
            mc "Fine by me. I’ll see you Monday."
            show natsuki at thide zorder 1
            hide natsuki
            "She leaves."
        "A Co-Op game.":
            "I grab {i}Wormhole 2{/i}'s box and pop the disk in the tray."
            show natsuki 1ba at t11
            "Natsuki grabs the cookies from the kitchen and sets them on the coffee table."
            "I dim the lights, and we both sit on the couch."
            "While she does pay attention, she doesn’t seem to enjoy it."
            show natsuki 2bi at t11
            n 2bb "I still think we should have read, instead."
            mc "Aww, come on! I’m enjoying this!"
            n 2bg "Alright, fine. But I’m going to read, okay?"
            "With that, she comes a bit closer to me, leaning against me." 
            "She takes out Parfait Girls and her phone light, starting to read." 
            "We go back to our own activities, once in a while grabbing cookies from the plate, until eventually things start to get dark out."
            n 1bc "Bye, [player]."
            n "No offense, but let’s do something different next week, alright?"
            mc "Fine by me. I’ll see you Monday."
            show natsuki at thide zorder 1
            hide natsuki
            "She leaves."            
        "A Story-based game.":
            "I grab {i}Gone Nuclear: Vegas Blues{/i}' box and pop the disk in the tray."
            show natsuki 1ba at t11
            "Natsuki grabs the cookies from the kitchen and sets them on the coffee table."
            "I dim the lights, and we both sit on the couch."
            "While she does pay attention, she doesn’t seem to enjoy it."
            show natsuki 2bi at t11
            n 2bb "I still think we should have read, instead."
            mc "Aww, come on! I’m enjoying this!"
            n 2bg "Alright, fine. But I’m going to read, okay?"
            "With that, she comes a bit closer to me, leaning against me." 
            "She takes out Parfait Girls and her phone light, starting to read." 
            "We go back to our own activities, once in a while grabbing cookies from the plate, until eventually things start to get dark out."
            n 1bc "Bye, [player]."
            n "No offense, but let’s do something different next week, alright?"
            mc "Fine by me. I’ll see you Monday."
            show natsuki at thide zorder 1
            hide natsuki
            "She leaves."            
            
    "As she walks out, I consider the events of this night. Is this what love is like?"
    scene black
    with dissolve_scene_full
    stop music fadeout 1.0
    
    scene bg kitchen
    play music t3
    "It’s Sunday, and for some reason I feel particularly off."
    "I’m excited for Natsuki’s visit, but I feel ill; it’s only when I start sneezing that I figure out why."
    "I’ve developed a cold. Great." 
    "I’m just about to prep some coffee when Natsuki knocks on the door, so of course I go to greet her."
    show natsuki 3ba at t11 zorder 2
    "However, I immediately relay the bad news."
    mc "Natsuki, I wouldn’t stay here. In case I don’t give the appearance, I’m sick today. Sorry."
    n 1be "Nice work, [player]. Guess who has to take care of you now?"
    mc "I can take care of myself!"
    n "Yeah, sure you can. You got yourself sick, idiot, but you probably won’t make yourself better. Come on, let’s go."
    "I think about this for a moment."
    "On the one hand, I did warn her, and she is insisting."
    "But on the other, it’s still mean of me to willingly go along with this."
    "She doesn’t need to be sick like this!"
    menu:
        "I guess I might as well—"
        "Let Natsuki in.":
            $ NatsukiVar += 1
            mc "Alright, fine."
            mc "But if you get sick, don’t blame me."
            n 2bh "I won’t."
            n "Now go lay down somewhere."
            n 2bk "Hurry up."
            scene bg bedroom
            show natsuki 1bi at t11 zorder 2
            "I naturally go to the only comfortable bed, the one in my bedroom, and lay in it."
            "Natsuki practically throws my cover at me."
            n 1bh "Here. Now, I’m going to get you something warm, so you can feel better."
            n "Stay here."
            show natsuki at thide zorder 1
            hide natsuki
            "Before I can mention that I can’t really go anywhere, she leaves."
            "A few minutes later, she arrives back with some hot soup."
            mc "Soup?"
            n 1be "It helps with colds!" 
            n 1bc "And it’s better than anything else I could’ve given you."
            n 1bb "Are you going to be mad at me for it or are you going to appreciate it?"
            mc "I appreciate it, Natsuki."
            mc "It’s really nice that you’re doing this."
            mc "Thank you."
            "She seems almost shocked by my words."
            n 3bw "Hmph, whatever."
            n "You’re my boyfriend now, so I need to take care of you!"
            n 3bq "You’d do the same, right?"
            mc "I suppose, yes, I would."
            n 3bx "What do you mean, you ‘suppose?’"
            mc "Ah, it’s just an expression!"
            mc "I don’t mean it like that."
            "She puts on an angry face, but once she pulls up a chair and sits next to me it slowly starts to fade."
            show natsuki 3bu at t11 zorder 2
            "After a few seconds, she grabs my hand, and I look at her in suspicion."
            n 2bw "I’m just trying to...keep your pulse in check."
            mc "That’s not how pulse works, that’d be my wrist."
            mc "Also, a cold wouldn’t really affect my pulse."
            n  "What, you don’t think I know that?"
            n "I’m not stupid, [player]!"
            "She doesn’t then mention why she’s REALLY holding my hand, but I do know, don't I?"
            "I decide to drop it anyways."
            "It won't do any good to let her know that I'm aware."
            "At any rate I..."
            mc "{i}Achoo!{/i}"
            "A sneeze then comes out of nowhere and ruins the moment."
            n 1be "Gross!"
            n "You need some tissues or something, where are they?"
            mc "Right there, over on my desk."
            "I pray to every god I can think of that she doesn’t put two and two together with the lotion right next to it."
            "And seeing the way her faces changes when she grabs it, I’m thinking none of them answered."
            "When she returns it to me, I blow my nose and throw the tissue in a nearby trash can."
            n 1by "So, why was this next to a bottle of lotion, [player]?"
            mc "Well... I... It’s really easy to explain..."
            "My stammering betrays my words. Natsuki laughs."
            n "You’re disgusting, [player]."
            "She laughs."
            "Before I have time to think of a retort, she grabs the remote for my TV."
            n 1bh "You wanna watch anything in particular?"
            mc "Nope."
            mc "You can pick if you like."
            "Hearing this, she flips over to an idol anime."
            "I’ve never seen it, but she seems to like it."
            "One of the characters does remind me of her, so I can see why."
            "I pay attention to her reaction when good and bad things happen to the cast, how she almost laughs at some of their misfortunes and charades."
            n 1bk "...[player]!"
            mc "Huh?"
            mc "Oh, what’s up?"
            n "You were kinda...staring at me."
            n 1bq "What is that for?"
            mc "I just...spaced out."
            mc "I’m sorry, I didn’t mean to make you uncomfortable."
            n "...Fine."
            "Afterwards, she turns back to the TV."
            "We sit like this for a bit until her hand meets mine and they interlock once more."
            n 3bs "[player]...I hope you know, I don’t mind if I get sick."
            n "It actually is fun spending time with you."
            mc "Yea, I like this, too."
            mc "But don’t get sick."
            mc "You’d make me feel really bad about it."
            n "Haha, I won’t then."
            "She returns to the show, as do I."
            "It’s only when the sun finally starts to set that she releases my hand, and something seems to be missing the second she does."
            n 4ba "Well, I’ve gotta go then."
            n "Bye, [player]."
            mc "Bye, Natsuki."
            mc "I hope I didn’t make you sick..."
            n 4bf "Stop worrying about me!"
            n "I can handle a little cold, anyway."
            n "See you tomorrow, alright?" 
            "And with that, she walks downstairs, and right before the door opens and closes behind her, I hear her sneeze."
            "Great."
        "Tell her to come back next week.":
            mc "Natsuki, I won’t let you get sick. Now, go. I’ll see you tomorrow, alright?"
            n 2bq "But--!"
            "The sound of something vibrating inside her pocket stopped her from continuing."
            "She excused herself, as she quickly threw a glance towards her mobile phone screen."
            "Natsuki froze."
            mc "Natsuki...?"
            n 1bu "Yea, sorry."
            n "Well, I'll go then."
            n 1bo "But you better take care of yourself!"
            mc "Don't worry, I know how to handle a cold."
            "I say that, trying to make Natsuki less worried about me."
            "But I'm sure she will worry about me, maybe even more now."
            "As she left, I used the rest of my strength to close the door and get to my bed."
            "Where I spent the rest of the day, asleep."
    scene black
    with dissolve_scene_full
    stop music fadeout 1.0
    
    scene bedroom
    with dissolve_scene_half
    play music t10
    "It’s Sunday, as usual."
    if NatsukiVar >= 3:
        "Natsuki shows up..." 
        "This time holding a box in her hand."
        n 12bc "He... he found out."
        n 12be "About us."
        n 12bd "Screamed at me, shoved an empty box in my face and told me to get out of his house."
        n "That I had 24 hours to leave or else he would..."
        n 12bb "I...I was really scared, [player]."
        n "I know this isn’t how we planned it, but I have no idea what else to do..."
        mc "Natsuki..."
        "At once, I go over to her and hug her tightly."
        show natsuki at thide zorder 1
        hide natsuki
        scene black
        "She almost drops the box in shock."
        mc "I..."
        mc "Shhh. It’ll be alright, Natsuki."
        mc "You’re safe now, alright?"
        mc "It isn’t what we planned, but that isn’t important."
        mc "All that’s important is that you’re alright."
        n "... I’m still scared."
        n "What if he gets mad and, comes for me, or something?"
        mc "Does he know where I..."
        mc "Where we live?"
        n "N-No..."
        mc "Then you’re fine."
        mc "I get that you’re paranoid, but I’ll protect you, alright?"
        mc "Even if I have to go down fighting, I won’t let anything hurt you."
        n "I..."
        "Tears begin to well up in Natsuki’s eyes."
        "I grab the box from her and set it down, and she buries her face in my chest, lightly sobbing."
        "Without really thinking, I wipe tears from her eyes."
        scene bg bedroom
        show natsuki 1bm at t11 zorder 2
        "She looks at me, for a straight half minute."
        "Her eyes are still slightly glistening from the tears."
        "I pick up her box, and start to go upstairs, motioning her to follow me."
        "She does, and I set her stuff on the bed."
        n 2bn "[player]...you only have one bed, huh?"
        mc "Oh yea..."
        mc "We’ll worry about that later."
        mc "For now, let’s find out where to put your stuff."
        "The majority of it, funnily enough, ended up being for baking."
        "What little of it wasn’t, was mostly items she kept around her room."
        "I noticed that she didn’t have much, and that was probably for a reason."
        "It’s mostly just kid’s dolls, a couple of anime posters, and Manga she hid from her father."
        "We put these in their proper place. "
        "At this point, Natsuki and I both sit on the bed."
        "I decide to ask her what we should do."
        n 1bw "What, you can’t think of something?"
        n 1bx "What are you bothering me for?"
        "It’s nice to see she’s returned to her normal state."
        mc "You sound like you can’t think of anything, either."
        n "I...I can, I just don’t want to!"
        n "You should do it instead!"
        mc "Fine, fine."
        mc "Here, you want to watch some anime?"
        mc "I’ll let you pick which one."
        n 1br "Yea, you better!"
        n "I w-wouldn’t let you pick, anyway."
        n 2bu "It’s not like I want to know what you want to watch, or something like that."
        n 2bx "Your taste is probably terrible!"
        "With that, Natsuki grabs the remote from me, and flips to a slice-of-life anime."
        "I notice a theme here."
        "I don’t refuse, instead changing my position to emulate me actually laying in bed, with my head propped up on my arm."
        "Natsuki lays down normally, yawning as she does."
        "We’re sitting together, and the show has just started."
        "While watching, I notice we both sort of 'slump' into the bed."
        "We begin to straight up lay next to each other, at this point."
        "We continue watching for a few minutes until she falls asleep."
        "At first, I don’t pay it much attention."
        "I’m perfectly fine here, as long as I explain to her what happened before she wakes up."
        "However, what I’m not expecting is for her to do is turn around and wrap her arms around me, settling into my side."
        "I panic."
        "What if she wakes up like this?"
        "What is she going to say?" 
        "What if this ruins everything?"
        "Slowly and carefully, I pick up her top arm and put it on her side."
        "I then try to push my other arm out from under her, slowly once more so that she doesn’t awaken."
        "She’s completely separate from me once more, and I breathe a sigh of relief."
        "That is, until she brings her arms right back into position, effortlessly."
        "God."
        "Damn."
        "It."
        "I take a different approach, attempting to remove myself from the situation."
        "I consider slithering out, from under her arms, when I hear her speak."
        n 1bw "You don’t have to move so much, idiot."
        n "You can just tell me you’re uncomfortable."
        mc "I...I’m not!"
        mc "I just...didn’t want to hear your reaction when you woke up."
        n 1bx "Well, I’m up."
        "She rubs the sleep out of her eyes, and yawns, stretching."
        n 1bs "I’m madder then I would have been, ya know."
        mc "Yea, you say that now, but if I had left you like that or even fell asleep myself, might be different."
        n 1bn "[player]..."
        "I turn to her."
        n 1bi "These Sundays with you are some of the best hours of my life."
        n "It’s so nice to have an escape from home, even when it was only temporarily, and you being with me makes things even better."
        n 1bc "I don’t normally like to be genuine like this, but if I had woken up like that...it would have been great."
        mc "Natsuki, these are some of the best moments of my life, too."
        mc "I never want these to end."
        mc "I would love to spend every Sunday ‘till the day I die with you."
        n 1ba "[player], I want to spend every {i}day{/i} ‘till the day I die with you."
        n 1bj "I want to spend the rest of my life with you."
        mc "Natsuki...I..."
        mc "God damnit, Natsuki."
        mc "I love you, alright?"
        mc "More than anyone on this entire earth, I love you."
        "She slowly begins weeping."
        n 1br "That’s..."
        n 12bf "Y-you’re the first person that’s ever said that to me."
        n "I love you too, [player]."
        "Natsuki being so candid makes me a bit shocked."
        "Without a word, I place my hand on the back of her head."
        show natsuki at thide zorder 1
        hide natsuki
        scene black
        "Once she realizes what’s going on, she wraps he arms around me as our lips meet, kissing for the first time since we first played video games together."
        "I’m completely taken out of my surroundings, and instead all I comprehend is myself, the couch, and the amazing girl I’m sharing this moment with."
        "The rest of our lives, huh?"
        "That doesn’t sound like a bad idea."
        scene bg bedroom
        show natsuki 1ba at t11 zorder 1
        stop music
        play music t6
        n 1ba "Idiot."
        mc "What?"
        n "I can tell."
        n 1bt "In your eyes."
        n "You still don’t believe me."
        mc "I- What?"
        "She ignores me."
        n 2by "Don’t worry."
        "As she rolls, and lays on top of me, she whispers in my ear."
        n "I can help fix that~"
        "{i}Gulp.{/i}"
        scene black
        with dissolve_scene_full
        stop music fadeout 2.0
    elif NatsukiVar >= 0:
        "Until five minutes ago, I was really happy that I got to see Natsuki today as well."
        "But she sent me a message where she told me that she can't come today."
        "What a shame, I guess I'll play some games today."
        "I'll see her tomorrow anyways." 
        scene black
        with dissolve_scene_full
        stop music fadeout 2.0
    else:
        hide natsuki
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

    
