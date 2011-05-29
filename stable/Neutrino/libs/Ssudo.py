#!/usr/bin/ env python
# -*- coding: utf-8 -*-

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

#Add Nouveau to BlackList
#Used by nvidia.py module
#Must be executed as root

file = open("/boot/grub/grub.conf", "r").readlines()
for position, line in enumerate(file):
	if "kernel /vmlinuz-2" in line:
		text = str(' rdblacklist=nouveau')
...             br = str('\n')
...             sline = line.split("\n")
...             nline= str(str(sline[0])+text+br)
...             file[position] = nline
open("/boot/grub/grub.conf", "w").writelines(file)


