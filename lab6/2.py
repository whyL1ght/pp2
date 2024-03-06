import os
import string
print('Exist:', os.access('C:\pp2\lab1', os.F_OK))
print('Readable:', os.access('C:\pp2\lab1', os.R_OK))
print('Writabillity:', os.access('C:\pp2\lab1', os.W_OK))
print('Executable:', os.access('C:\pp2\lab1', os.X_OK))