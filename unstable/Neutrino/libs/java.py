#!/usr/bin env python
# -*- coding: utf-8 -*-

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
#This script will install Oracle Java or openJDK and configure the javaplugin or de icedtea-web plugin with Firefox
#
from os import environ, chdir, symlink, system
desktoptype = environ.get('DESKTOP_SESSION')
from api.neutrino import GBase
base = GBase()


JAVA = str("http://cleitonlima.com.br/neutrino/packages/jre-6u24-linux-i586.rpm")
JAVA_OPEN = ["java-openjdk", "icedtea-web"]

def install (alternative):
	if alternative == "openjdk":
		#Install OpenJDK and Icedtea-web plugin
		base.pkg_install(JAVA_OPEN)
		
	elif alternative == "java":
		#Install Extra Fonts in repository
		base.web_install(JAVA, "jre-6u24-linux-i586.rpm")
	
		#Set our installed java as default
		system('alternatives --install /usr/bin/java java /usr/java/jre1.6.0_24/bin/java 20000')
		system('alternatives --install /usr/bin/javaws javaws /usr/java/jre1.6.0_24/bin/javaws 20000')
	
		#Create Symbolic link to Java plugin in Firefox's plugin Folder
		chdir("/usr/lib/mozilla/plugins/")
		symlink("/usr/java/jre1.6.0_24/lib/i386/libnpjp2.so", "libnpjp2.so")

OPENJDK_DESCRIPTION = str("The OpenJDK runtime environment.")
JAVA_DESCRIPTION = str("O JRE consiste no Java Virtual Machine (JVM), nas classes centrais e bibliotecas de suporte da plataforma Java. O JRE representa a parte de tempo de execução do software Java, que é tudo de que você precisa para executá-lo em um navegador da Web.")
