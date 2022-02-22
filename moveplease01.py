#!/usr/bin/env python3

import shutil
import os


#force the Python program to 'start' in the home user directory
#this will allow the user to run the program from any location on the system, and our script still always start at /home/student/mycode/
os.chdir('/home/student/mycode/')

#move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location
shutil.move('raynor.obj', 'ceph_storage/')

#prompt the user for a new name for the kerrigan.obj file
xname = input('What is the new name for kerrigan.obj? ')

#rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


