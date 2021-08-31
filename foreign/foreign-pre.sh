#!/bin/sh

DISTRO=$(lsb_release -is)
RELEASE=$(lsb_release -cs)

if [ "${DISTRO}" != "Ubuntu" ] ; then
  echo "Error: Patching Quartus to run on a non-x86 machine only currently supported on Ubuntu"
  exit
elif [ "${RELEASE}" != "focal" ] ; then
  echo "Warning: Patching Quartus to run on a non-x86 machine only tested on Ubuntu 20.04 arm64 - continuing anyway"
fi

ARCH=$(dpkg --print-architecture)

# enable amd64 and i386 packages
sudo dpkg --add-architecture amd64
sudo dpkg --add-architecture i386

# x86 packages live on a different ubuntu server from arm64 packages
# so make separate sources.list files for each
sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.d/x86.list
sudo sed -i "s/deb http/deb [arch=$ARCH] http/g" /etc/apt/sources.list
sudo sed -i "s/deb .*http/deb [arch=amd64,i386] http/g" /etc/apt/sources.list.d/x86.list
sudo sed -i "s|ports.ubuntu.com/ubuntu-ports|archive.ubuntu.com/ubuntu|g" /etc/apt/sources.list.d/x86.list

# update the package database
sudo apt-get update

# install necessary amd64 libraries for Quartus
sudo apt-get -y install libc6:amd64 zlib1g:amd64 libncurses5:amd64 \
  libgtk2.0-0:amd64 libsm6:amd64 
# for Qsys (Platform Designer)
sudo apt-get -y install libstdc++6:amd64 libxtst6:amd64
# for Modelsim Intel Starter Edition (32 bit)
sudo apt-get -y install libc6:i386 libxext6:i386 libxft2:i386

# install QEMU user emulation
sudo apt-get update
sudo apt-get -y install qemu-user

#sudo apt -y install 
#gcc-multilib g++-multilib lib32z1 lib32stdc++6 lib32gcc1 libstdc++6:i386
#expat:i386 fontconfig:i386 libfreetype6:i386 libexpat1:i386 libc6:i386
#libgtk-3-0:i386 libcanberra0:i386 libpng12-0:i386 libice6:i386 libsm6:i386
#libncurses5:i386 zlib1g:i386 libx11-6:i386 libxau6:i386 libxdmcp6:i386
#libxext6:i386 libxft2:i386 libxrender1:i386 libsm6:i386 libfontconfig1:i386
#libxi6:i386 libxtst6:i386 libxt6:i386 libxtst6:i386 default-jre bzip2:i386
#libgtk2.0-0:i386
