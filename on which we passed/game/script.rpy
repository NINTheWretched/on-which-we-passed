# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Izumi")

define y = Character("Yu")

define h = Character("Hitomi")

define hheart = Character("Hitomi <3")

define g = Character("Girl")

# The game starts here.

label start:

    stop music

    scene bg cw

    "This game contains sensitive material over the topics of self harm and sexual abuse."

    "Do you still wish to continue?"

menu:

    "Yes.":
        jump c1_yes

    "No.":
        jump c1_no

label c1_yes:

    jump c1_cont

label c1_no:

    $ menu_flag = False

    return

label c1_cont:

    scene bg yusroom

    play sound "audio/computer_hum.mp3" loop

    "Track fourteen ends and the album comes to a full stop."

    "I'm back here again."

    "Left with nothing but the quiet hum of my computer."

    "I'm staring into the ceiling."

    "My mind is going nowhere."
    "I am going nowhere."

    "My sister cracks the door, opening it just enough to reveal herself to me."

    show izumi talk at right

    i "Yu, I'm heading out."
    i "I love you..."

    show izumi quiet at right

    y "Yeah."
    y "See you in a bit."

    "She hesitates, waiting for me to say, 'I love you.' back."
    "I never did..."

## SKIP POINT
    $ renpy.stop_skipping()

    stop sound

label jrstation:

    scene bg jrrailway

    play music "audio/tennoji_station.mp3" loop

    play sound "ambulence_siren.mp3"

    "Izumi was only eighteen."

    "I still remember when the police came to our door."

    "They told us she was involved in a 'human body railway incident.'"
    "Dad and I both knew what it meant."

    "He didn't go back to work for weeks."

    "Not long after, I moved out."

    "I think about that night all the time..."
    "If I could have stopped her."

    "If things would have been different had I just said-"

## SKIP POINT
    $ renpy.stop_skipping()

    stop music

    stop sound

label yuroom2:

    scene bg yusroom

    show izumi quiet at right

    play sound "audio/computer_hum.mp3" loop

    y "I love you too."

## SKIP POINT
    $ renpy.stop_skipping()

    stop sound

label intro_sequence:

    $ renpy.movie_cutscene("videos/owwp_opening.webm", delay=None, loops=0, stop_music=False)

label encounter:

    scene bg konbi

##play shop sound of japanese convenience store or checkout

## SKIP POINT
    $ renpy.stop_skipping()

    "I take my sandwich from the counter, and bow before I walk away."

## insert an "audio" clip of the sliding door sound here so that it carries into the next scene.
##play cicadas "sound" on a loop after that (possibly on a fadein.) play low because music

    play audio "audio/sliding_door.mp3" volume 1.0
    play sound "audio/cicada.mp3" fadein 1.0 volume 0.2 loop

    scene bg lensflare

    "The sliding doors open, spitting me out into a street with light afternoon traffic."

    play music "audio/but_i_saw_a_piercing_light_last_night.mp3" loop

    "A group of girls runs past."

    "The glare of the sunlight hides their faces, but their figures are clear."

    "They laugh softly, making jokes between one another."

    "I step onto the sidewalk, watching as they turn back to yell something at me."

    y "What are they saying...?"

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg hittalk

    show hitomi smilingupstreet at right

    "A straggler from the group walks up, coming to a halt just beside me."

    "It's a girl."

    "Her face is softened by the shadows of the trees overhead."

    show hitomi smilingtalkingupstreet at right

    g "Sorry about that."

    show hitomi smilingupstreet at right

menu:

    "Don't worry about it.":
        jump c1_dwai

    "Were they talking to me?":
        jump c1_wtttm

label c1_dwai:

    $ menu_flag = True

    show hitomi smilingtalkingupstreet at right

    g "Honestly..."
    g "Sometimes, they can be so annoying."

    jump c1_fin

label c1_wtttm:

    $ menu_flag = False

    show hitomi smilingtalkingupstreet at right

    g "No..."
    g "They were yelling to me."

    jump c1_fin

label c1_fin:

    show hitomi smilingeyesclosed at right

    g "You can just ignore them."

    show hitomi smilingeyesopenht at right

    g "I'm-"

    show hitomi shocked

    "As she turns to me, the smile drops from her face."
    "It's as though she has seen a ghost."

## SKIP POINT
    $ renpy.stop_skipping()

    $ renpy.movie_cutscene("videos/enc.webm", delay=None, loops=0, stop_music=False)

    show hitomi shocked at center
 
    y "Are you alright...?"

    show hitomi confused
    g "Yu...?"
    g "Yu Sato?"

    "Why does she know my name?"

    show hitomi confused2
    g "Your name is Yu, isn't it...?"

    y "Yes..."

    show hitomi ecstatic
    g "Oh my god!"

    h "It's me! Hitomi!"
    show hitomi smilingeyesclosed
    h "Hitomi Yoshinaga, from junior high school!"

    show hitomi smilingquiet
    y "Oh..."
    y "Yeah. I remember you."

    "I'm more surprised that she remembers me."

    y "Nice to see you again."

    show hitomi smilingeyesopenht
    h "You too!"
    h "It's been too long!"

## SKIP POINT
    $ renpy.stop_skipping()

    show hitomi smilingupstreet

    "Hitomi turns to look at the group of girls, who are now farther up the street."
    "Their voices echo by, dissipating just beyond where Hitomi and I stand."


    show hitomi smilingtalkingupstreet
    h "I should go."
    h "They're going to leave me behind."
    show hitomi smilingupstreet
    "She laughs as she says it, but her final giggle reveals the truth as it fades into a quiet sigh."

    show hitomi smilingquiet
    "Hitomi turns back to me."

    show hitomi confused2
    h "Hey..."
    h "We-"
    show hitomi ecstatic
    h "We should hang out soon!"
    show hitomi smilingeyesclosed
    h "It would be nice to catch up."
    show hitomi smilingquiet
    "Her eyes soften with her smile."
    "She looks deep into mine, like she's trying to figure out what I am going to say next..."

    y "Well, I don't really..."

    show hitomi ecstatic
    h "I know! Let's swap numbers!"

    y "..."
    y "Okay..."
    show hitomi smilingeyesclosed
    y "Sure."

    show hitomi handout
    "She stands there beckoning as I dig my phone out from my pocket."

    show hitomi smilingeyesclosed
    "I place it in the palm of her hand, and she smiles as she switches between the screens."

    show hitomi handingphone
    "She punches in the numbers, and flips her phone closed with a look of accomplishment."
    "She holds my phone back out to me, and puts hers away simultaneously."

    hide hitomi
    "As I take it from her hand, she jogs off towards her friends."

    "Hesitating slightly, she turns back."

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg hitomiwa
    "The sun envelops her under a blanket of white and red hues."
    "Her shadow reaches out, joining with mine."
    "Everything that is the person who calls herself Hitomi Yoshinaga, stands just before me."

    "A smile forms across her face."

    h "See you soon!"

    scene bg lensflare

    "She takes off and rejoins with the group."

    "As they round a corner in the distance, I look back down at my phone."

    "The contact name reads..."

    scene bg hitomi
    " "

    stop music

    stop sound

label texting:

## SKIP POINT
    $ renpy.stop_skipping()

    play music "audio/tabasko_after_the_flood.mp3" loop

    scene bg phone

    hheart ">I’m sorry if I was too forward in asking for your number."

    hheart ">I just thought it would be nice to see you again after so long."

    y "It's alright.<"
    y "I don't mind at all.<"

    "Back in school, Hitomi was always the sociable one."
    "She ran for class president."
    "And won of course."
    "She always answered questions in class."
    "Made friends with the new students."
    "Went to all of the dances and events."

    "I never did."

    hheart ">Oh, thank god."
    hheart ">I don't want to be annoying."

    y "Is that really why you wanted it?<"

    hheart ">Wanted what?"

    y "My number.<"

    hheart ">Oh! Oh!"
    hheart ">Sorry. I'm stupid."
    hheart ">Yeah!"
    hheart ">I just wanted to catch up!"
    hheart ">Maybe we could get lunch!"
    hheart ">Or something!"
    hheart ">I don't know."
    hheart ">Totally up to you!"

    y "I don't get out much, but I'm fine with that.<"

    "My stomach is turning at the thought of it."

    "Being around others..."

    "I try not to get close to people anymore."

    y "Was there something specific that you had in mind?<"

    hheart ">Do you like coffee?"

    y "I try not to drink it too much, but I like lattes.<"

    hheart ">Perfect."
    hheart ">It's settled then."
    hheart ">How does this Saturday sound?"

    y "I'm not busy.<"

    "I'm never busy."

    hheart ">Awesome!"
    hheart ">Let's do 12:30 at Ko Coffee!"

    y "Sounds good.<"
    y "I'll see you there.<"

    hheart ">See you :)"

    stop music

label chapter2start:

    stop music

    stop sound

    stop audio

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg cafewide

    play music "audio/pmu_cafe.mp3" loop

    "The incessant hum of people speaking around me rises in volume with each minute."

    "Every time the entry bell rings, I turn to look."

    "It's never Hitomi."

    scene bg cafeoutside

    "Maybe she's not coming..."

    "Shit."

    scene bg yuhands

    "Of course she's not."

    "I wouldn't."

    "That's probably what her friends were yelling."

    scene bg enc

    "It was the plan."

    "This whole thing was a cruel prank."

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg black

    "I didn't even want to do this."


##DOOR DING SOUND

    $ renpy.movie_cutscene("videos/hitnotice.webm", delay=None, loops=0, stop_music=False)

label talks:
    
    scene bg black

    h "Hey..."

    scene bg hitomienter

    h "I hope that I didn't make you wait too long?"
    h "It seems like you've been here a while."

    scene bg ythought

    y "I have, but I chose to come here pretty early."
    y "I don't get out very much,"
    y "so I try to give myself some time to acclimate."

## SKIP POINT
    $ renpy.stop_skipping()


    scene bg yuthought2

    h "I see."

    h "Well, I'm glad that you agreed to come out to meet with me!"

    scene bg ythought

    y "I thought about what you said..."
    y "And I guess that I decided it would be nice to catch up."

    scene bg hitomiwoah

    h "Woah!"
    h "There he is!"

    h "I never thought I would see my Yu Sato again!"

    scene bg hitomiwoahcl

    "I feel..."
    "Strange."

    "Safe."

    "Like I could almost laugh too."

    "It's been a long time since I've felt this way."

## SKIP POINT
    $ renpy.stop_skipping()

menu:

    "Apologize.":
        jump a1_sorry

    "Refuse change.":
        jump a1_ly

label a1_sorry:

    y "Sorry..."

    scene bg hitomijeez

    h "Jeez..."
    h "You apologize too much!"

    y "Yeah..."

    scene bg hitomithink

    "We sit in silence for a moment."

    jump a1_cont

label a1_ly: 

    $ menu_flag = False

##hitomi and yutogether distorted


    scene bg hitomithink

    "A moment of silence falls between us."
    "The air fills stiffer than before Hitomi arrived."

    "Things are falling apart..."
    "Back to the way that they were."

##please help me

    "Everything."
    "Always."
    "Returns."

    jump a1_cont

label a1_cont:

    scene bg hitomijeez

    stop music

    play music "audio/oh_boy_ok.mp3" loop

    h "Hey..."
    h "Yu...?"

    scene bg hitomithink

    "I'm brought back out of it."

    y "Yeah?"

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg whathap

    h "I'm sorry if it feels like I'm being too forward..."
    h "But, can I ask you something that might be a little personal?"

    y "Sure."

    scene bg hitomimouth

    h "What happened to you in junior high school?"

## SKIP POINT
    $ renpy.stop_skipping()


##The scene with izumi will have to be an animation so that there is no dialogue box visible on the screen
##unless I can find a way to hide it??

    scene bg izumi
    play sound "audio/static.mp3" fadein 1.0 volume 0.1 loop

    "..."

    stop sound

    scene bg whathapquiet

    y "Huh...?"

    scene bg whathap

    h "You just seemed to become..."
    h "Distant."

    scene bg izumi
    play sound "audio/static.mp3" fadein 1.0 volume 0.1 loop

    "..."

    stop sound
    scene bg whathapquiet

    y "Distant...?"

    scene bg izumi

    play sound "audio/static.mp3" fadein 1.0 volume 0.2 loop
    "..."

    stop sound
    scene bg whathapquiet

    "Distant..."

    scene bg izumi
    play sound "audio/static.mp3" fadein 1.0 volume 0.3 loop

    "..."

    stop sound
    scene bg whathapquiet

    "Distant..."

    scene bg ilyt

    "..."

    scene bg izumi
    play sound "audio/static.mp3" fadein 1.0 volume 0.5 loop

    y "Izumi..."

    i "Yu..."

    h "Yu...?"

    h "Hey, Yu?"

    stop sound

    scene bg hitruok

    h "Are you okay?"

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg hitruok2

    y "What?..."
    y "Oh..."

    y "Shit."

    y "S- Sorry..."

    scene bg hitruok

    h "No, I'm sorry."
    h "I didn't mean to upset you."

    scene bg hitruok2

    y "No, it's..."

    scene bg hitruok

    h "We can skip past that."
    h "let's talk about something else."

    scene bg hitruok2

    y "No."

    scene bg heart

    "My heart has grown nails."

## SKIP POINT
    $ renpy.stop_skipping()
    "Like it's clawing at my throat to get out."

    "I'm choking up."
    "I can't say it."
    "What am I doing?"
    "Why do I want to tell her these things?"

    "I just need someone to hear me."
    "I don't care who it is."

    scene bg black

    h "Please..."

    stop music
    stop sound
    stop audio

    scene bg hitbeg

    play sound "audio/static.mp3" fadein 1.0 volume 0.6 loop
    play music "audio/breakdown.mp3" loop

    h "Stop."

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg hitomicry

    "..."
    "Her face."
    "She's..."
    "Crying."

    scene bg static

    "I barely even realized that the restaurant had fallen silent."
    "My head is filled with static."
    "All this noise."

    h "Please..."

    scene bg cafewide

    "Why did I do this?"

## SKIP POINT
    $ renpy.stop_skipping()

    y "This was a stupid idea."

    h "Yu..."

    scene bg standup

    y "I should have never come."
    y "I'm sorry."

    scene bg keepwalking2

    "Walk."

    h "Yu."

    scene bg keepwalking3

    "Keep walking."

    h "Yu!"

    "The door of the cafe opens to the street."

    scene bg reach

    "Keep walking."

    scene bg hitomistop

    h "YU!"

    scene bg black

    "Keep walking...?"

menu:

    "Yes.":
        jump p1_yes

    "No, I want to turn around.":
        jump c1_idka

label p1_yes:

    jump p1_a

label c1_idka:

    $ menu_flag = False

    "It seems like you've done enough."

    "What will you say to her?"

    "Is it really worth it?"

    menu:
        "Stop it.":
            jump p2_through

        "Wait...":
            $ menu_flag = False
            jump p2_through

    jump p1_a

label p1_a:

    "I let go of the door."

## SKIP POINT
    $ renpy.stop_skipping()

label p2_through:

    "My hand is..."
    "Warm."
    "It's all warm."
    "It's not my hand."

    scene bg handhold

    "I turn around to see Hitomi standing behind me."

    "Her hand is clinging onto mine."

    scene bg toknowyou

    h "I told you..."

## SKIP POINT
    $ renpy.stop_skipping()

    h "I told you that I wanted to catch up."
    h "Didn't I?"

    stop sound

label flashes:

    scene bg city

    "Hitomi forced me to get out of the house more and more often."

    "It didn't matter how much I hated it,"
    "or how little I wanted to go."

    "I ended up with her anyways."

    scene bg mrsdonut

    "Her favorite place to eat is Mrs. Donut."

    "Days are creeping into weeks..."
    "Weeks into months."

    scene bg favcolor

    "Her favorite color, white."

    "A construct."

    scene bg const

    "Her favorite thing about me is my composure."

    "That's what it feels like."
    "Like I am watching it happen from the outside."

    scene bg break1

    "She's an only child."

    "Am I truly happy?"
    "Or am I just going through the motions?"

    scene bg andicant

    "She wants to be an UNIKO model."

    "Is this all there is for me?"

    scene bg questionyourself

    "This is it."
    "This is me."

    scene bg food

    "Lunches."

    scene bg artex

    "Art exhibits."

    scene bg park

    "Walks in the park."

    "I am no longer who I once was."

## SKIP POINT
    $ renpy.stop_skipping()

    "But I can't tell if I am who I wanted to be."
    "I can't tell if she's who she wanted to be either."

    "Today,"
    "as we stared at the clouds"
    "she asked me..."

    scene bg sky

    h "Hey, Yu...?"

    y "Mhm?"

    h "Would you want to go to the Sumigawa Fireworks Festival with me...?"

    "END OF CHAPTER 2."

## SKIP POINT
    $ renpy.stop_skipping()

    $ renpy.movie_cutscene("videos/owwp_credits.webm", delay=None, loops=0, stop_music=False)

    stop music
    stop sound
    stop audio

    # This ends the game.
    return

##easter egg