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
  version          Quartus version, eg 18.0pro, 17.1lite, 16.1std.
                   Supplying an invalid version will return the supported versions.
  target           Directory to install Quartus in
  device           Device to download/install in Quartus.  Supported:
                           a2    Arria II
                           a5    Arria V
                           a5gz  Arria V GZ
                           a10   Arria 10
                           c4    Cyclone IV
                           c5    Cyclone V
                           c10gx Cyclone 10 GX
                           c10lp Cyclone 10 LP
                           m2    MAX II
                           m5    MAX V
                           m10   MAX 10
                           s4    Stratix IV
                           s5    Stratix V
                           s10   Stratix 10
                           dsp   DSP Builder
                           eds   ARM EDS
                           opencl OpenCL toolkit

optional arguments:
  -h, --help       show this help message and exit
  --download-only  Only download, don't install
  --install-only   Only install, don't download
  --prune          Delete install files when finished
  --nosetup        Don't download Quartus setup frontend
  --parallel PARALLEL, -j PARALLEL
                   Number of parallel download connections
  --fix-libpng     Build and add libpng12.so binary to Quartus library dir
                   (needed for recent Ubuntu among others)
  --check-urls     Check whether the URLs in the database are fetchable
```

Example usage:
```
quartus-install.py 18.1std /opt/intelFPGA/18.1std a10 s4 s5 c4 c5 m10
```

You will also need the ['aria2'](https://aria2.github.io/) tool installed to
perform parallel downloads (since the Akamai servers have limited per-file
bandwidth, it is most efficient to download all the pieces in parallel if
you are on a high-bandwidth link).

Please note that installing Quartus implies acceptance of [Intel FPGA's
EULA](http://fpgasoftware.intel.com/eula/) for the appropriate version(s)
you download.

Since it's necessary to extract the URLs manaully from the Intel website,
only a limited set of Quartus versions are supported.  Patches welcome!


Theo Markettos
github+atm26 at cl.cam.ac.uk
