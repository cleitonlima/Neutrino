#!/usr/bin/ env python

#Neutrino Project
#por Cleiton Lima <cleitonlima@fedoraproject.org>
#por Rafael Gomes <rafaelgomes@techfree.com.br>
#License: GPLv3
#
#Chromium Browser Install
#Must be executed as root

from api.base import *
import urllib
from os import chdir, getenv, getlogin
import getpass

#Adding Chromium Repo
chdir("/etc/yum.repos.d/")
system("xterm -e beesu wget http://repos.fedorapeople.org/repos/spot/chromium/fedora-chromium.repo")

#Install Chromium Browser
pkg_install("chromium")