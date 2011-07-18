#!/usr/bin env python
# -*- coding: utf-8 -*-

#Projeto Neutrino
#Neutrino's User Interface
#Cleiton Lima <cleitonlima@fedoraproject.org>

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

from os import system, path, makedirs, getlogin, remove, listdir, getenv, getcwd, chdir
import urllib2
import zlib
from PyQt4 import QtCore
import dbus
import yum

if not path.exists("/tmp/neutrino"):
    makedirs("/tmp/neutrino")

#Variables of the API

#repos
RPMFUSION_FREE = str("http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm")
RPMFUSION_NONFREE = str("http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm")

#Video
NVIDIA_PROP = str("akmod-nvidia")
NVIDIA_PROP_96 = str("akmod-nvidia-96xx")
NVIDIA_PROP_173 = str("akmod-nvidia-173xx")
ATI_PROP = str("kmod-fglrx xorg-x11-drv-fglrx-libs")

#Multimedia
CODEC_PROP = str("totem-gstreamer totem-xine totem-nautilus totem-mozplugin totem-pl-parser totem-youtube xine-lib-extras xine-lib-extras-freeworld gstreamer-ffmpeg ffmpeg ffmpeg-libs gstreamer-plugins-good gstreamer-plugins-bad gstreamer-plugins-ugly compat-libstdc++-33 compat-libstdc++-296 libdvdread libdvdnav lsdvd libdvbpsi")
JAVA = str("http://espacoliberdade.blog.br/neutrino/packages/jre-6u24-linux-i586.rpm")

#general packages and programs
Ssudo_DESCRIPTION = str("Allow current user to execute programs and commands using 'sudo' instead of 'su'")

#Package Installation Thread
class pkg_install(QtCore.QThread):
	def __init__(self, parent = None):
		QtCore.QThread.__init__(self, parent)
		self.exiting = False
		self.package = []
	def __del__(self):
		self.exiting = True
		self.wait()
	def install(self, package):
		self.package = package
		self.start()
	def run (self):
		try:
			yb = yum.YumBase()
			for item in self.package:
				yb.install(name=item)
			yb.doConfigSetup()
			yb.doRepoSetup()
			yb.doSackSetup()
			yb.doTsSetup()
			yb.doRpmDBSetup()
			yb.resolveDeps()
			yb.processTransaction()
		except Exception, e:
			f = open("/tmp/neutrino/error.txt", "w")
			f.write('Ocorreu o seguinte erro: %s' % e)
			f.close()
			self.exiting = True

class pkg_remove(QtCore.QThread):
	def __init__(self, parent = None):
		QtCore.QThread.__init__(self, parent)
		self.exiting = False
		self.package = []
	def __del__(self):
		self.exiting = True
		self.wait
	def remove(self, package):
		self.package = package
		self.start()
	def run (self):
		try:
			yb = yum.YumBase()
			for item in self.package:
				yb.remove(name=item)
			yb.doConfigSetup()
			yb.doRepoSetup()
			yb.doSackSetup()
			yb.doTsSetup()
			yb.doRpmDBSetup()
			yb.resolveDeps()
			yb.processTransaction()
		except Exception, e:
			f = open("/tmp/neutrino/error.txt", "w")
			f.write('Ocorreu o seguinte erro: %s' % e)
			f.close()
			self.exiting = True




















































