#!/usr/bin/env python
# encoding: utf-8
"""
Created by Brendan Erwin on 2008-05-21.
Copyright (c) 2008 Brendan Erwin. All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""

import sys
import os
import serial


class RepRapArduinoSerialSender:
	
	_verbose = False
	
	def __init__(self, verbose=False):
		self._verbose = verbose
		pass

	def writeToArduino(self, dataToWrite):
		port = "/dev/tty.usbserial-FTDOMG4X"

		if self._verbose:
				print >> sys.stdout, "Opening serial port: " + port

		ser = serial.Serial(port, 19200)

		if self._verbose:
			print >> sys.stdout, "Serial Open?: " + str(ser.isOpen())
			print >> sys.stdout, "Baud Rate: " + str(ser.baudrate)

		if self._verbose:
			print >> sys.stdout, "Writing: " + dataToWrite

		ser.write(dataToWrite)

		if self._verbose:
			print >> sys.stdout, "Closing serial port."

		ser.close()

		if self._verbose:
			print >> sys.stdout, "Serial Open?: " + str(ser.isOpen())