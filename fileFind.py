import os
import csv
import time
import sys
import datetime	
timeStarted = datetime.datetime.now()
started = timeStarted.strftime("%m/%d/%Y %I:%M %p")

mydir = "C:\\"
bad_words = ['old', 'trash', 'replace', 'delete', '- copy']
def find_path(MyDire):
	for root, dirs, files in os.walk(mydir):
		for filename in files:
			for bad in bad_words:
				if bad in filename.lower():
					file_path = os.path.join(root,filename)
					
					file_size = os.path.getsize(file_path)

					print ("\"" + file_path + "\"" + \
						 ",\"" + str(round(file_size/1000)) + "\"" + \
						 ",\"" + filename + "\"", file=f);
				
with open('C:\\Temp\\LAN Contents ' + timeStarted.strftime("%Y-%m-%d %I.%M %p") + '.csv', 'w', newline='', encoding='utf8') as f:
	print("\"File Path\",\"Size (KB)\",\"FileName\"", file=f)
	
	find_path(mydir)
	print("Complete")
