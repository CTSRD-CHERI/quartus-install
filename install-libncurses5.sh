#!/bin/sh

TARGET=$1
# share the system's ncurses files, just with our own build of the library
PREFIX=/usr

aria2c -c https://invisible-island.net/datafiles/release/ncurses.tar.gz
tar zxvf ncurses.tar.gz
cd ncurses-*
./configure --with-abi-version=5 --with-shared --prefix=$PREFIX
make -j$(nproc)
cd ..
cp ncurses-*/lib/libncurses.so* $TARGET/
