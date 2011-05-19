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
#Installation of Codecs to execute mp3, wmv, avi and other formats

from os import chdir, path, system, environ
desktoptype = environ.get('DESKTOP_SESSION')
print desktoptype
if "gnome" in desktoptype :
	from api.base import GBase
	base = GBase()
elif "kde" in desktoptype:
	from api.base import KBase
	base = KBase()
else:
	pass

CODEC_PROP = str("totem-gstreamer totem-xine totem-nautilus totem-mozplugin totem-pl-parser totem-youtube xine-lib-extras xine-lib-extras-freeworld gstreamer-ffmpeg ffmpeg ffmpeg-libs gstreamer-plugins-good gstreamer-plugins-bad gstreamer-plugins-ugly compat-libstdc++-33 compat-libstdc++-296 libdvdread libdvdnav lsdvd libdvbpsi")
RPMFUSION_FREE = str("http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm")
RPMFUSION_NONFREE = str("http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm")

def install():
	#Check if repo RPMFusion already exists
	if path.isfile("/etc/yum.repos.d/rpmfusion-free.repo") == False:
		base.web_install(RPMFUSION_FREE, "rpmfusion-free-release-stable.noarch.rpm")
	elif path.isfile("/etc/yum.repos.d/rpmfusion-nonfree.repo") == False:
		base.web_install(RPMFUSION_NONFREE, "rpmfusion-nonfree-release-stable.noarch.rpm")
	
	#Install Flash Plugin from repo
	base.pkg_install(CODEC_PROP)

CODEC_DESCRIPTION = str("Todos os codecs necessários para tocar arquivos mp3, avi e outros formatos.")