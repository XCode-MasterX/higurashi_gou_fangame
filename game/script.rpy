﻿# The script of the game goes in this file.
init -10 python:
    def shrink(s):
        return Transform(s, zoom=.5)

    config.displayable_prefix["small"] = shrink

    def char(s):
        return Transform(s, zoom=.55)

    config.displayable_prefix["char"] = char
    dpunch = Move((0, 30), (0, -30), 0.35, bounce=True, repeat=True, delay=.5)




#declare non-char images here
image endofchapter = "images/ui/endofchapter.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.
#CHARACHTERS

define k = Character("Keichi", color="#8C6161")
define m = Character("Mion", color="#0D7343")
define re = Character("Rena", color="#F29C50")
define ri = Character("Rika", color="#2D4473")
define sa = Character("Satoko", color="#F2E96B")
define sh = Character("Shion", color="#49BF88")



#Images

#KEIICHI
image ke sch happy = char(Image("images/CharactersMei/Keichi/ke_sch1.png"))

#MION
image mi cas sigh close = char(Image("CharactersMei/Mion/mi_cas1.png"))
image mi cas grin close = char(Image("CharactersMei/Mion/mi_cas2.png"))
image mi cas oh close = char(Image("CharactersMei/Mion/mi_cas3.png"))
image mi cas blank close = char(Image("CharactersMei/Mion/mi_cas4.png"))
image mi cas open close = char(Image("CharactersMei/Mion/mi_cas5.png"))
image mi cas irate close = char(Image("CharactersMei/Mion/mi_cas6.png"))
image mi cas smile close = char(Image("CharactersMei/Mion/mi_cas7.png"))
image mi cas laugh close = char(Image("CharactersMei/Mion/mi_cas8.png"))
image mi cas blank = char(Image("CharactersMei/Mion/mi_cas9.png"))
image mi cas open = char(Image("CharactersMei/Mion/mi_cas10.png"))
image mi cas irate = char(Image("CharactersMei/Mion/mi_cas11.png"))
image mi cas smile = char(Image("CharactersMei/Mion/mi_cas12.png"))
image mi cas laugh = char(Image("CharactersMei/Mion/mi_cas13.png"))
image mi cas sigh = char(Image("CharactersMei/Mion/mi_cas14.png"))
image mi cas grin = char(Image("CharactersMei/Mion/mi_cas15.png"))
image mi cas oh = char(Image("CharactersMei/Mion/mi_cas16.png"))

image mi sch sigh close = char(Image("CharactersMei/Mion/mi_sch1.png"))
image mi sch grin close = char(Image("CharactersMei/Mion/mi_sch2.png"))
image mi sch oh close = char(Image("CharactersMei/Mion/mi_sch3.png"))
image mi sch blank close = char(Image("CharactersMei/Mion/mi_sch4.png"))
image mi sch open close = char(Image("CharactersMei/Mion/mi_sch5.png"))
image mi sch irate close = char(Image("CharactersMei/Mion/mi_sch6.png"))
image mi sch smile close = char(Image("CharactersMei/Mion/mi_sch7.png"))
image mi sch laugh close = char(Image("CharactersMei/Mion/mi_sch8.png"))
image mi sch blank = char(Image("CharactersMei/Mion/mi_sch9.png"))
image mi sch open = char(Image("CharactersMei/Mion/mi_sch10.png"))
image mi sch irate = char(Image("CharactersMei/Mion/mi_sch11.png"))
image mi sch smile = char(Image("CharactersMei/Mion/mi_sch12.png"))
image mi sch laugh = char(Image("CharactersMei/Mion/mi_sch13.png"))
image mi sch sigh = char(Image("CharactersMei/Mion/mi_sch14.png"))
image mi sch grin = char(Image("CharactersMei/Mion/mi_sch15.png"))
image mi sch oh = char(Image("CharactersMei/Mion/mi_sch16.png"))


#RENA
image re cas sigh close = char(Image("CharactersMei/Rena/re_cas9.png"))
image re cas grin close = char(Image("CharactersMei/Rena/re_cas10.png"))
image re cas oh close = char(Image("CharactersMei/Rena/re_cas11.png"))
image re cas blank close = char(Image("CharactersMei/Rena/re_cas12.png"))
image re cas open close = char(Image("CharactersMei/Rena/re_cas13.png"))
image re cas irate close = char(Image("CharactersMei/Rena/re_cas14.png"))
image re cas smile close = char(Image("CharactersMei/Rena/re_cas15.png"))
image re cas smile  = char(Image("CharactersMei/Rena/re_cas16.png"))
image re cas laugh  = char(Image("CharactersMei/Rena/re_cas17.png"))
image re cas sigh  = char(Image("CharactersMei/Rena/re_cas18.png"))
image re cas grin  = char(Image("CharactersMei/Rena/re_cas19.png"))
image re cas oh  = char(Image("CharactersMei/Rena/re_cas20.png"))
image re cas blank  = char(Image("CharactersMei/Rena/re_cas21.png"))
image re cas open  = char(Image("CharactersMei/Rena/re_cas22.png"))
image re cas irate  = char(Image("CharactersMei/Rena/re_cas23.png"))

image re sch sigh close = char(Image("CharactersMei/Rena/re_sch9.png"))
image re sch grin close = char(Image("CharactersMei/Rena/re_sch10.png"))
image re sch oh close = char(Image("CharactersMei/Rena/re_sch11.png"))
image re sch blank close = char(Image("CharactersMei/Rena/re_sch12.png"))
image re sch open close = char(Image("CharactersMei/Rena/re_sch13.png"))
image re sch irate close = char(Image("CharactersMei/Rena/re_sch14.png"))
image re sch smile close = char(Image("CharactersMei/Rena/re_sch15.png"))
image re sch smile  = char(Image("CharactersMei/Rena/re_sch16.png"))
image re sch laugh  = char(Image("CharactersMei/Rena/re_sch17.png"))
image re sch sigh  = char(Image("CharactersMei/Rena/re_sch18.png"))
image re sch grin  = char(Image("CharactersMei/Rena/re_sch19.png"))
image re sch oh  = char(Image("CharactersMei/Rena/re_sch20.png"))
image re sch blank  = char(Image("CharactersMei/Rena/re_sch22.png"))
image re sch open  = char(Image("CharactersMei/Rena/re_sch23.png"))
image re sch irate  = char(Image("CharactersMei/Rena/re_sch21.png"))

#RIKA
image ri cas sigh close = char(Image("CharactersMei/Rika/ri_cas1.png"))
image ri cas grin close = char(Image("CharactersMei/Rika/ri_cas2.png"))
image ri cas oh close = char(Image("CharactersMei/Rika/ri_cas3.png"))
image ri cas blank close = char(Image("CharactersMei/Rika/ri_cas4.png"))
image ri cas open close = char(Image("CharactersMei/Rika/ri_cas5.png"))
image ri cas irate close = char(Image("CharactersMei/Rika/ri_cas6.png"))
image ri cas smile close = char(Image("CharactersMei/Rika/ri_cas7.png"))
image ri cas smile  = char(Image("CharactersMei/Rika/ri_cas8.png"))
image ri cas laugh close  = char(Image("CharactersMei/Rika/ri_cas9.png"))
image ri cas sigh  = char(Image("CharactersMei/Rika/ri_cas10.png"))
image ri cas grin  = char(Image("CharactersMei/Rika/ri_cas11.png"))
image ri cas oh  = char(Image("CharactersMei/Rika/ri_cas12.png"))
image ri cas blank  = char(Image("CharactersMei/Rika/ri_cas13.png"))
image ri cas open  = char(Image("CharactersMei/Rika/ri_cas14.png"))
image ri cas irate  = char(Image("CharactersMei/Rika/ri_cas15.png"))

image ri sch sigh close = char(Image("CharactersMei/Rika/ri_sch1.png"))
image ri sch grin close = char(Image("CharactersMei/Rika/ri_sch2.png"))
image ri sch oh close = char(Image("CharactersMei/Rika/ri_sch3.png"))
image ri sch blank close = char(Image("CharactersMei/Rika/ri_sch4.png"))
image ri sch open close = char(Image("CharactersMei/Rika/ri_sch5.png"))
image ri sch irate close = char(Image("CharactersMei/Rika/ri_sch6.png"))
image ri sch smile close = char(Image("CharactersMei/Rika/ri_sch7.png"))
image ri sch smile  = char(Image("CharactersMei/Rika/ri_sch8.png"))
image ri sch laugh close  = char(Image("CharactersMei/Rika/ri_sch9.png"))
image ri sch sigh  = char(Image("CharactersMei/Rika/ri_sch10.png"))
image ri sch grin  = char(Image("CharactersMei/Rika/ri_sch11.png"))
image ri sch oh  = char(Image("CharactersMei/Rika/ri_sch12.png"))
image ri sch blank  = char(Image("CharactersMei/Rika/ri_sch13.png"))
image ri sch open  = char(Image("CharactersMei/Rika/ri_sch14.png"))
image ri sch irate  = char(Image("CharactersMei/Rika/ri_sch15.png"))

#SATOKO
image sa cas sigh close = char(Image("CharactersMei/Satoko/sa_cas9.png"))
image sa cas grin close = char(Image("CharactersMei/Satoko/sa_cas10.png"))
image sa cas oh close = char(Image("CharactersMei/Satoko/sa_cas11.png"))
image sa cas blank close = char(Image("CharactersMei/Satoko/sa_cas12.png"))
image sa cas open close = char(Image("CharactersMei/Satoko/sa_cas13.png"))
image sa cas irate close = char(Image("CharactersMei/Satoko/sa_cas14.png"))
image sa cas smile close = char(Image("CharactersMei/Satoko/sa_cas15.png"))
image sa cas smile  = char(Image("CharactersMei/Satoko/sa_cas16.png"))
image sa cas sigh  = char(Image("CharactersMei/Satoko/sa_cas18.png"))
image sa cas grin  = char(Image("CharactersMei/Satoko/sa_cas19.png"))
image sa cas oh  = char(Image("CharactersMei/Satoko/sa_cas20.png"))
image sa cas blank  = char(Image("CharactersMei/Satoko/sa_cas21.png"))
image sa cas open  = char(Image("CharactersMei/Satoko/sa_cas22.png"))
image sa cas irate  = char(Image("CharactersMei/Satoko/sa_cas17.png"))
image sa cas sneak  = char(Image("CharactersMei/Satoko/sa_cas2.png"))



image sa sch sigh close = char(Image("CharactersMei/Satoko/sa_sch9.png"))
image sa sch grin close = char(Image("CharactersMei/Satoko/sa_sch10.png"))
image sa sch oh close = char(Image("CharactersMei/Satoko/sa_sch11.png"))
image sa sch blank close = char(Image("CharactersMei/Satoko/sa_sch12.png"))
image sa sch open close = char(Image("CharactersMei/Satoko/sa_sch13.png"))
image sa sch irate close = char(Image("CharactersMei/Satoko/sa_sch14.png"))
image sa sch smile close = char(Image("CharactersMei/Satoko/sa_sch15.png"))
image sa sch smile  = char(Image("CharactersMei/Satoko/sa_sch16.png"))
image sa sch sneak  = char(Image("CharactersMei/Satoko/sa_sch17.png"))
image sa sch sigh  = char(Image("CharactersMei/Satoko/sa_sch18.png"))
image sa sch grin  = char(Image("CharactersMei/Satoko/sa_sch19.png"))
image sa sch oh  = char(Image("CharactersMei/Satoko/sa_sch20.png"))
image sa sch blank  = char(Image("CharactersMei/Satoko/sa_sch21.png"))
image sa sch open  = char(Image("CharactersMei/Satoko/sa_sch22.png"))
image sa sch irate  = char(Image("CharactersMei/Satoko/sa_sch23.png"))




# The game starts here.
label start:
    #testing
    
    label onidamashi:
        label oni1:
            stop music fadeout 1.0
            scene ch_op with intro_trans
            show onidamashi with dissolve 
            pause 7.0
            play sound cowbell
            show onidamashi-bern with slowdissolve
            play sound cowbell
            pause 10
            
            
            play music higurashi fadein 1.0 volume 0.66
            scene kei_room_black_blood with slowdissolve
            scene blood1
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch
            pause 1.0
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch
            pause 1.0 
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch
            pause 1.0
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch
            pause 2.0 

            "Where...?"
            "Where did those happy times 
            go?"

            pause 2.0
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch

            pause 1.0 
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch

            pause 2.0
            "How did it come to this...?"
            "Why did it come to this...?!"
            pause 1.0 
            

            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch
        
            pause 1.0 
            play sound kswing
            play sound down
            "{i}*thwack*{/i}" with vpunch

            "I wish...that I could go 
            back and change things..."

            "I wish that I could go back to 
            before it all went wrong..."

            pause 2.0

            "Forgive me."

            scene kei_room_black_blood with slowdissolve
            pause 3.0
            "The higurashi continued to sing their song."

            pause 3.0
            stop music fadeout 2.0
            scene black with slowdissolve
            stop sound fadeout 1.0
            pause 3.0
            
            voice kei_mom_k
            "Mom" "Keiichi! Wake up!"

            scene kei_room_dark with slowdissolve

            pause 1.0 
            voice kei_yawn
            "I stirred from my slumber, yawning as I rubbed my eyes."
            "Slowly, the nightmare I had just awoken from faded from my mind."
            pause 1.0
            play sound tummy
            "{i}*grumble*{/i}"

            "I guess I should go down and eat breakfast. Rena-chan will be here soon to pick me up."

            play music daily_life_boppy fadein 1.0

            scene mae_dining_morn with dissolve

            pause 1.0

            "My mom laid breakfast out on the table. Seaweed, pickled vegetables, raw egg, and grilled salmon."
            "The platonic ideal of a Japanese breakfast. But my mother was not finished." 
            "To her, no breakfast would be complete without a steaming bowl of miso soup."
            "She walked over with the soup, eyes shining, all while humming a little tune."
            "She must be in a good mood today."

            pause 1.0

            "Mom" "You haven't skipped breakfast once since we moved to Hinamizawa. I'm so proud of you."
            scene black with dissolve
            "Let me explain."
            show ke sch happy with dissolve
            "My name is Maebara Keiichi."
            "It has been three weeks since my family moved to the small village of Hinamizawa, and, honestly, I can't believe it belongs to the same country as the city I used to live in."
            "In fact, I have a hard time believing that it belongs to the same time period..."

            scene mae_dining_morn with dissolve

            voice kei_oh
            k "Yeah~ Your cooking is just that delicious!"

            "Back when we lived in the city, I was never a morning person. My parents were lucky if they saw me before I left for school."
            "Boycotting breakfast was my way of fighting back against my parents, who forced me to go to cram school."
            "Taking another bite of the grilled salmon, I sighed with satisfaction."
            "If I could go back in time, I would slap myself for ignoring all the hard work my mom put into those breakfasts."
            "Anyways, waking up early now was no issue, now that I no longer attended cram school."
            "I guess the country air helps too."

            "Mom" "Keiichi! Isn't it almost time for you to meet up with Rena-chan? Hurry, hurry!"

            "Mom seemed to enjoy the fact that I was walking to school with a girl."
            "That girl is named Ryuugu Rena. She is one of my classmates."
            "Every day since moving to Hinamizawa, Rena has shown up in the morning to walk me to school."
            "She and mom hit it off too. Rena would come over every so often with home-grown vegetables, and my mom was always appreciative of her kindness."

            "Mom" "Keiichi! Rena-chan is waiting!"

            "I shoveled the remainder of my breakfast down my throat and hopped up from the table."
            "After giving thanks to my mother, I ran out the door to meet up with Rena. As I left, my mom yelled out the door."

            scene mae_door_day with dissolve

            "Mom" "Have a safe trip! Don't forget to thank Rena-chan for the vegetables!"

            voice kei_giggle
            k "Haha, will do!"

            scene kei_house_sch with dissolve

            show re sch laugh with dissolve
            voice rena_ohayo
            re "Keiichi-kun! Good morning!"

            voice kei_yorena
            k "Why are you always here so early? You know you can sleep in every so often."

            show re sch open with dissolve
            voice rena_unn
            re "But if I slept in, I would keep you waiting."

            voice kei_chee
            k "I wouldn't wait for you."

            show re sch sigh with dissolve
            voice re_mate
            re "W-wha...? Keiichi-kun is so mean!"

            voice kei_jajaja    
            k "I'd leave you in the dust and kick you to the curb."


            voice rena_squeal
            re "Keiichi-kun! But I always wait for you..."

            voice kei_nah
            k "Don't care. I'd ditch you in a heartbeat if you were late."

            show re sch sigh close
            voice rena_cryout
            re "Why are you being so cold to me, Keiichi-kun? Why?"

            "I acted as if I was bothered by Rena, but in truth every morning I was excited to walk to school with her."
            "That being said, someone this fun to tease is a rare occurance. I have to take advantage of it when I can."

            voice kei_giggle
            k "Just kidding. I would never ditch you."

            show re sch sigh with dissolve
            voice re_hh
            re "Th-thanks."

            voice kei_re2
            k "Yep. I would definitely wait for you. No matter how long it took, I would wait for you forever, Rena-chan."

            show re sch open
            voice rena_hau
            re "F...f...forever...? Hauuuuu~"

            "Blushing profusely, Rena was at a loss for words. Fortunately for her, the awkward silence was soon shattered as we arrived at our next stop."

            scene hi2_day with dissolve
            
            show re sch smile at halfright with dissolve
            pause 2.0
            show mi sch smile with dissolve

            voice mion_ohayo
            m "There you all are! You guys sure took your sweet time getting to me! Any longer and I would have left without you!"
            "Rena and I made eye contact, wondering, if perhaps, Mion had psychically been listening in on our previous conversation."
            

            voice kei_mi2
            k "You're the one who is usually late Mion..."

            pause 1.0

            "This perky girl is Sonozaki Mion. She's my senior and pretty much the leader of our class."

            show re sch laugh at halfright with dissolve
            voice rena_ohayo
            re "Good morning Mii-chan!"

            show mi sch laugh with dissolve
            voice mion_ohayo
            m "Good morning Rena~!"

            show mi sch grin with dissolve
            voice mion_yahokei
            m "Long time no see, Kei-chan! How many years has it been?"

            voice kei_hua
            k "I was gone for two days, jeez! Besides, shouldn't I be asking that question to you, old man!?"

            "Mion leaned in to get a good look at me."
            
            
            show mi sch grin:
                ease .5 zoom 3.0 yoffset 1000 #moves right 100px, bottom 50px. set to 0 when you return later.
                
            
            voice mion_mn
            m "You seem to be the same Kei-chan as when you left a few days ago..."
            pause 0.75
            show mi sch open:
                ease .25 zoom 1 yoffset 0
            
            voice mion_ahque
            m "Hm? What's this?"
            pause 1.0

            show mi sch laugh close with dissolve
            voice mion_laughcute
            m "Kei-chan, I see that your buddy is quite perky this morning."
            voice kei_giggle 
            k "Yes, yes.{fast} He's always getting perky in the morning. It's actually a real pain. Wanna try saying hi to him?"

            show re sch open at halfright with dissolve                          
            voice rena_haaaaaaahhhhhh
            re "Waa... What are you talking about? Mii-chan, Keiichi-kun?!"

            "As usual, Rena couldn't keep up with our early morning, crude banter. I can't blame her though. Most people would also be confused by Mion's morning antics."

            show mi sch grin with dissolve
            voice mion_do
            m "So! How was your trip, Kei-chan? Did you find that thing I asked you about?"
            show mi sch laugh with dissolve
            voice mion_laughcute
            m "You know, that Western game catalog I wanted?"

            voice kei_ano
            k "I went back to Tokyo for a funeral, so I was busy the whole time. I didn't really have time to look around for toy shops."

            show mi sch smile with dissolve
            voice mion_kyukyukyu
            m "Tsk tsk tsk... Toy shops are nothing like hobby shops. Western stuff in general is impossible to find in these parts, ya know..."


            scene school_d with dissolve
            "Laughing as we walked we soon arrived at school."
            "The students of Hinamizawa, all 30 of them, learn in a single classroom. It seems kind of strange at first, though I guess I got used to it pretty quickly."

            scene school_hall with dissolve
            "Mion reached out to open the classroom door but hesited for a moment."
            show mi sch smile with dissolve
            voice mion_laughcute
            m "Well, well... hehehe... After you, Kei-chan..."

            voice kei_ungh
            k "Are you trying to test my skills? I won't be defeated this time! Rena, get back!"

            show re sch open at halfright with dissolve 
            voice rena_squeal
            re "Huh..? What's going on guys?"

            voice kei_hua
            k "Stay back Rena! Its her!! She's at it again!"

            show re sch open close at halfright with dissolve
            voice rena_uuu
            re "Eh..? By she, you mean...?"

            show re sch open at halfright
            k "Look over there! Your trap is way too obvious, Houjo Satoko!!!!" with dpunch
            
            "I pointed to the top of the doorway."
            "Suspended in the crack at the top of the door was an eraser."
            "If I had recklessly opened the door, it surely would have been my demise."


            show mi sch laugh with dissolve
            m "Guess the game is on again today."
            m "Kei-chan keeps getting better and better at spotting Satoko-chan's traps."
            m "You may even defeat her today."

            
            k "No!" with vpunch
            k "Satoko isn't this naive." with vpunch
            k "There must be some trick involved!" with vpunch
            "I leaned in to get a closer look at the eraser."
            "To my eyes, it seemed to be an ordinary eraser."
            "When I first transfered here, Satoko had trapped the doorway in a similar manner to the way she had today."
            "However, the eraser that fell on my was not an ordinary eraser."
            "Satoko had put rocks in the eraser to make it heavier. Thanks to her, I left my first day at a new school covered in bruises."

            show re sch smile at halfright with dissolve
            re "Why don't you just stand back and open the door?"
            show re sch smile close at halfright with dissolve
            re "I wonder if you can dodge the eraser, I wonder...?"


            k "Rena isn't thinking hard enough."
            show re sch open at halfright
            k "The eraser is only one piece of Satoko's master trap."
            k "It is a red herring, a mere distraction meant to lure me into missing the greater threats!"


            "Rena looked dumbfounded and Mion simply laughed."

            m "Hehehe... I wonder who will win today...?"
            show mi sch grin with dissolve
            m "Kei-chan is in top form this morning."

            "I searched the rest of the door, looking for anything else that seemed remotely suspicious."
            "That's when I spotted it: the glint of thumbtacks taped to the inside of the door-handle."
            "Had I not found them, Satoko would surely have left me wounded and defeated, however, today was my day as the victor."

            k "Aha! Checkmate Satoko!" with vpunch
            k "The real trap is the thumbtackes in the door-handle!" with vpunch

            "Pulling the end of the tape, I masterfully stripped away all of the thumbtacks from the inside of the door-handle."

            k "You may have created a brilliant combination trap, but the mind of Maebara Keiichi is far superior!" with vpunch

            "Excited to see the look on Satoko's face when she realized I had won, I rushed into the classroom at full speed."
            scene classroom with dissolve
            pause 1.0

            "{i}*twang*{/i}" with vpunch

            pause 1.0

            "What was that?"

            pause 1.0

            k "Waaaaaaaaaaaahhhhhhhh!!!???" with vpunch

            pause 1.0 

            "Is that a rope? Why is the ground heading towards me so fast?"

            pause 1.0

            "{b}{i}*CRASH*{/i}{/b}" with vpunch

            show sa sch grin at halfright with dissolve

            sa "Ohohohoho! What do we have here?"

            "There she is. Houjo Satoko, the cheeky little trap mistress herself."

            show sa sch smile at halfright with dissolve
            sa "Good morning to you, Keiichi-san."
            sa "Causing a ruckus at this early hour?"
            
            k "I'm impressed, Satoko. This was a step up from your ordinary traps!"
            
            show sa sch sneak at halfright with dissolve
            sa "I haven't the faintest idea as to what you are refering to."

            k "Why, you little..." with vpunch

            "I tried to stand up, but I had landed on my knee when I fell. I grunted involuntarily at the pain."
            "I felt a small hand rest and pat my head."


            show ri sch laugh close at offscreenleft
            show ri sch laugh close:
                ease .25 zoom 3.0  yoffset 900 xoffset 500
            ri "Pain, pain, go away!~"

            "The one petting my head is Furude Rika. Unlike Satoko, she is an absolute angel."
            show mi sch smile at left behind ri
            show re sch smile at right
            re "Good morning, Rika-chan!"

            show ri sch smile:
                ease .5 zoom 1.0 yoffset 0 xoffset 500

            ri "Good morning, Rena!"
            show ri sch laugh close with dissolve
            ri "Good morning, everyone!"

            k "Wow, Rika-chan is a really good girl."
            k "The exact opposite of a certain someone."

            show sa sch irate close at halfright with dissolve
            sa "Lies! Slander! Murder!" with vpunch
            show sa sch irate:
                ease .5 zoom 2.0 xoffset -100 yoffset 400
            sa "You have no proof to back up any of your heinous words..."

            "I picked up Satoko by her uniform. She's only in middle school, so its like lifting a child."

            k "You better beware Satoko." with vpunch
            k "My finger flick has been known to split plywood." with vpunch

            show sa blank with dissolve
            sa "Ehhhh! Unhand me you brute!!!" with vpunch

            k "Hey, quiet down, people will get the wrong idea!"

            show sa irate:
                ease .25 zoom 1.0 xoffset 0 yoffset 0
            sa "Waaaaaaaaahhhh!" with vpunch

            "Satoko started crying."
            "Rika, being the sweet girl she is, walked over to comfort her."

            show ri sch smile:
                ease .5 xoffset 750
            ri "No need to cry, Satoko!"
            show ri laugh close with dissolve
            ri "Fight-on!"

            ri "And next time, you will set up an even more amazing trap."
            ri "Then you can squich Keiichi like a pancake!~ Nipah!~"

            k "Gah!! Being betrayed by an angel hurts so much more..." with vpunch


            show re laugh with dissolve
            re "Hauuuu!!"
            show re laugh:
                ease .5 xoffset -45
            re "Satoko-chan is crying... but it's soo kyuute!!!"
            show re laugh:
                ease .25 xoffset -95
            re "I wanna take her home!! Hauuuuuuuuuuuu!!!!!" with vpunch

            #end scene wipe to Keiichi's Bedroom
            window hide
            pause 2.0
            show endofchapter with slowdissolve

            pause 3.0
            hide endofchapter with slowdissolve

            scene mae_door_dusk with dissolve
            "Later that evening I recieved a knock on the door from Rena and Mion."

            show re sch smile at center with dissolve
            show mi sch smile at halfleft with dissolve
            re "Hey Keiichi-kun!"
            show re close with dissolve
            re "Tomorrow, Mii-chan and Rena were thinking that we'd like to show you all around Hinamizawa!"

            show mi grin with dissolve
            m "You'll be joining us, of course, right, Kei-chan?"

            k "I'll check my schedule."

            show mi open with dissolve
            m "But you're being invited by two girls!!!"

            show re sch open with dissolve
            re "Keiichi-kun, I wonder are you free? Are you?"

            k "I am."
            show mi irate
            m "Woah woah! Why do you treat Rena-chan differently than me!????"

            "Mion and Rena left soon after extending the invitation."
            scene kei_room_lamp with dissolve
            "I thought it was really nice of them to give me a tour of Hinamizawa."
            "I knew how to get to school pretty well, but the rest of the village was a complete mystery."
            

            "*The next day*"
            scene hi2_day with dissolve

            "Mion and I met up at the usual spot. Rena, however, was nowhere to be seen."

            k "Hey, Mion. Where's Rena?"
            k "She's never late like this."


            m "She said she was going to make bento for you, so she's probably pulling out all the stops."
            m "Though I hope she doesn't go too much overboard."
            "I could hardly imagine the immense intricacies of a bento that would cause Ryuugu Rena to be late, but sure enough I soon could see Rena's figure approaching."
            "In her hands was a large wrapped bento."
            "Wait, at a second glance it should be described as many bento stacked together!"
            "How much food did Rena make?"
            re "Sorry I'm late!"
            re "Ok...1...2...3..."
            "*thud*"
            "Rena set down the large stack of bento, with a thud. Clearly, the food weighed a considerable amount."

            m "Hey, Kei-chan. Rena really went all out making you this bento. It's a shame that a delicate girl like Rena would get exhausted carrying it all day."

            k "I completely agree. I am a man of honor. I shall take responsibility for my actions and bear this load."

            re "Keiichi-kun...? Mii-chan..? What do you mean take responsibility...? Hauu..."

            "Fortunately for her, taking responsibility meant carrying around the food that Rena made."
            scene hi3 with dissolve
            pause 3.0
            scene hi9 with dissolve
            pause 3.0
            scene hi1_view with dissolve
            pause 3.0
            "Rena and Mion led me through the main shopping area of Hinamizawa."
            "We passed by kind villagers who all knew who I was, though they seemed to be complete strangers to me."
            "It was a beautiful day for a walk around the village. Days like these make me so glad that I live in Hinamizawa."
            scene shrine_day with dissolve
            "Finally, Rena and Mion brought me to a steep outdoor stairway, appearing to lead to a shrine of some sort."

            re "Welcome to the Furude Shrine!"

            m "Next Sunday there will be a huge festival here!"

            k "Hmm...?{w} It seems a little early in the summer for a festival."

            m "Well, the {i}Watanagashi{/i} is a festival celebrating the end of winter!"

            "Mion and Rena continued up the stairs at a pace far faster than my own."
            "Of course, they weren't carrying all of our food, so our experiences climbing up were likely uncomprable."
            "From the top of the stairs, I could see Rena and Mion setting out a picnic blanket."
            "As I reached them, they quickly and masterfully stole the bento from me and began setting out dishes left and right."


            re "Eat up!"
            m "And make sure you eat all of it, Kei-chan... You're in for a whole lot of pain if you make Rena cry."
            k "I'm a man! I'll do my best, but... {w} this is a lot of food!"
        
            "Suddenly, from the shadows, a voice rang out."

            sa "Well, well, well... What do we have here?"
            "Suddenly, also at the top of the stairs were Satoko and Rika."
            ri "Good morning, everyone!"

            k "Good morning, Rika-chan! We are about to eat the gormet feast that Rena made us!"

            sa "Yes, yes. I can see that."
            sa "I just have a single question."
            sa "Why have you laid out a tarp on our private property?"

            k "Shrines are open to the public! You can't keep us from picnicking here!"

            ri "Keiichi's right. Anyone is able to use this space."

            k "As usual, Rika-chan is a really good child.{w}Come have a seat and dig in!"

            ri "Thank you so much!"

            sa "Hold on a second!!"

            "Satoko puffed out her chest."
            
            sa "Wherever am I supposed to sit!?"

            k "Nowhere, because you're not getting any of this food!"

            re "H-hold on Keiichi. It's fine~{w}You can have some too, Satoko-chan-"

            k "Not!{fast} {p}I'm going to eat it all first!"
            "I shoved as much food as I could into my mouth at once."
            sa "Rikaaaaaa! Make him stop!"
            "Rika walked over to Satoko and pet her on the head."
            ri "Take these chopsticks! Use them wisely to defeat Keiichi!"

            "Satoko sat herself down next to me, and before I knew it an impromptu eating contest begun between Satoko and me."
            m "Boy, Kei-chan...You're pretty good at roping people into doing stuff..."
            ri "We need to work fast to catch up, otherwise Satoko and Keiichi will eat it all!"
            m "No kidding!{w}We old farts better get in on the action while we can!"

            "Suddenly, it was an all out war for food."
            "Any tricks and tactics were allowed."
            "As I reached over the table to refill my plate, a pain suddenly hit my abdoman."
            k "Hey, Satoko! Elbowing me is cheating!"
            sa "Ohohoho! No hamburg steak for you!"

            k "That's it... "
            k "Houjou Satoko! The hour of your defeat has arrived!!!"
            "Using my chopsticks as skewers, I deftly pierced as many meatballs as I could at once, keeping everyone, but mostly Satoko, from taking more."

            sa "No! Not the meatballs!"

            k "My, my, my. They're so plump and juicy... Abosultely phenominal!"

            "Satoko looked in the bento, looking for an opprotunity to strike."
            "Suddenly, before I knew it, she pounced, completely emptying a corner of one of the bento."

            sa "While you were busy stuffing your face, I am going to finish these tamagoyaki!"
            "She shoved them all in her mouth at once."
            sa "Wow! They really melt in your mouth! So delicious..."

            "I can't believe I only met my friends three weeks ago. It feels like we have known eachother forever."
            "I was so lucky that my friends were treating me with care to help me, a transfer student, fit in their village."
            "It was thanks to my friends that I learned how fun a simple day like today could be."
            "It was thanks to my friends that I learned how tasty bento could be if you were eating with other people."
            "If my everyday life could stay like this, then I would fo everything I could to keep it that way."
            pause 2.0
            "I truly am glad that I moved to Hinamizawa and met my friends."
            window hide
            pause 2.0
            show endofchapter with slowdissolve

            pause 3.0
            #end scene, open tips menu
        label end_oni1:
            stop music fadeout 5.0
            scene black with slowdissolve
            call screen end_oni1
        label oni2:
            "Having completely devoured all of Rena's delicious food, we spent the rest of the afternoon hanging out."
            "I didn't realize how late it was until suddenly the sun was setting."
            "Satoko and Rika left as soon as the sun started to set."
            "Its important for kids to get home safely before it gets too dark."
            "That left Mion, Rena, and me to clean up and carry everything home."
            "Not that I'm complaining. I would do ten times the amount of work for an afternoon with my friends."
            "Eventually Mion parted ways with us, as we had reached the fork in the road that divided our homes."
            m "Bye, guys! See you all tomorrow."
            k "Mion, thank you so much for showing me around today."
            k "I really appreciate it."
            m "Haha! No worries Kei-chan. See you guys tomorrow!"
            re "Bye bye!~"
            pause 1.0
            "Rena and I continued on towards our homes."
            re "I wonder... did Keiichi have fun today?"
            k "Yeah, loads! I'm actually kinda bummed we're all going home."
            "Rena stopped in front of me with a smile."
            re "Well... is it okay then if we make one stop on the way back? Is it...?"
            k "Sure. Where are we going?"
            re "Its a suprise!~"
            "Rena led me down a new path I had never taken before."
            "The sky was a beautiful amber color and the summer higurashi were singing their song."
            "Eventually we came to a gate, which opened up to a massive trash dump."
            "There were piles and piles of junk of all sorts, from furniture to electronics to toys, and, of course, the requisite garbage.."
            "I wasn't sure whether Rena had taken me to the right place, until I heard her speak."
            re "I wonder what's here! I wonder!~"
            "She sprinted down expertly hopping through the trash heap."
            k "You wanted to go climb a pile of trash, Rena?"
            re "It's not trash!"
            re "To me, it's a pile of treasure!"
            "Treasure...?"
            re "Maybe I'll find something kyute..."
            re "I can't wait!~ Can't wait!~"
            "She ran so far ahead that I couldn't see her anymore."
            "*Sigh*"
            "I guess I'll follow her. Besides, climbing around in the dump seems kinda fun."
            k "Rena! Wait up!"
            "I tried to climb down into the dump, but my footing slipped and I fell down."
            "Oof, that hurt. How does Rena do it?"
            re "It's okay, Keiichi-kun!"
            "Rena's voice came from over the next mound of trash."
            re "You just wait over there!"
            "Sheesh..."
            "I clambered out of the dump and onto stable ground."
            "I laid down and stretched out, staring at the summer sky."
            "What a wonderful day."
            "The sunset is so beautiful."
            "I never want these days to end."
            "..."
            "..."
            "Before I knew it, my eyes had closed and I had fallen asleep for a few seconds."
            "No worries. When I open my eyes I will see the same beautiful summer sky."
            k "Gaahhh!"
            "When I opened my eyes, the last thing I expected to see right above my eyes was a camera lens."
            "???" "Woah, you scared me!"
            k "I think you mean the opposite!"
            k "You're the one who scared me!"
            "???" "Whoops. Sorry about that. I didn't mean to startle you."
            "Didn't mean to startle me? Who in their right mind would take a picture of a sleeping child and then be suprised when the child is startled..."
            "The man's voice brought me back to focus."
            "???" "Do you live here in Hinamizawa?"
            "Who was this man? Why did he think I would reveal any information to him?"
            "Having sensed my discomfort, the man made ways to introduce himself."
            "???" "The name's Tomitake."
            "Tomitake" "I'm a freelance photographer. I come by Hinamizawa every now and then."
            "He acted very familiar with me, which was strange considering I had never met him before."
            "Granted, lots of people in the village treated me like that, but this guy isn't even from Hinamizawa..."
            "Tomitake" "There's so much beauty just waiting to be captured on film."
            k "Shouldn't a professional photographer know better than to take someone's photo without asking permission?"
            "Tomitake" "Ahaha. No worries!"
            "Tomitake" "I'm used to taking pictures of birds, since I don't need to ask their permission!"
            "As if that makes it any better!"
            re "Keiichi-kun!"
            "Luckily, there was Rena's voice to calm me down again."
            "Let's see... Where is she now...?"
            "I turned and looked toward the sound of her voice. Rena was standing atop a broken down car."
            "She was pretty deep out there. It's impressive she made it so far."
            re "Sorry to keep you waiting, Keiichi-kun! I'm all done!"
            "Tomitake" "Oh, I didn't realize you were here with a friend."
            "Tomitake" "What on earth is she doing in a place like this?"
            "Tomitake asked me, as if I knew more than him about why Rena brought me here."
            "Might as well have some fun while I'm waiting for Rena."
            k "I have no idea why she's here."
            k "Maybe she's checking in on a dismembered corpse or something."
            "I expected Tomitake to react in some way, but he just looked at me."
            "Whoops... I ended up saying something that I would only say to one of my friends. I guess he didn't really get my sense of humor."
            k "Never mind... I was just kidding..."
            "Tomitake continued to look at me with that somber expression."
            "Tomitake" "What a terrible incident."
            pause 2.0
            "Huh...?"
            pause 2.0
            "What did he just say?"
            pause 2.0
            "I could have sworn he just said..."
            "Tomitake" "I hear one of his arms is still missing."
            pause 3.0
            re "Thanks for waiting, Keiichi-kun!"
            "Oh. When did Rena get here?"
            re "I'm sorry that took so long, so sorry!~"
            "She then realized that Tomitake-san was here."
            re "Oh, good evening."
            "Tomitake" "Good evening."
            "Tomitake" "I don't want to be a third wheel here, so I'll see you guys around."
            "Tomitake" "Sorry again for scaring you, Keiichi-kun."
            "He walked away."
            "What was it he said again...?"
            "His arm...missing...?"
            re "Keiichi-kun?"
            "Rena's voice again brought me back to the present."
            k "Ohh, uhh. Did you find any buried treasure?"
            "Rena's face brightened up."
            re "I did! I did!"
            re "I found a Kenta-kun doll!"
            k "Kenta-kun doll? You mean the ones you see in front of those fried chicken joints?"
            re "Yeah! A Kenta-kun!~"
            re "Hauu, it's so kyute!"
            re "I wanna take him home!!"
            k "He's in the trash so you can take him home if you want."
            re "Well, I would if I could but he's buried deep in the bottom of the pile."
            re "And its getting dark soon..."
            k "How about we come by again and I'll help you get him out?"
            k "That way I can pay you back for that awesome bento you made us."
            "Rena beamed from ear to ear."
            re "Thank you!"
            re "Keiichi-kun's gonna help me... and Kenta-kun's gonna come home with me! Hau~"
            "As weird as it is, I'm kinda glad Rena brought me to the junkyard."
            "Her obsession with kyute things is adorable, and she is such a nice girl."
            "Everyone here in Hinamizawa has been so nice."
            "I keep meeting new people... it's amazing how many people you meet in a small town."
            "Like Tomitake-san. Weird as he is, he seems like an alright guy."
            "Except...what was that thing he said...? About some incident?"
            k "Hey, Rena?"
            k "Did something big happen around here a while back?"
            re "Yeah! They were gonna build a dam here."
            k "Did anything happen at the build site? Like an accident, or some kind of incident..."
            re "I don't know.{fast}"
            pause 2.0
            "Eh?"
            re "I only moved here a year ago, you see!"
            k "Huh? You're also a transfer student? I had no idea."
            re "Yeah! That's why I dunno about stuff that happened before then! Sorry!"
            "I wonder..."
            "Did something happen here in Hinamizawa?"
            "Only the higurashi could know the true answer to that question."

            window hide
            pause 2.0
            show endofchapter with slowdissolve
            pause 3.0
            hide endofchapter with slowdissolve

            "It was the next day after school."
            
            m "The creed of our club is to obtain games from all eras and nations, and to play these games to their fullest potential!"
            m "I am pleased to announce that, despite coming in dead last, our latest club applicant showed incredible promise during his evaluation game, and, as such, I, Sonozaki Mion, president of this club, do hereby welcome our newest member..."
            m "Maebara Keiichi!"
            "This was it. My chance to prove myself."
            m "Now, are you ready for today!?"
            "Last week Mion and the rest tested my skills by playing a game of old maid."
            "I lost, and as a result was forced to walk around town with marker scribbled all over my face."
            k "It's all your fault anyway! You guys and your shifty card tricks..."
            k "Do you know how much humiliation I had to endure?!"
            re "I mean, you did lose, so you had to face the penalty game... right...?"
            k "A penalty game!?"
            k "This was far worse than that!"
            k "Mion used that torture device to completely ruin my face!"
            m "You aren't spreaking about this, are you Kei-chan?"
            "Mion whipped out a thick marker. The very tool used to desecrate my face."
            k "Of course I mean that! And it's permanent ink, too! My mom caught me wiping off all that crap in the bathroom! Have a little sympathy!"
            sa "You're such a drama queen, Keiichi-san."
            "Rika again came over and pet my head, which naturally caused Rena to go into a kyute fit."
            ri "Poor, poor Keiichi!"
            k "So... What game are we playing today? Old maid again? Tycoon?"
            m "Nah, it wouldn't be fair to youto play another card game. You have an inherent handicap. Let's do something else..."
            pause 1.0
            m "How about a treasure hunt instead?"
            m "I'll hide this marker somewhere in the school building."
            m "Whoever gets their hands on it first, wins. That sounds fair, doesn't it, Kei-chan?"
            k "Hold on. If you hide the treasure, you can't play the game. How are you supposed to get a penalty game??"

            m "Fine, I'll add a special rule!"
            m "If you are the first to find the treasure, Kei-chan, I will let you scribble on my face."
            "There it was. My win condition."
            "All I had to do was find a treasure? Easy."
            "I could see the prize in sight."
            k "You better not take back those words, Mion!"

            "Before I knew it, the game had begun."
            "I had to think strategicly... Where would Mion hide the treasure?"
            "I ran down the hallway, and stopped at the end."
            "Perhaps... she hid it under the cubby?"
            pause 1.0 
            "Dammit... Mion where did you hide it?"
            "I ran back to the classroom. The cabinets in the back of the room looked suspicious."
            "I threw open each cabinet, pulling the contents out, hoping that the treasure would be in there."
            "There was only some gardening tools, a cardboard box, a bunch of old baseball stuff..."
            "The marker was nowhere to be seen."
            "Stay cool, Maebara Keiichi!"
            "Knowing Mion, she probably wants to make sure anyone but me finds the treasure."
            "I ran down the hall again, passing the storage room."
            "I couldn't rule that room out, so I entered the dark room."
            "I bet because I'm new here, Mion decided to hide the treasure in this room that was a mystery to me."
            "I turned the corner passing a large shelf full of papers and books."
            "Oh...? Is that...?"
            k "Rena!"
            re "Keiichi-kun!"
            "Wait, I need to remember. Club rule #2."
            k "You're not going to let me win, are you..."
            re "Sorry Keiichi-kun. \"Always strive for victory with everything you've got!\""
            "Of course. Rena wouldn't let me win that easily."
            "Suddenly, from behind us ran Satoko and Rika."
            sa "Pardon me!"
            ri "Excuse us!"
            "Just as soon as they had arrived, they were gone."
            "Of course, they too were my enemies here. They were also after the treasure."
            "I looked toward where they were running."
            "At first it seemed like nothing was there, but then out of the corner of my eye I saw it."
            "Nestled next to some crates was the treasure: Mion's marker!"
            "Satoko and Rike were both sprinting toward it."
            "Suddenly, Rika pulled ahead."
            "She reached for the marker, as it was nearly within her grasp."
            "Suddenly, a shrill voice cut through the air."
            sa "Did you really think I would let you win? Rika, take this!"
            "Satoko pulled a rope, causing a bunch of metal pots to fall from the ceiling."
            "Another one of her master traps."
            sa "You're still no match for my ingenious traps, my sweet, little Rika!"
            sa "Ohohoho! Remember Rika. When I decide to win, I win with absolute certainty."
            "Satoko was laughing with glee, clearly overjoyed that she outsmarted Rika."
            m "Satoko, I think that's enough..."
            "Rika got up out of the pile of pans."
            ri "It's okay! I lost. I'm not mad about it at all."
            ri "In fact, give me one second! I will be right back!"
            "She ran out of the storage room only to return a few moments later holding a strange box."
            "It was the one that was in the cabinets at the back of the classroom. I guess it was Rika's."
            ri "Satoko, because you won, I've got you a special victory present!"
            "Satoko blushed, not expecting this sudden act of kindness."
            "Though only a moment later, she pulled herself together."
            sa "That's the Rika I know. Always on top of things."
            ri "Congratulations Satoko! Nipah!~"
            "Satoko leaned in to see what was in the box."
            "At that exact moment, Rika pressed a small button on the box."
            "{b}*BAM*{\b}"
            k "Sa-Satoko?!"
            "Satoko flew across the room."
            "A giant spring-loaded fist popped out of the box, socking Satoko right in the face."
            "A clever trap that foiled the Trap Master herself. Rika is a clever girl..."
            sa "Wha...what happened?"
            "Satoko got up and... was that...?"
            m "Ahahahaha! Now that's the Rika-chan we know!"
            "Satoko clearly couldnt see what had happened."
            k "Satoko... your face."
            "Stamped on Satoko's face in bright red were the letters K and O."
            "Knockout."
            "Satoko may have won the game, but Rika had bested Satoko in the end."
            sa "W...what is this!?"
            ri "I prepared to fight your traps. Nipah~"
            m "Haha! Satoko is no maych for Rika-chan."
            "Mion and I laughed together. We turned toward Rika, expecting her to join us."
            k "Eh...? Rena...?"
            "She was standing right next to us, but her eyes were staring into another world."
            "As I said her name, Rena began to focus more on the classroom."
            re "Oh, sorry. I'm a little sleepy... Maybe all that fun wore me out!"
            "She looked really tired."
            m "Are you alright, Rena?"
            "She nodded."
            re "Yeah. I think I'm gonna go rest in the nurse's office, then go home."
            k "Oh Rena! When you're feeling better, I'll help you out with Kenta-kun!"
            re "Th..thanks..."
            sa "I'm going to wash my face. It would be embarassing to go outside looking like this."
            "Satoko went up next to Rena."
            sa "Rena-san, I'll walk you to the infirmary."
            re "Hauu...thank you Satoko-chan..."
            "Rena and Satoko made their way down the hall."
            "I could still hear them talking as they get further away."
            re "Hauu~ The stamp mark on your face is so kyuute... I want to take you home~~"
            sa "Wha...? How come-!?"
            m "I guess that's it for today... Kei-chan, do you want to walk home together?"
            scene black with slowdissolve

            m "A Kenta-kun doll?"
            m "That's right up Rena's alley."

            k "Hey, Mion? You know about that dam construction site?"
            k "Did anything ever happen there?"

            m "Sure did! A whole war, basically."
            m "We demanded for the construction to stop, hosted sit-ins, and held big protests."

            k "Makes sense that everyone would fight. The dam would've flooded your homes."

            m "The government cronies were dead set on seeing the project through."
            m "Once they found out they couldn't bribe their way to victory, they resorted to some really nasty tactics."

            k "I'm suprised the villagers still ended up winning, especially against te government."

            m "The mayor and all of the village bigwigs signed petitions. They went to Tokyo and struck deals with politicians."
            m "Thanks to all their hard work, the dam project was finished. The sweet taste of victory was ours."


            k "There wasn't, like, any violence or anything, right?"
            k "No one got assaulted...or murdered?"

            m "Of course not."

            m "Okay, see you tomorrow!"
        label end_oni2:
            stop music fadeout 5.0
            scene black with slowdissolve
            call screen end_oni1

        label oni3:
            "I am at the dump wowee"


            k "There she is."
            k "Yo, Rena! Working up a sweat?"

            re "Keiichi-kun?!"
            re "Why are you here?!"

            k "I recieved word of an emergency in the area and rushed to the scene!"
            k "Where's the man in need of grave assistance?!"

            re "Huh? What? An emergency?!"

            k "Yes! I got a report about a Kenta-kun doll buried deep in a pile of trash?"

            re "O-oh! C'mon Keiichi-kun, you scared me!"

            k "I'm just messing around. I promised I'd help, remember?"

            re "Eh...? You came all the way here for me...? Hauu..."


            k "So where is Kenta-kun at?"

            re "Over here!"


            re "Right there. See him underneath?"

            k "You were really going to try to get him out from there all by yourself?"
            k "Here, get out of the way."


            k "Man... I wish we had an axe or a saw or something..."

            re "It's fine Keiichi-kun."

            k "No worries! If Rena-chan wants it, I'm happy to help."



            k "O-okay, let's take a break."

            re "H-hey, let me go get us some barley tea!"
            re "My house is super close!"
            re "Stay there, okay!"










    label oni_tip1:
        "Hauuu!~"
        "There's a new pile of treasure!"
        "How exciting...!"
        pause 3.0
        "This froggy is so kyute!~"
        "Hauuu! A cute red post box!!~"
        pause 3.0
        "Over there! Could it be...?"
        return

#label splashscreen:
    #$renpy.movie_cutscene("op.mp4")
    #return

