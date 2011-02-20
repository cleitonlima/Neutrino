#!/usr/bin/ env python

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
#por Rafael Gomes <rafaelgomes@techfree.com.br>
#Chromium Browser Install
#Must be executed as root

from api.base import *
import urllib
from os import chdir, getenv, getlogin
import getpass

def repo_chromium():
	#Adding Chromium Repo
	chdir("/etc/yum.repos.d/")
	system("xterm -e beesu wget http://repos.fedorapeople.org/repos/spot/chromium/fedora-chromium.repo")

def chromium_instal():
	#Install Chromium Browser
	pkg_install("chromium")