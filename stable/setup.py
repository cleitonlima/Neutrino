#!/usr/bin/python

from setuptools import setup, find_packages
import os
import platform

setup_info =dict(name = 'neutrino',
        version = '0.8',
        description = 'Install Extra Packages and Configure Fedora',
        author = 'Cleiton Lima',
        author_email = 'cleitonlima@fedoraproject.org',
        url = 'https://github.com/cleitonlima/Neutrino',
        license = 'GNU GPL 3',
        classifiers=[
        "Development Status :: 2 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: GNU/Linux",
        "Programming Language :: Python",
        ],
	package = 'Neutrino'
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
	('share/Neutrino/imgs', ['Neutrino/imgs/neutrino.png']),
	('share/Neutrino/imgs', ['Neutrino/imgs/uninstall.png']),
	('share/applications', ['Neutrino/neutrino.desktop.desktop']),
	('bin', ['Neutrino/neutrino']),
	('share/Neutrino', ['Neutrino/ui.py']),
	('share/Neutrino', ['Neutrino/README']),
	('share/Neutrino/libs', ['Neutrino/libs/libreoffice.py']),
	('share/Neutrino/libs', ['Neutrino/libs/dialog_ok.py']),
	('share/Neutrino/libs', ['Neutrino/libs/dialog_error.py']),
	('share/Neutrino/libs', ['Neutrino/libs/dialog.py']),
	('share/Neutrino/libs', ['Neutrino/libs/elementary.py']),
	('share/Neutrino/libs', ['Neutrino/libs/faenza.py']),
	('share/Neutrino/libs', ['Neutrino/libs/gshell_elementary.py']),
	('share/Neutrino/libs', ['Neutrino/libs/gshell_smooth.py']),
	('share/Neutrino/libs', ['Neutrino/libs/gshell_atolm.py']),
	('share/Neutrino/libs', ['Neutrino/libs/chromium.py']),
	('share/Neutrino/libs', ['Neutrino/libs/Ssudo.py']),
	('share/Neutrino/libs', ['Neutrino/libs/flash.py']),
	('share/Neutrino/libs', ['Neutrino/libs/gnash.py']),
	('share/Neutrino/libs', ['Neutrino/libs/fonts.py']),
	('share/Neutrino/libs', ['Neutrino/libs/nvidia.py']),
	('share/Neutrino/libs', ['Neutrino/libs/openjdk.py']),
	('share/Neutrino/libs', ['Neutrino/libs/java.py']),
	('share/Neutrino/libs', ['Neutrino/libs/codecs.py']),
	('share/Neutrino/libs', ['Neutrino/libs/__init__.py']),
	('share/Neutrino/libs/api', ['Neutrino/libs/api/__init__.py']),
	('share/Neutrino/libs/api', ['Neutrino/libs/api/base.py']),
    ]

setup(data_files = _data_files,
        packages = find_packages(), **setup_info)
