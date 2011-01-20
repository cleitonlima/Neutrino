#!/usr/bin/ env python
#Neutrino Project
#Setup sudo in Fedora
#Cleiton Lima
#License: GPLv3

from os import getlogin, getenv, chdir

line = str("\n")
user = str(getlogin())
print user
cmd = str(" ALL=(ALL) NOPASSWD:ALL")
chdir(str("/home/cleiton/"))
sudoers = open ('sudoers', 'r').readlines()
sudoers.append(line+user+cmd)
sudo = open('sudoers', 'w')
sudo.writelines(sudoers)
sudo.close