import os
import shutil

"""this code copy entire folder from ../.openrave/ to .openrave/"""
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try : 
                shutil.copytree(s, d, symlinks, ignore)
                print(d)
            except : pass
        else:
            shutil.copy2(s, d)
            print(d)

copytree('../.openrave/', '.openrave/')
print("done")
