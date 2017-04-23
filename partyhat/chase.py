#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time

numLEDs = os.getenv('NUM_LEDS', 20 * 3)
fadecandy_url = os.getenv('FADECANDY_URL', 'localhost:7890')
client = opc.Client(fadecandy_url)

while True:
	for i in range(numLEDs):
		pixels = [ (0,0,0) ] * numLEDs
		pixels[i] = (255, 255, 255)
		client.put_pixels(pixels)
		time.sleep(0.01)
