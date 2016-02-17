#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# student: Dmitry Makarov

import os # import of os module

# checking for current version of Python
import platform
print('Current version of Python is: ' + platform.python_version() + '\n')

''' Some suitables paths:
/usr/bin/
/usr/lib/
/etc/
/usr/local/lib/
/usr/include/
/usr/share/python/
/usr/share/man/man1/
'''

# variables:
dir_path='/usr/bin'
find_name='python'
files_number = 0
word_number = 0

#print (os.listdir('.')) # list of files and dirs in current dir

# open file for writing, create it if doesn't exist, truncate it if exists ('w+')
file_for_writing = open('output_file.txt', 'w+')

# print and write first message:
current_message = ('We found these files in dir "' + 
    dir_path +'", which names include substring "python":\n')
print(current_message)
file_for_writing.write(current_message)

# Loop for finding files with include searching word
for file_name in os.listdir(dir_path):
    if file_name.find(find_name) != -1 and os.path.isfile(dir_path + '/' + file_name):
        # print current filename on screen
        print(file_name)
        # write current filename to file
        file_for_writing.write(file_name + '\n')
        # increment number of found files
        # files_number = files_number + 1
        files_number += 1
        word_number = word_number + file_name.count(find_name)

# Print and write numbers of founding files:
current_message = '\nNumber of files is:' + str(files_number) + '. Number of words is: ' + str(word_number)
print(current_message)
file_for_writing.write(current_message)
file_for_writing.close()

input("Press Enter to read from the file...")
# Read result from output file for testing:
file_for_reading = open('output_file.txt')
print('\nRead from closed and opened for reading file:\n')
print(file_for_reading.read())
file_for_reading.close()
