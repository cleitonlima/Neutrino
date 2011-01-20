#!/usr/bin/ env python

#Neutrino Project
#License: GPLv3
#Por Cleiton Lima <cleitonlima@fedoraproject.org>
#
#This module will install Gnash, opensource alternative to Adobe Flash
#

from api.base import *

pkg_install("gnash gnash-plugin")