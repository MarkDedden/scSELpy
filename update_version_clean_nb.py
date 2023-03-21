import setuptools
import os
pwd = os.path.dirname(os.path.abspath(__file__))
import shutil

def tryremove(inp):
	try:
		shutil.rmtree(inp)
	except:
		pass

tryremove(pwd+"/build/")
tryremove(pwd+"/dist/")
tryremove(pwd+"/scSELpy.egg-info/")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("scselpy/version.py", "r", encoding="utf-8") as f_vers:
    version_inp = f_vers.read().splitlines()
version_inp_ = version_inp[0].replace("\"","").split(" = ")[1]
#Everytime we run setup.py, we update the version automatically
vers1= version_inp_.split(".")[-1]

vers2 = str(int(vers1)+1)

vers3 = version_inp[0][:-1][:-len(vers1)]+vers2+"\""

f = open("scselpy/version.py", "w+")
f.write(vers3)
f.close()

f = open("scselpy/version.txt", "w+")
f.write(version_inp_[:-len(vers1)]+vers2)
f.close()




from docs import Generate_params
Generate_params.Create_parameters_html()
from docs import Prepare_tutorial
Prepare_tutorial.CleanNB()



