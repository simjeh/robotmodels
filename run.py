import os
import sys
modelname=sys.argv[1]
if sys.argv[2] == None:
    xyzres = "0.06"
else: 
    xyzres = sys.argv[2]

os.system("openrave.py --database kinematicreachability --numthreads=12 --robot=rsc/"+modelname+".xml --xyzdelta="+xyzres)

