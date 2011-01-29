#!/usr/bin/ env python

#Fedora Extras Center
#por Cleiton Lima <cleitonlima@fedoraproject.org>
#API do Programa.
#

from os import system

#Variables of the API

#repos
RPMFUSION_FREE = str("http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm")
RPMFUSION_NONFREE = str("http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm")

#Video
NVIDIA_OPEN = str("mesa-dri-drivers-experimental")
NVIDIA_PROP = str("akmod-nvidia")
NVIDIA_PROP_96 = str("akmod-nvidia-96xx")
NVIDIA_PROP_173 = str("akmod-nvidia-173xx")
ATI_PROP = str("kmod-fglrx xorg-x11-drv-fglrx-libs-32bit")

#Multimedia
CODEC_PROP = str("totem-gstreamer totem-xine totem-nautilus totem-mozplugin totem-pl-parser totem-youtube xine-lib-extras xine-lib-extras-freeworld gstreamer-ffmpeg ffmpeg ffmpeg-libs gstreamer-plugins-good gstreamer-plugins-bad gstreamer-plugins-ugly compat-libstdc++-33 compat-libstdc++-296 libdvdread libdvdnav lsdvd libdvbpsi")
FLASH = str("flash-plugin")
GNASH = str("gnash-plugin")
JAVA_OPEN = str("java-*openjdk java-*openjdk-plugin")

#general packages and programs
CHROMIUM = str("chromium")

#Commands
def cacher():
	#Function to make repos cache to yum.
	#Will make install/remove package faster.
	system("gnome-terminal -e beesu yum makecache")

def pkg_install (package):
	#Function to add a package to system
	#Using graphical interface
	system("gpk-install-package-name "+str(package))
	
def web_install(adress):
	#Function to install package from de web.
	#Will be util for rpmfusion repos install, for example.
	system("gnome-terminal -e beesu yum localinstall "+str(adress))
	
def pkg_remove (package):
	#Function to remove a package from the system
	#No easy graphical interface is available, using text mode, with gnome-terminal and yum.
	system("gnome-terminal -e beesu yum remove "+str(package))
	
def chromium_repo():
	#Add Chromium Repo, from Fedora People
	system("gnome-terminal -e cd /etc/yum.repos.d;beesu yum localinstall http://repos.fedorapeople.org/repos/spot/chromium/fedora-chromium.repo")