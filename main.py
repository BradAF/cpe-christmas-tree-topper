""""
    Make sure to copy this code to the `code.py` file on the CircuitPlayground Express.
    It should be `main.py` in the repository so the VS Code pylinter doesn't get grouchy because it overwrites the 'code' standard library.
"""

from adafruit_circuitplayground.express import cpx as cp
import random
import time

color_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255,255,0),
    "white": (255,255,255)
}

lastLed = -1
lastColor = -1
holdTimeSeconds = 2 # Length of time in seconds after fading in, and before fading out.

def fadeIn(led,color):
    """ Fade in to a specific LED and color to maximum brightness. """
    cp.pixels[led] = color
    # Range doesn't work with floats, so need to convert as cp.pixels.brightness expects range between 0.0 and 1.0 (0-100%)
    r, g, b = color
    # Range is 0-100, but endpoint in range isn't counted so +1 to make sure it hits 100.
    for i in range(0,101,1):
        if i == 0:
            cp.pixels[led] = (0,0,0)
        else:
            cp.pixels[led] = (int(r*i/100), int(g*i/100), int(b*i/100))
    pass

def fadeOut(led):
    """ Fade out to a specific LED and color to minimum brightness then turn off - just in case. """
    r, g, b = cp.pixels[led]
    # Range is 0-100, but endpoint in range isn't counted so -1 to make sure it hits 0.
    for i in range(100, -1, -1):
        if i == 0:
            cp.pixels[led] = (0,0,0)
            # Workaround to reset all pixels on a switch change.
            cp.pixels.fill((0,0,0))
            cp.pixels.brightness = 1.0
        else:
            cp.pixels[led] = (int(r*i/100), int(g*i/100), int(b*i/100))
    pass

def fadeInAll(color):
    for i in range(0,101,1):
        cp.pixels.brightness = i/100
        cp.pixels.fill(color)

def fadeOutAll():
    for i in range(100,-1, -1):
        cp.pixels.brightness = i/100

def randomColor(color_dict):
    global lastColor
    color = random.choice(list(color_dict.values()))
    while color == lastColor:
        color = random.choice(list(color_dict.values()))
    lastColor = color
    return color

def randomLED():
    global lastLed
    # Don't need to subtract 1 from total here because the last value in range isn't included by design.
    led = random.randrange(0, len(cp.pixels))
    while led == lastLed:
        led = random.randrange(0, len(cp.pixels))
    lastLed = led
    return led

def chaseLED(color):
    for i in range(len(cp.pixels)):
        fadeIn(i-1,color)
        fadeOut(i-1)

def halfLED(colors: tuple):
    """
    Sets half the random LEDs to one color, the other half to another color.
    """
    numOfLEDs = len(cp.pixels)
    numOfLEDsInGroup = numOfLEDs // 2
    for i in range(0, numOfLEDsInGroup):
        cp.pixels[i] = colors[0]
    for i in range(numOfLEDsInGroup, numOfLEDs):
        cp.pixels[i] = colors[1]
    
    # TODO: Test if the following list slicing works on hardware as an alternative to the for loops
    # cp.pixels[0:halfNumOfLEDs] = [colors[0]] * halfNumOfLEDs
    # cp.pixels[halfNumOfLEDs:] = [colors[1]] * (numOfLEDs - halfNumOfLEDs)

def allLEDRandom(color_dict: dict):
    """
    Sets all the LEDS to a random color.
    """
    for i in range(len(cp.pixels)):
        cp.pixels[i] == randomColor(color_dict)


def initializeBoard():
    cp.red_led = True
    cp.play_file("merrychristmascb.wav")
    cp.red_led = False

def playMusic(song):
    pass

initializeBoard()

while True:
    # Get a random color defined in the dict.
    currentColor = randomColor(color_dict)
    
    # print(f"currentColor: {currentColor}")
    # print(f"brightness: {cp.pixels.brightness}")

    # If the switch is to the left, do a random LED.
    if cp.switch:
        currentLED = randomLED()
        fadeIn(currentLED,currentColor)
        time.sleep(holdTimeSeconds)
        fadeOut(currentLED)
    # If the switch is to the right, do ALL LEDs.
    else:
        fadeInAll(currentColor)
        time.sleep(holdTimeSeconds)
        fadeOutAll()