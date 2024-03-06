import os
import string
os.chdir('C:\pp2')
for dirpath, dirnames, filenames in os.walk('C:\pp2'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()