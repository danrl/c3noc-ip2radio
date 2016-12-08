import subprocess
from time import sleep
import circuit as c
import signal

def clean_exit():
    print "clean exit"
    c.cleanup()
    exit(0)

signal.signal(signal.SIGINT, clean_exit)
signal.signal(signal.SIGTERM, clean_exit)

stations = [
    'http://stream2.friskyradio.com:8000/frisky_mp3_hi',
    'http://ice1.somafm.com/defcon-128-mp3'
]

proc = False

def play(station):
    global stations
    global proc
    c.led_off("all")
    c.led_on("orange")
    if proc:
        proc.terminate()
        sleep(3)
    proc = subprocess.Popen([
        'mplayer',
        '-cache', '512',
        '-cache-min', '5',
        stations[station]
    ])
    # wait for stream to cache
    for _ in range(5*2):
        c.led_off("orange")
        sleep(0.25)
        c.led_on("orange")
        sleep(0.25)
    c.led_off("orange")

play(0)
c.led_on("green")

while True:
    if c.button("one"):
      play(0)
      c.led_on("green")
    elif c.button("two"):
      play(1)
      c.led_on("yellow")
    sleep(0.5)

c.cleanup()
