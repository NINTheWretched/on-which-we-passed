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

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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

    ##change the scene to a train station, then the ground.

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

    scene bg yusroom

    show izumi doorway2 at right

    play sound "audio/computer_hum.mp3" loop

    y "I love you too."

    stop sound

    scene bg on which we passed

    play sound "passing_car.mp3"

    " "

    scene bg konbini

    "I take my sandwich from the counter, bowing before I walk away."

    "My feet remain just under my body."

    scene bg lensflare

    play music "audio/but_i_saw_a_piercing_light_last_night.mp3" loop

    "As I open the door, a group of girls runs past."

    "The glare of the sunlight hides their faces, but their figures are clear."

    "They laugh softly, making jokes between one another."

    "I step onto the sidewalk, watching as they turn back to yell something at me."

    y "What are they saying...?"

    "A straggler from the group walks up, coming to a halt just beside me."

    show hitomi lookupstreettst:
        xalign 0.75
        yalign -0.50

    g "Sorry about that."
    g "You can just ignore them."

    y "I'm not even sure what they-"

    "The girl's face drops from a smile to utter shock."

    y "Are you alright...?"

    g "Yu...?"
    g "Yu Sato?"

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

    "She laughs as she says it, her final giggle letting out into a quiet sigh."

    "Hitomi turns back to me."
    # This ends the game.

    return

##easter egg
