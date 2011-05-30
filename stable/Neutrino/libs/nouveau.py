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

#Used by nvidia.py module
#Must be executed as root

from os import system, remove


file = open("/boot/grub/grub.conf", "r").readlines()

for position, line in enumerate(file):
	if "kernel /vmlinuz-2" in line:
		text = str(' rdblacklist=nouveau')
		br = str('\n')
		sline = line.split("\n")
		system("xrandr | grep '*' | cut -d' ' -f4 > /tmp/neutrino/resolution.txt")
		reso = open("/tmp/neutrino/resolution.txt", 'r').read()
		resolution = reso.split("\n")
		if resolution[0] == "800x600":
			vga = str(" vga=0x314")
		elif resolution[0] == "1024x768":
			vga = str(" vga=0x317")
		elif resolution[0] == "1152x864":
			vga = str(" vga=0x163")
		elif resolution[0] == "1280x1024":
			vga = str(" vga=0x31A")
		elif resolution[0] == "1600x1200":
			vga = str(" vga=0x31E")
		else:
			vga = str(" vga=0x317")
		nline = str(str(sline[0])+text+vga+br)
		print nline
		file[position] = nline
		
open("/boot/grub/grub.conf", "w").writelines(file)
remove("/tmp/neutrino/resolution.txt")