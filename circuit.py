import CHIP_IO.GPIO as GPIO
from time import sleep


# --- leds --- #

led_init = False

def __led_init():
    global led_init
    if not led_init:
        GPIO.setup("XIO-P0", GPIO.OUT)
        GPIO.setup("XIO-P2", GPIO.OUT)
        GPIO.setup("XIO-P4", GPIO.OUT)
        GPIO.output("XIO-P0", GPIO.LOW)
        GPIO.output("XIO-P2", GPIO.LOW)
        GPIO.output("XIO-P4", GPIO.LOW)
        led_init = True

def __led(led, state):
    # state
    if state == "off":
        state = GPIO.LOW
    elif state == "on":
        state = GPIO.HIGH
    else:
        return False
    # led
    if led == "green":
        led = "XIO-P0"
    elif led == "yellow":
        led = "XIO-P2"
    elif led == "orange":
        led = "XIO-P4"
    elif led == "all":
        __led("green", state)
        __led("yellow", state)
        __led("red", state)
        return True
    else:
        return False
    # execute
    return GPIO.output(led, state)

def led_off(led):
    __led_init()
    return __led(led, "off")

def led_on(led):
    __led_init()
    return __led(led, "on")


# --- buttons --- #

button_init = False

def __button_init():
    global button_init
    if not button_init:
        GPIO.setup("XIO-P6", GPIO.IN)
        GPIO.setup("XIO-P7", GPIO.IN)
        button_init = True

def button(button):
    __button_init()
    if button == "one":
        button = "XIO-P6"
    elif button == "two":
     button = "XIO-P7"
    else:
        return False
    return GPIO.input(button)


# --- general functions --- #

def cleanup():
    GPIO.cleanup()

def test():
    print "led test"
    for i in range(3):
        led_on("green")
        sleep(0.5)
        led_on("yellow")
        sleep(0.5)
        led_on("orange")
        sleep(0.5)
        led_off("green")
        sleep(0.5)
        led_off("yellow")
        sleep(0.5)
        led_off("orange")
        sleep(0.5)
    print "press button 1"
    while True:
        if button("one"):
            print "perfect!"
            break
    print "press button 2"
    while True:
        if button("two"):
            print "perfect!"
            break
    sleep(0.25)
    print "all tests done"

# --- main --- #

if __name__ == '__main__':
    print "test"
    test()
    print "cleanup"
    cleanup()
