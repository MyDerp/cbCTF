#!/usr/bin/python
from PIL import Image
from pyzbar.pyzbar import decode
import requests
while 1:
	data = decode(Image.open('pic.jpg'))
	ncode = data[0]
	# Receives the first item in the list which happens to be another list
	code = ncode[0]
	# Receives decoded data (Other data exists you just have to print the list to choose)
	print(code)
	# Preference, remove it if you dont wanna see whats going on
	important = code['start_of_file':'end_of_file']
	# Example: important = code[30:40] -->
	# --> https://example.com/directory/342545445.jpg
	# --> 342545445
	if  code.find("initial_flag") != -1: #Example: "animanCTF"
		print(code)
		break
	url = 'https://example.com/directory/' + important + '.extension'
	# Example: 'https://example/directory/342545445.jpg'
	r = requests.get(url, allow_redirects=True)
	open('pic.jpg', 'wb').write(r.content)

