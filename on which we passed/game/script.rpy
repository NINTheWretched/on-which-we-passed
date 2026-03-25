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

label chapter2start:

    stop music

    stop sound

    stop audio

## SKIP POINT
    $ renpy.stop_skipping()

    scene bg preview

    "The incessant hum of people speaking around me rises in volume with each minute."

    "Every time the entry bell rings, I turn to look."

    "It's never Hitomi."

    "Maybe she's not coming..."

    "Shit."

    "Of course she's not."

    "I wouldn't."

    "That's probably what her friends were yelling."

    "It was the plan."

    "This whole thing was a cruel prank."

    "I didn't even want to do this."

##DOOR DING SOUND

##HITOMI IS TALKING TO WORKER BY THE COUNTER

    h "Hey."

    h "I hope that I didn't make you wait too long?"
    h "It seems like you've been here a while."

    y "I have, but I chose to come here pretty early."
    y "I don't get out very much,"
    y "so I try to give myself some time to acclimate."

    h "I see."

    h "Well, I'm glad that you agreed to come out to meet with me!"

    y "I thought about what you said..."
    y "And I guess that I decided it would be nice to catch up."

    h "Woah!"
    h "There he is!"

    h "I never thought I would see my Yu Sato again!"

    "I feel..."
    "Strange."

    "Safe."

    "Like I could almost laugh too."

    "It's been a long time since I've felt this way."

    y "Sorry..."

    h "Jeez..."
    h "You apologize too much!"

    y "Yeah..."

    "A moment of silence falls between us."
    "The air fills stiffer than before Hitomi arrived."

    "Things are falling apart..."
    "Back to the way that they were."

    "Everything."
    "Always."
    "Returns."

    h "Hey..."
    h "Yu...?"

    "I'm brought back out of it."

    y "Yeah?"

    h "I'm sorry if it feels like I'm being too forward..."
    h "But, can I ask you something that might be a little personal?"

    y "Sure."

    h "What happened to you in junior high school?"

##The scene with izumi will have to be an animation so that there is no dialogue box visible on the screen
##unless I can find a way to hide it??

    scene bg izumi

    "..."

    scene bg hitomitable

    y "What...?"

## SKIP POINT
    $ renpy.stop_skipping()

    "END OF DEMO."
    "THANK YOU FOR PLAYING."

    # This ends the game.
    return

    stop music

##easter egg
