#!/usr/bin/python
import subprocess
import os
import sys
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import warnings
warnings.filterwarnings("ignore")
from difflib import SequenceMatcher

PATH = #SET PATH TO MUSIC FOLDER
FILES = os.listdir(PATH)
query = ' '.join(sys.argv[1:])
choicemade = False
index = -1
flag = True
fileList = process.extract(query, FILES, limit=8)

while flag:
	if choicemade:
		flag = False
		song = fileList[index][0]
		song2 = ""
		for i in song:
			if i in '`~!@#$%^&*()_-+=:;,\\\' ':
				i = '\\'+i
			song2 += i
		subprocess.call(["mpg123 "+PATH+song2], shell=True)

	else:
		for i in range(len(fileList)):
			if fileList[i][0].endswith('.mp3'):
				print (str(i) +": "+ str(fileList[i]))
		index = input("\nEnter your choice: ")
		choicemade = True
