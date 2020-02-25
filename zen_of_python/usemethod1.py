import json
import random
def spinWheel():
	print ("working on wheel")
	with open('wheel.json','r') as f:
		wheel = json.loads(f.read())
		#print (wheel)
		return random.choice(wheel)

print(spinWheel()) 