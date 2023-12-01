from adafruit_circuitplayground.express import cpx as cp
import random

color_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255,255,0),
    "white": (255,255,255)
}

lastLed = -1
lastColor = -1

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
        else:
            cp.pixels[led] = (int(r*i/100), int(g*i/100), int(b*i/100))
    pass

def randomColor(color_dict):
    global lastColor
    color = random.choice(list(color_dict.values()))
    while color == lastColor:
        color = random.choice(list(color_dict.values()))
    lastColor = color
    return color

def randomLED():
    global lastLed
    led = random.randrange(0, len(cp.pixels) - 1)
    while led == lastLed:
        led = random.randrange(0, len(cp.pixels) - 1)
    lastLed = led
    return led

def initializeBoard():
    cp.red_led = True
    for i in range(len(cp.pixels)):
        fadeIn(i-1,(color_dict['white']))
        fadeOut(i-1)
    cp.red_led = False
    pass

def playMusic(song):
    pass

initializeBoard()

while True:
    currentLED = randomLED()
    currentColor = randomColor(color_dict)
    fadeIn(currentLED,currentColor)
    fadeOut(currentLED)