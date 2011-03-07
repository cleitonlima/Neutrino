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

#API do Programa.

from os import system, path, makedirs, getlogin
from PyQt4 import QtCore, QtGui

if not path.exists("/tmp/neutrino"):
    makedirs("/tmp/neutrino")

#Variables of the API

#repos
RPMFUSION_FREE = str("http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm")
RPMFUSION_NONFREE = str("http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm")

#Video
NVIDIA_OPEN = str("mesa-dri-drivers-experimental")
NVIDIA_PROP = str("akmod-nvidia")
NVIDIA_PROP_96 = str("akmod-nvidia-96xx")
NVIDIA_PROP_173 = str("akmod-nvidia-173xx")
ATI_PROP = str("kmod-fglrx xorg-x11-drv-fglrx-libs")

#Multimedia
CODEC_PROP = str("totem-gstreamer totem-xine totem-nautilus totem-mozplugin totem-pl-parser totem-youtube xine-lib-extras xine-lib-extras-freeworld gstreamer-ffmpeg ffmpeg ffmpeg-libs gstreamer-plugins-good gstreamer-plugins-bad gstreamer-plugins-ugly compat-libstdc++-33 compat-libstdc++-296 libdvdread libdvdnav lsdvd libdvbpsi")
FLASH = str("flash-plugin")
GNASH = str("gnash-plugin")
JAVA_OPEN = str("java-1.6.0-openjdk java-1.6.0-openjdk-plugin")

#general packages and programs
FONTS = str("aajohan-* adf-* aldusleaf-* allgeyer-* apa-new-* apanov-* artwiz-* beteckna-* bitstream-* bpg-* dejavu-* dustin-* ecolier-* gargi-* gdouros-* gfs-* gnu-free-* google-droid-* hartke-aurulent-* mgopen-* mona-* oflb-* yanone-* ghostscript-fonts xorg-x11-fonts* liberation-*")
CHKFONT = str("http://espacoliberdade.blog.br/neutrino/packages/chkfontpath-1.10.1-2.fc13.i686.rpm")
MSTTFONT = str("http://espacoliberdade.blog.br/neutrino/packages/msttcorefonts-2.0-2.noarch.rpm")
Ssudo_DESCRIPTION = str("Allow current user to execute programs and commands using 'sudo' instead of 'su'")

#GTK Module

class GBase ():
	def cacher():
		#Function to make repos cache to yum.
		#Will make install/remove package faster.
		system("xterm -e beesu yum makecache")

	def pkg_install (GBase, package):
		#Function to add a package to system
		#Using graphical interface
		system("gpk-install-package-name "+str(package))
	
	def web_install(GBase, adress):
		#Function to install package from de web.
		#Will be util for rpmfusion repos install, for example.
		system("cd /tmp/neutrino;xterm -e wget "+str(adress))
		system("gpk-install-file /tmp/neutrino/*.rpm")
		system("rm -rf /tmp/neutrino/*")
	
	def pkg_remove (GBase, package):
		#Function to remove a package from the system
		#No easy graphical interface is available, using text mode, with gnome-terminal and yum.
		system("xterm -e beesu yum remove "+str(package))

#Qt4/KDE Module

class KBase ():
	def cacher():
		#Function to make repos cache to yum.
		#Will make install/remove package faster.
		system("xterm -e beesu yum makecache")

	def pkg_install (KBase, package):
		#Function to add a package to system
		#Using graphical interface
		system("kpackagekit --install-package-name "+str(package))
	
	def web_install(KBase, adress):
		#Function to install package from de web.
		#Will be util for rpmfusion repos install, for example.
		system("cd /tmp/neutrino;xterm -e wget "+str(adress))
		system("kpackagekit --install-local-file /tmp/neutrino/*.rpm")
		system("rm -rf /tmp/neutrino/*")
	
	def pkg_remove (KBase, package):
		#Function to remove a package from the system
		#No easy graphical interface is available, using text mode, with gnome-terminal and yum.
		system("xterm -e beesu yum remove "+str(package))