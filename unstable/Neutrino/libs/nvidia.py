#!/usr/bin/ env python
# -*- coding: utf-8 -*-

#Neutrino Project

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


#por Cleiton Lima <cleitonlima@fedoraproject.org>
#Nvidia General Driver Install

from os import chdir, path, system, environ
desktoptype = environ.get('DESKTOP_SESSION')
from api.neutrino import GBase
base = GBase()

NVIDIA_PROP = str("akmod-nvidia")
NVIDIA_PROP_96 = str("akmod-nvidia-96xx")
NVIDIA_PROP_173 = str("akmod-nvidia-173xx")
RPMFUSION_FREE = str("http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm")
RPMFUSION_NONFREE = str("http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm")

#Script para Nvidia GeForce 6, 7, 8, 9, série 200, série 300 e superiores
def install (version):
	#Check if repo RPMFusion already exists
	if path.isfile("/etc/yum.repos.d/rpmfusion-free.repo") == False:
		base.web_install(RPMFUSION_FREE, "rpmfusion-free-release-stable.noarch.rpm")
	elif path.isfile("/etc/yum.repos.d/rpmfusion-nonfree.repo") == False:
		base.web_install(RPMFUSION_NONFREE, 'rpmfusion-nonfree-release-stable.noarch.rpm')
	
	#Install Nvidia Driver
	if version == "default":
		base.pkg_install(NVIDIA_PROP)
	#Install  Nvidia GeForce FX Driver
	elif version == "173":
		base.pkg_install(NVIDIA_PROP_173)
	#Install Nvidia GeForce 2, 3, 4 e Quadro 4 Driver
	elif version == "96":
		base.pkg_install(NVIDIA_PROP_96)

NVIDIA_DESCRIPTION = str("Driver Nvidia para placas GeForce 6, 7, 8, 9, série 200, série 300 e superiores. Mais informações: http://www.nvidia.com/object/IO_18897.html")
NVIDIA_173_DESCRIPTION = str("Driver Nvidia para placas GeForce FX. Mais informações: http://www.nvidia.com/object/IO_18897.html")
NVIDIA_96_DESCRIPTION = str("Driver Nvidia para placas GeForce 2, 3, 4 e Quadro 4. Mais informações: http://www.nvidia.com/object/IO_18897.html")
