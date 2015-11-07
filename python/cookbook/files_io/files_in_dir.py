import os.path
# Get all regular files
names = [name for name in os.listdir('.')
    if os.path.isfile(os.path.join('.', name))]
# Get all dirs
dirnames = [name for name in os.listdir('.')
    if os.path.isdir(os.path.join('.', name))]

import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
        if fnmatch(name, '*.py')]    