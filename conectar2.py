#!/usr/bin/python

import os
import sys


print "Dime el nombre"
usuario=raw_input()

print "Escribe la contraseña"
password=raw_input()

print "Escribe la base de datos"
bd=raw_input()


os.system('mysql --user=' + usuario + ' --password=' + password + ' ' + bd)
