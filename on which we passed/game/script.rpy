# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Izumi")

define y = Character("Yu")

define h = Character("Hitomi")

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
    "If I could have stopped it."

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

    $ renpy.movie_cutscene("videos/owwp_op.webm", delay=None, loops=0, stop_music=False)

## SKIP POINT
    $ renpy.stop_skipping()

label encounter:

    scene bg konbi

##play shop sound of japanese convenience store or checkout

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

## show hitomi looking up street smiling

    show hitomi smilingupstreet at right

    "A straggler from the group walks up, coming to a halt just beside me."

    "It's a girl."

    "Her face is softened by the shadows of the trees overhead."

##hitomi smiling-talking-up-street
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

    show hitomi smilingeyesclosed

    g "You can just ignore them."

##hitomi smiling-talking-to-yu (mouth open)

    g "I'm-"

##hitomi shock

    "As she turns to me, the smile drops from her face."
    "It's as though she has seen a ghost."

## SKIP POINT
    $ renpy.stop_skipping()

    $ renpy.movie_cutscene("videos/enc.webm", delay=None, loops=0, stop_music=False)

    y "Are you alright...?"

##hitomi shockedtalking

    g "Yu...?"
    g "Yu Sato?"

    "Why does she know my name?"

    g "Your name is Yu, isn't it...?"

    y "Yes..."

    g "Oh my god!"

    h "It's me! Hitomi!"

    show hitomi smilingeyesclosed
    h "Hitomi Yoshinaga, from junior high school!"

    y "Oh..."
    y "Yeah. I remember you."

    "I'm more surprised that she remembers me."

    y "Nice to see you again."

    h "You too!"
    show hitomi smilingeyesclosed
    h "It's been too long!"

## SKIP POINT
    $ renpy.stop_skipping()

    "Hitomi turns to look at the group of girls, who are now farther up the street."
    "Their voices echo by, dissipating just beyond where Hitomi and I stand."

    h "I should go."
    show hitomi smilingeyesclosed
    h "They're going to leave me behind."

    "She laughs as she says it, but her final giggle reveals the truth as it fades into a quiet sigh."

    "Hitomi turns back to me."

##hitomi nervous
    h "Hey..."
##hitomi nervouslookingaside...
    h "We-"
##hitomi excited
    h "We should hang out soon!"
##hitomisoftsmiletalking
    h "It would be nice to catch up."
##hitomi smiling quiet
    "Her eyes soften with her smile."
    "She looks deep into my eyes, like she's trying to figure out what I am going to say next..."

    y "Well, I don't really..."

    hitomi smilingeyesclosed
    h "I know! Let's swap numbers!"

    y "..."
    y "Okay..."
    y "Sure."

##hitomi hand out
    "She stands there beckoning as I dig my phone out from my pocket."
    "I place it in the palm of her hand, and she smiles as she switches between the screens."

    "She punches in the numbers, and flips her phone closed with a look of accomplishment."

    "She holds my phone back out to me, and puts hers away simultaneously."

    "As I take it from her hand, she jogs off towards her friends."

    "Hesitating slightly, she turns back."

## SKIP POINT
    $ renpy.stop_skipping()

    "The sun envelops her under a blanket of white and red hues."
    "Her shadow reaches out, joining with mine."
    "Everything that is the person who calls herself Hitomi Yoshinaga, stands just before me."

    "A smile forms across her face."

    h "See you soon!"

    "She takes off and rejoins with the group."

    "As they round a corner in the distance, I look back down at my phone."

    "The contact name reads..."

    "Hitomi <3"

label texting:

    scene bg phone

    h "I’m sorry if I was too forward in asking for your number."

## SKIP POINT
    $ renpy.stop_skipping()

    h "I just thought it would be nice to see you again after so long."

    y "It's alright."
    y "I don't mind at all."

    "Back in school, Hitomi was always the sociable one."
    "She ran for class president."
    "And won of course."
    "She always answered questions in class."
    "Made friends with the new students."
    "Went to all of the dances and events."

    "I never did."

    h "Oh, thank god."
    h "I don't want to be annoying."

    y "Is that really why you wanted it?"

    h "Wanted what?"

    y "My number."

    h "Oh! Oh!"
    h "Sorry. I'm stupid."
    h "Yeah!"
    h "I just wanted to catch up!"
    h "Maybe we could get lunch!"
    h "Or something!"
    h "I don't know."
    h "Totally up to you!"

    y "I don't get out much, but I'm fine with that."

    "My stomach is turning at the thought of it."

    "Being around others..."

    "I try not to get close to people anymore."

    y "Was there something specific that you had in mind?"

    h "Do you like coffee?"

    y "I try not to drink it too much, but I like lattes."

    h "Perfect."
    h "It's settled then."
    h "How does this Saturday sound?"

    y "I'm not busy."

    "I'm never busy."

    h "Awesome!"
    h "Let's do 12:30 at Ko Coffee!"

    y "Sounds good."
    y "I'll see you there."

    h "See you!"


## SKIP POINT
    $ renpy.stop_skipping()

    "END OF CHAPTER 1"

    # This ends the game.
    return

##easter egg
