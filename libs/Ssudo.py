#!/usr/bin/ env python
#Neutrino Project
#por Cleiton Lima <cleitonlima@fedoraproject.org>

#This file is part of Neutrino Project.

#    Neutrino is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#    Neutrino is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Neutrino.  If not, see <http://www.gnu.org/licenses/>.

#Setup sudo in Fedora
from os import getlogin, getenv, chdir
	
line = str("\n")
user = str(getlogin())
print user
cmd = str(" ALL=(ALL) NOPASSWD:ALL")
chdir(str("/etc/"))
sudoers = open ('sudoers', 'r').readlines()
sudoers.append(line+user+cmd)
sudo = open('sudoers', 'w')
sudo.writelines(sudoers)
sudo.close