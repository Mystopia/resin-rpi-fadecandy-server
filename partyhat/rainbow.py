#!/usr/bin/env python
"""
Derived from pimoroni/unicorn-hat

https://github.com/pimoroni/unicorn-hat/blob/master/examples/rainbow.py
"""
import math
import os
import time
from collections import defaultdict

# import unicornhat as unicorn


# print("""Rainbow
# Displays a beautiful rainbow across your HAT/pHAT :D
# If you're using a Unicorn HAT and only half the screen lights up,
# edit this example and  change 'unicorn.AUTO' to 'unicorn.HAT' below.
# """)

# unicorn.set_layout(unicorn.AUTO)
# unicorn.rotation(0)
# unicorn.brightness(0.5)
# width,height=unicorn.get_shape()

# Fadecandy
import opc
fadecandy_url = os.getenv('FADECANDY_URL', 'localhost:7890')
print('FADECANDY_URL:', fadecandy_url)
client = opc.Client(fadecandy_url)
print('CLIENT: ', client)

width, height = 20, 3
OFFSET = 30
VELOCITY = 0.3
SLEEP = 0.01

print("Reticulating splines")
time.sleep(.5)
print("Enabled unicorn poop module!")
time.sleep(.5)
print("Pooping rainbows...")

frame = defaultdict(defaultdict)

def main():
    i = 0.0
    step = 0
    offset = OFFSET
    while True:
            i = i + VELOCITY
            step += 1
            for y in range(height):
                    for x in range(width):
                            pixelRGB = pixel(x, y, i)
                            # draw_pixel(x, y, pixelRGB)
                            frame[x][y] = pixelRGB
            if step % 500 == 0: print("T: ", step * SLEEP)
            # unicorn.show()
            # draw_frame(frame)
            draw_frame_fadecandy(frame)
            time.sleep(SLEEP)

def pixel(x, y, i):
    offset = OFFSET
    r = 0
    g = 0
    r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
    g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
    b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
    r = max(0, min(255, r + offset))
    g = max(0, min(255, g + offset))
    b = max(0, min(255, b + offset))
    return r, g, b

def draw_pixel(x, y, value):
    r, g, b = value
    # print("PIXEL: ", (x, y, int(r), int(g), int(b)))
    # unicorn.set_pixel(x,y,int(r),int(g),int(b))

def draw_frame(frame):
    # print(frame)
    for y in range(height):
        for x in range(width):
            pixelRGB = frame[x][y]
            # print(x, y, pixelRGB)
            # unicorn.set_pixel(x, y, int(r),int(g),int(b))
    # unicorn.show()

def draw_frame_fadecandy(frame):
    pixels = [ (0,0,0) ] * height * width
    # print(frame)
    i = 0
    for y in range(height):
        for x in range(width):
            pixelRGB = frame[x][y]
            # print(x, y, pixelRGB)
            r, g, b = pixelRGB
            pixels[i] = (int(r),int(g),int(b))
            i += 1
    # print(pixels)
    client.put_pixels(pixels)

if __name__ == '__main__':
    main()
