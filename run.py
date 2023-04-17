import os
import sys
modelname=sys.argv[1]
os.system("openrave.py --database kinematicreachability --numthreads=12 --robot=rsc/"+modelname+".xml --xyzdelta=0.01 --output="+modelname+".txt")
