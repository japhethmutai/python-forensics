#
# p-fish : Python File System Hash Program
# Author: C. Hosmer
# July 2013
# Version 1.0
#
import logging		# Python Standard Library Logger
import time			# Python Standard Library time functions
import sys			# Python Library system specific parameters
import _pfish		# _pfish Support Function Module

if __name__=='__main__':
	PFISH_VERSION = '1.0'

	# Turn on Logging
	logging.basicConfig(filename='pFishLog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

	# Process the Command Line Arguments
	_pfish.ParseCommandLine()

	# Record the Starting Time
	startTime = time.time()

	# Record the Welcome Message
	logging.info("Welcome to p-fish version 1.0\nNew Scan Started...")
	_pfish.DisplayMessage("Welcome to p-fish..." + PFISH_VERSION)

	# Record some information regarding the system
	logging.info('System:'+sys.platform)
	logging.info('Version:'+sys.version)

	# Traverse the file system directories and hash the files
	filesProcessed = _pfish.WalkPath()

	# Record the end time and calculate the duration
	endtime = time.time()
	duration = endtime - startTime

	logging.info('Files Processed'+str(filesProcessed))
	logging.info('Elapsed Time'+str(duration)+' seconds')

	logging.info("Program Terminated Normally")

	_pfish.DisplayMessage("Program End")
