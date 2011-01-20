#!/usr/bin env python
#Project Neutrino
#License: GPLv3
#Por Cleiton Lima
#
#This script will install extra fonts, present in the system and in others ways.
#

from api.base import *

#Install Extra Fonts in repository

pkg_install(FONTS)

#Install Chkfont

web_install(CHKFONT)

#Install Microsoft Fonts

web_install(MSTTFONT)