#!/usr/bin/python

from setuptools import setup, find_packages
import os
import platform

setup_info =dict(name = 'neutrino',
        version = '0.5',
        description = 'Install Extra Packages and Configure Fedora',
        author = 'Cleiton Lima',
        author_email = 'cleitonlima@fedoraproject.org',
        url = 'https://github.com/cleitonlima/Neutrino',
        license = 'GNU GPL 3',
        classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: GNU/Linux",
        "Programming Language :: Python",
        ],
	package = 'Neutrino',
	#package_data = {'Neutrino':['*.py', 'libs/*/*']}
	)
	
_data_files = [
        ('share/Neutrino/imgs', ['Neutrino/imgs/applications-accessories.png']),
        ('share/Neutrino/imgs', ['Neutrino/imgs/applications-graphics.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-games.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-internet.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-office.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-other.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-system.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/applications-multimedia.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/install.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/uninstall.png']),
	('share/applications', ['Neutrino/neutrino.desktop']),
	('bin', ['Neutrino/neutrino']),
	('share/Neutrino', ['Neutrino/ui.py']),
	('share/Neutrino', ['Neutrino/README']),
	('share/Neutrino/libs', ['Neutrino/libs/chromium.py']),
	('share/Neutrino/libs', ['Neutrino/libs/Ssudo.py']),
	('share/Neutrino/libs', ['Neutrino/libs/flash.py']),
	('share/Neutrino/libs', ['Neutrino/libs/gnash.py']),
	('share/Neutrino/libs', ['Neutrino/libs/fonts.py']),
	('share/Neutrino/libs', ['Neutrino/libs/nvidia.py']),
	('share/Neutrino/libs', ['Neutrino/libs/openjdk.py']),
	('share/Neutrino/libs', ['Neutrino/libs/codecs.py']),
	('share/Neutrino/libs', ['Neutrino/libs/__init__.py']),
	('share/Neutrino/libs/api', ['Neutrino/libs/api/__init__.py']),
	('share/Neutrino/libs/api', ['Neutrino/libs/api/base.py']),
    ]

setup(data_files = _data_files,
        packages = find_packages(), **setup_info)
