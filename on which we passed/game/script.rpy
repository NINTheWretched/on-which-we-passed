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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg yusroom

    play sound "audio/computer_hum.mp3" loop

    # These display lines of dialogue.

    "Track fourteen ends and the album comes to a full stop."

    "I'm back here again."

    "Left with nothing but the quiet hum of my computer."

    "I'm staring into the ceiling."

    "My mind is going nowhere."
    "I am going nowhere."

    "My sister cracks the door, opening it just enough to reveal herself to me."

    show izumi doorway at right

    i "Yu, I'm heading out."
    i "I love you..."

    show izumi doorway2 at right

    y "Yeah."
    y "See you in a bit."

    "She hesitates, waiting for me to say, 'I love you.' back."
    "I never did..."

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

    stop music

    stop sound

label yuroom2:

    scene bg yusroom

    show izumi doorway2 at right

    play sound "audio/computer_hum.mp3" loop

    y "I love you too."

    stop sound

    scene bg on which we passed

    play sound "passing_car.mp3"

    " "

    stop sound

label encounter:

    scene bg konbini

    "I take my sandwich from the counter, bowing before I walk away."

## insert an "audio" clip of the sliding door sound here so that it carries into the next scene.
##play cicadas "sound" on a loop after that (possibly on a fadein.) play low because music

    play audio "audio/sliding_door.mp3" volume 1.0
    play sound "audio/cicada.mp3" fadein 1.0 volume 0.2 loop

    "The sliding doors open, spitting me out into a street with light afternoon traffic."

    scene bg lensflare

    play music "audio/but_i_saw_a_piercing_light_last_night.mp3" loop

    "A group of girls runs past."

    "The glare of the sunlight hides their faces, but their figures are clear."

    "They laugh softly, making jokes between one another."

    "I step onto the sidewalk, watching as they turn back to yell something at me."

    y "What are they saying...?"

    "A straggler from the group walks up, coming to a halt just beside me."

    "It's a girl."

    "Her face is softened by the shadows of the trees overhead."

##hitomi smiling-talking-up-street
    show hitomi lookupstreettst:
        xalign 0.75
        yalign -0.50

    g "Sorry about that."

##hitomi smiling-eyes-closed

    g "You can just ignore them."

##hitomi smiling-talking (mouth open)

    g "They-"

##hitomi shock

    "Her face drops from a smile to utter shock."

    $ renpy.movie_cutscene("videos/encounter.webm", delay=None, loops=0, stop_music=False)

    y "Are you alright...?"

##hitomi shock-talking

    g "Yu...?"
    g "Yu Sato?"

##insert a video of Yu from Hitomi's view (portrait), slow pan out.
##in the same video cut to both of them standing face to face (side), slow pan out.
##find the code to insert a video into renpy.

## change the cut length to 4 seconds for each cut, so that we hold on Yu and the two of them for longer.
##    $ renpy.movie_cutscene("videos/encounter.webm", delay=None, loops=0, stop_music=False)

    "Why does she know my name?"

    g "Your name is Yu, isn't it...?"

    y "Yes..."

    g "Oh my god!"

    h "It's me! Hitomi!"
    h "Hitomi Yoshinaga, from junior high school!"

    y "Oh..."
    y "Yeah. I remember you."

    "I'm more surprised that she remembers me."

    y "Nice to see you again."

    h "You too!"
    h "It's been too long!"

    "Hitomi turns to look at the group of girls, who are now farther up the street."
    "Their voices echo by, dissipating just beyond where Hitomi and I stand."

    h "I should go."
    h "They're going to leave me behind."

    "She laughs as she says it, but her final giggle reveals the truth as it fades into a quiet sigh."

    "Hitomi turns back to me."

    h "Hey..."
    h "We-"
    h "We should hang out soon!"
    h "It would be nice to catch up."

    "Her eyes soften with her smile."
    "She looks deep into my eyes, like she's trying to figure out what I am going to say next..."

    y "Well, I don't really..."

    h "Here! Let's swap numbers."

    y "Okay..."
    y "Sure."

    "She stands there beckoning as I dig my phone out from my pocket."
    "I place it in the palm of her hand, and she smiles as she switches between the screens."

    "She punches in the numbers, and flips her phone closed with a look of accomplishment."

    "She holds my phone back out to me, and puts hers away simultaneously."

    "As I take it from her hand, she jogs off towards her friends."

    "Hesitating slightly, she turns back."

    "The sun envelops her under a blanket of white and red hues."
    "Her shadow reaches out, joining with mine."
    "Everything that is the person who calls herself Hitomi Yoshinaga, stands just before me."

    "A smile forms across her face."

    h "See you soon!"

    "She takes off and rejoins with the group."

    "As they round a corner in the distance, I look back down at my phone."

    "The contact name reads..."

    "Hitomi <3"

    # This ends the game.
    "END OF CHAPTER 1"
    return

##easter egg
