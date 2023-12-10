# Circuit Playground Express - Christmas Tree Topper

## Getting Started

1. Follow the instructions for installing CircuitPython on your Circuit Playground Express on [Install CircuitPython | Circuit Playground + CircuitPython Quickstart Guide | Adafruit Learning System](https://learn.adafruit.com/circuit-playground-express-circuitpython-5-minute-guide/update-circuitpython).

2. Copy the main folder containing main.py, boot.py, mode.txt and any .wav files used to the CIRCUITPY volume.

3. Make sure the switch on the Circuit Playground Express is set so only CircuitPython can modify the storage (switch towards the silkscreen 'Ear' icon on the Circuit Playground Express PCB)

4. Power off and power on the Circuit Playground Express.

## Changing modes.

Due to the lack of access to hardware interrupts in CircuitPython's standard library (or my ignorance) the script only checks for button presses on every loop.

Therefore, make sure to hold either button down on the Circuit Playground Express until the current animation ends to be able to switch the mode.

## Using a wav file on startup

Only certain kinds of wav files can be loaded, due to limited space in the standard CircuitPython libraries.

### scripts

### Convert mp3 or wav to compatible wav

```sh
ffmpeg -i merry-christmas-charlie-brown.wav -f wav -bitexact -acodec pcm_s16le -ac 1 -ar 22050 merrychristmascb.wav
```

- [Cannot play custom wav file · Issue #97 · adafruit/Adafruit_CircuitPython_CircuitPlayground · GitHub](https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/issues/97)

### Trim a wav file

```sh
# Get duration
ffprobe christmas.wav

# Include only audio in the timestamps.
ffmpeg -ss 00:00:00 -t 00:00:05 -i christmas.wav -c copy merry-christmas-charlie-brown.wav
```

- [How i could cut the last 7 second of my video with ffmpeg? - Super User](https://superuser.com/questions/744823/how-i-could-cut-the-last-7-second-of-my-video-with-ffmpeg)
