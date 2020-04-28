#!/bin/sh

TARGET=$1
git clone https://git.code.sf.net/p/libpng/code libpng-code
cd libpng-code
git checkout libpng12
./configure
make
cp -v .libs/*.a $TARGET
cp -v .libs/*.so* $TARGET

