import os
import sys
modelname=sys.argv[1]
os.system("openrave.py --database kinematicreachability --numtheread=12 --robot=rsc/"+modelname+".xml --xyzdelta=0.06 --output="+modelname+".txt")
