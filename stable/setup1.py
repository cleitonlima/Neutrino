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

from distutils.core import setup 

_data_files = [
        ('share/Neutrino/imgs', ['imgs/applications-accessories.png']),
        ('share/Neutrino/imgs', ['Neutrino/imgs/applications-graphics.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-games.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-internet.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-office.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-other.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-system.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-multimedia.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-install.png']),
	('share/applications', ['Neutrino/neutrino.desktop']),
	
    ]

setup (name = 'Neutrino', 
          description = "Install Extra Packages in Fedora", 
          author = "Cleiton Lima", 
          author_email = "cleitonlima@fedoraproject.org", 
          version = '1.0.0', 
	  license = 'GPLv3',
	  url = 'https://github.com/cleitonlima/Neutrino',
	  packages = ['Neutrino'],
          package_dir = {'Neutrino' : 'Neutrino'},
	  data_files = _data_files
	  )
