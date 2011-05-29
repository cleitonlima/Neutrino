#!/usr/bin env python
#Project Neutrino
#Por Cleiton Lima <cleitonlima@fedoraproject.org>

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

#
#This script will install Oracle Java and configure the javaplugin with Firefox
#
from os import environ, chdir, symlink, system
desktoptype = environ.get('DESKTOP_SESSION')
if "gnome" in desktoptype :
	from api.base import GBase
	base = GBase()
elif "kde" in desktoptype:
	from api.base import KBase
	base = KBase()
else:
	pass

JAVA = str("http://cleitonlima.com.br/neutrino/packages/jre-6u25-linux-i586.rpm")

#Install Extra Fonts in repository
print "Baixando o Pacote jre-6u25-linux-i586.rpm. Aguarde."
base.web_install_alt(JAVA, "jre-6u25-linux-i586.rpm")
	
#Set our installed java as default
system('alternatives --install /usr/bin/java java /usr/java/jre1.6.0_25/bin/java 20000')
system('alternatives --install /usr/bin/javaws javaws /usr/java/jre1.6.0_25/bin/javaws 20000')
	
#Create Symbolic link to Java plugin in Firefox's plugin Folder
chdir("/usr/lib/mozilla/plugins/")
symlink("/usr/java/jre1.6.0_25/lib/i386/libnpjp2.so", "libnpjp2.so")