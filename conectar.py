#!/usr/bin/python

import os
import sys

usuario=sys.argv[1]
password=sys.argv[2]
bd=sys.argv[3]

os.system('mysql --user=' + usuario + ' --password=' + password + ' ' + bd)
