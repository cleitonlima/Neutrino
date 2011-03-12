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
#Adobe Flash Plugin Install

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

def install():
	#Check Adobe's repositoy
	if path.isfile("/etc/yum.repos.d/adobe-linux-i386.repo") == False:
		base.webinstall("http://espacoliberdade.blog.br/neutrino/packages/adobe-release-i386-1.0-1.noarch.rpm")
	#Install Flash Plugin from repo
	base.pkg_install(FLASH)

FLASH_DESCRIPTION = str("O Adobe Flash Player é um runtime de aplicativo\n baseado em navegador entre plataformas que oferece uma exibição isenta\n de aplicativos expressivos, conteúdo e vídeos entre telas e navegadores.\n O Flash Player 10.2 fornece maravilhoso vídeo HD, renderização de gráficos mais rápidos e alto desempenho em telas móveis\n e foi criado para aproveitar as capacidades do dispositivo original -- permitindo experiências de usuário mais envolventes e avançadas.")