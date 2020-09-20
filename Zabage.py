#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/ASCII-text-banners

import sys,os,platform

args = sys.argv

##### colors
colors = True	# output colored c:
machine = sys.platform 		# detecting the os
checkPlatform = platform.platform()	# get current version of os
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
	colors = False 	# Mac and Windows shouldn't display colors :c
if checkPlatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
	color = True	# coooolorssss \o/
	os.system('')	# Enables the ANSI -> standard encoding that reads that colors
if not colors:
	BGreen = BYellow = BPurple = BCyan = Yellow = Green = Red = Blue = On_Black = ''
else:
	BGreen = "\033[1;32m"     # Bold Green
	BYellow = "\033[1;33m"    # Bold Yellow
	BPurple = "\033[1;35m"    # Bold Purple
	BCyan = "\033[1;36m"      # Bold Cyan
	Yellow = "\033[0;33m"     # Yellow
	Green = "\033[0;32m"      # Green
	Red = "\033[0;31m"      # Red
	Blue = "\033[0;34m"     # Blue

	# Background
	On_Black="\033[40m"       # Black Background


##### logo
if len(args) == 1:		### Made with figlet or toilet
	print('''
		{On_Black}{BCyan}
		\t  _____     _
		\t |__  /__ _| |__   __ _  __ _  ___
		\t   / // _` | '_ \ / _` |/ _` |/ _ \\
		\t  / /| (_| | |_) | (_| | (_| |  __/
		\t /____\__,_|_.__/ \__,_|\__, |\___|
		\t                        |___/
		{BYellow} # Zanotti's banner generator{Green}
		https://github.com/LeonardoZanotti/ASCII-text-banners

To generate your banner type:
\t
{BGreen}$ python3 zabage.py text to banner            
		'''.format(BCyan=BCyan,BGreen=BGreen,Green=Green,BYellow=BYellow,On_Black=On_Black))                                   

	sys.exit()
else:
	args[0] = ''
	i = 0
	text = ''
	for arg in args:
		text += args[i]+" "
		i = i + 1

	os.system("figlet {text}".format(text=text))
	os.system("toilet {text}".format(text=text))
	for font in os.listdir('/usr/share/figlet'):
		if (font.split('.')[1] != 'flc'):
			os.system("figlet -f {font} {text}".format(font=font,text=text))