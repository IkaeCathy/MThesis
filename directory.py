import os
import re

#used for iterating through several files in diferent subdirectories...
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for name in files:
            r.append(os.path.join(root, name))
    return r


