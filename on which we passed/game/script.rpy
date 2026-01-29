# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Izumi")

define y = Character("Yu")

define h = Character("Hitomi")


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

    play sound "passing_car.mp3"

    scene bg on which we passed

    " "

    # This ends the game.

    return

##easter egg
