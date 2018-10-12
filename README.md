# quartus-install.py

This script installs Intel FPGA's Quartus Prime software on remote servers
which don't have a web browser or a GUI.  It makes it easy to download
across a number of servers, and to run as part of a scripted build.

Syntax:
```
usage: quartus-install.py [-h] [--download-only] [--install-only] [--prune]
                          version target device [device ...]

Download and install Quartus.

positional arguments:
  version          Quartus version, eg 18.0pro, 17.1lite, 16.1std
  target           Directory to install Quartus in
  device           Device to download/install in Quartus, eg s5 (Stratix 5),
                   a10 (Arria 10), m2 (MAX II), c10gx (Cyclone 10GX)

optional arguments:
  -h, --help       show this help message and exit
  --download-only  Only download, don't install
  --install-only   Only install, don't download
  --prune          Delete install files when finished
```

Please note that installing Quartus implies acceptance of [Intel FPGA's
EULA](http://fpgasoftware.intel.com/eula/) for the appropriate version(s)
you download.

Since it's necessary to extract the URLs manaully from the Intel website,
only a limited set of Quartus versions are supported.  Patches welcome!


Theo Markettos
github+atm26 at cl.cam.ac.uk
