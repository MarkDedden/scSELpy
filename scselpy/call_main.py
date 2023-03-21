import sys
import os
def OnMainCall():

	with open(str(__file__)[:-12]+"version.txt", "r", encoding="utf-8") as f_vers:
	    version_inp = f_vers.read()
	sys.exit("Please only use scSELpy as import. Version: "+str(version_inp))

