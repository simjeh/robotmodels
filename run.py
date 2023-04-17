import os
import sys
modelname=sys.argv[1]
os.system("openrave.py --database kinematicreachability --robot=rsc/"+modelname+".xml --numtheread=12 --xyzdelta=0.01 --output="+modelname+".txt")
