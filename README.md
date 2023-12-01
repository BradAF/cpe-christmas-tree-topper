# Circuit Playground Express - Christmas Tree Topper

## Getting Started

Copy the contents of main.py to code.py on CIRCUITPY volume.

- CircuitPython boot loader must already be loaded

## Using a wav file

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
