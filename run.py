import os
import sys
modelname=sys.argv[1]
if len(sys.argv) == 2:
    xyzres = "0.06"
else: 
    xyzres = sys.argv[2]

os.system("openrave.py --database kinematicreachability --numthreads=12 --robot=rsc/"+modelname+".xml --xyzdelta="+xyzres)

