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

    i "Yu, I'm heading out."

    i "I love you..."

    y "Yeah."

    y "See you in a bit."

    "She hesitates, waiting for me to say, 'I love you.' back."

    "I never did..."

    stop sound

    ##change the scene to a train station, then the ground.

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

    # This ends the game.

    return

##easter egg
