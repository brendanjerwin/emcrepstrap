#!/usr/bin/python

"""
	Loads a GTS file, runs Skeinforge to create RepRap G Code and feeds that to Axis via stdout.
"""
from Tkinter import *
from math import *
from fillet import *
from slice import *
from fill import *
from preview import *
from gRead import *
import tkMessageBox
import os
import sys

#Determine if we are running from Axis
IN_AXIS = os.environ.has_key("AXIS_PROGRESS_BAR")

def previewFile(filename):
	layers = []
	gRead(filename, layers)
	Preview(layers)

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	sourceFile = 'motor-coupling.gts'
	if len(argv) > 1:
		sourceFile = argv[1]

	filePrefix = ''
	fileExtension = ''	
	if sourceFile.endswith('.gts'):
		filePrefix = sourceFile[0:sourceFile.rindex('.gts')]
		fileExtension = '.gts'
	
	#process	
	filletChainFile(sourceFile)
	
	#read the result of processing
	gcodeFileName = filePrefix + '_fillet.gcode'
	gcodeFile = open( gcodeFileName , 'r' )
	gcodeFileText = gcodeFile.read()
	gcodeFile.close()
	
	#delete the file so we don't have junk lying around
	os.remove(gcodeFileName)
	
	#touch up the file so it works in EMC/Axis	
	#We need the values passed in to be on the P word
	gcodeFileText = gcodeFileText.replace('\nM104 S','\nM104 P')
	gcodeFileText = gcodeFileText.replace('\nM108 S','\nM108 P')
	
	#I like a little more commentary
	gcodeFileText = gcodeFileText.replace('\nM101\n','\nM101 (Turn extruder on, forward)\n')
	gcodeFileText = gcodeFileText.replace('\nM103\n','\nM103 (Turn extruder off)\n')
	gcodeFileText = gcodeFileText.replace('\nM106\n','\nM106 (Turn fan on)\n')
	gcodeFileText = gcodeFileText.replace('\nM107\n','\nM107 (Turn fan off)\n')
	
	#Remove No-Op M Codes
	gcodeFileText = gcodeFileText.replace('\nM105\n','\n')
	gcodeFileText = gcodeFileText.replace('\nM110\n','\n')
	
	#write it out to Axis
	sys.stdout.write(gcodeFileText)
	

main()