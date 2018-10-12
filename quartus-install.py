#!/usr/bin/env python
#-
# SPDX-License-Identifier: BSD-2-Clause
#
# Copyright (c) 2018 A. Theodore Markettos
# All rights reserved.
#
# This software was developed by SRI International and the University of
# Cambridge Computer Laboratory (Department of Computer Science and
# Technology) under DARPA contract HR0011-18-C-0016 ("ECATS"), as part of the
# DARPA SSITH research programme.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

"""
Download and install Quartus Prime software on remote servers that don't have a web browser or GUI
"""

quartus_url_171std = {
    'setup' : 'http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/QuartusSetup-17.1.0.590-linux.run',
    'modelsim' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/ModelSimSetup-17.1.0.590-linux.run",
    'a2' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arria-17.1.0.590.qdz",
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arria10_part1-17.1.0.590.qdz",
    'a10_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arria10_part2-17.1.0.590.qdz",
    'a10_part3' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arria10_part3-17.1.0.590.qdz",
    's4' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/stratixiv-17.1.0.590.qdz",
    's5' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/stratixv-17.1.0.590.qdz",
    'c10lp' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arriav-17.1.0.590.qdz",
    'c5' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/stratixiv-17.1.0.590.qdz",
    'c4' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/cyclone-17.1.0.590.qdz",
    'a5' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arriav-17.1.0.590.qdz",
    'a5gz' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arriav-17.1.0.590.qdz",
    'm5' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arriav-17.1.0.590.qdz",
    'm10' : "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/arriav-17.1.0.590.qdz",
    'update1' : "http://download.altera.com/akdlm/software/acdsinst/17.1std.1/593/update/QuartusSetup-17.1.1.593-linux.run"
}

quartus_url_171pro = {
    'setup' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/QuartusProSetup-17.1.0.240-linux.run",
    'modelsim' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/QuartusProSetup-17.1.0.240-linux.run",
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/arria10_part1-17.1.0.240.qdz",
    'a10_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/arria10_part2-17.1.0.240.qdz",
    'a10_part3' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/arria10_part3-17.1.0.240.qdz",
    'c10gx_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/cyclone10gx_part1-17.1.0.240.qdz",
    'c10gx_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/cyclone10gx_part2-17.1.0.240.qdz",
    's10_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/cyclone10gx_part1-17.1.0.240.qdz",
    's10_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/cyclone10gx_part1-17.1.0.240.qdz",
    's10_part3' : "http://download.altera.com/akdlm/software/acdsinst/17.1/240/ib_installers/cyclone10gx_part1-17.1.0.240.qdz",
    'update1' : "http://download.altera.com/akdlm/software/acdsinst/17.1.2/304/update/QuartusProSetup-17.1.2.304-linux.run"
}

quartus_url_180pro = {
    'setup' : 'http://download.altera.com/akdlm/software/acdsinst/18.0/219/ib_installers/QuartusProSetup-18.0.0.219-linux.run',
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/18.0/219/ib_installers/arria10-18.0.0.219.qdz",
    'c10gx_part1' : "http://download.altera.com/akdlm/software/acdsinst/18.0/219/ib_installers/cyclone10gx-18.0.0.219.qdz",
    's10_part1' : "http://download.altera.com/akdlm/software/acdsinst/18.0/219/ib_installers/stratix10-18.0.0.219.qdz",
    'update1': "http://download.altera.com/akdlm/software/acdsinst/18.0.1/261/update/QuartusProSetup-18.0.1.261-linux.run"
}


quartus_url_180std = {
    'setup' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/QuartusSetup-18.0.0.614-linux.run",
    'a2' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/arria-18.0.0.614.qdz",
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/arria10_part1-18.0.0.614.qdz",
    'a10_part2' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/arria10_part2-18.0.0.614.qdz",
    'a10_part3' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/arria10_part3-18.0.0.614.qdz",
    'a5': "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/arriav-18.0.0.614.qdz",
    'a5gz' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/arriavgz-18.0.0.614.qdz",
    'c4': "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/cyclone-18.0.0.614.qdz",
    'c10lp' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/cyclone10lp-18.0.0.614.qdz",
    'c5' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/cyclonev-18.0.0.614.qdz",
    'm5': "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/max-18.0.0.614.qdz",
    'm10' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/max10-18.0.0.614.qdz",
    's4' : "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/stratixiv-18.0.0.614.qdz",
    's5': "http://download.altera.com/akdlm/software/acdsinst/18.0std/614/ib_installers/stratixv-18.0.0.614.qdz"
}

quartus_url_170pro = {
    'setup' : "http://download.altera.com/akdlm/software/acdsinst/17.0/290/ib_installers/QuartusProSetup-17.0.0.290-linux.run",
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.0/290/ib_installers/arria10_part1-17.0.0.290.qdz",
    'a10_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.0/290/ib_installers/arria10_part2-17.0.0.290.qdz",
    'a10_part3' : "http://download.altera.com/akdlm/software/acdsinst/17.0/290/ib_installers/arria10_part3-17.0.0.290.qdz",
    'c10gx_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.0/290/ib_installers/cyclone10gx_part1-17.0.0.290.qdz",
    'c10gx_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.0/290/ib_installers/cyclone10gx_part2-17.0.0.290.qdz"
}

quartus_url_170std = {
    'setup' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/QuartusSetup-17.0.0.595-linux.run",
    'a2' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/arria-17.0.0.595.qdz",
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/arria10_part1-17.0.0.595.qdz",
    'a10_part2' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/arria10_part2-17.0.0.595.qdz",
    'a10_part3' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/arria10_part3-17.0.0.595.qdz",
    'a5' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/arriav-17.0.0.595.qdz",
    'c4' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/cyclone-17.0.0.595.qdz",
    'c10lp' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/cyclone10lp-17.0.0.595.qdz",
    'c5' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/cyclonev-17.0.0.595.qdz",
    'm5' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/max-17.0.0.595.qdz",
    'm10' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/max10-17.0.0.595.qdz",
    's4' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/stratixiv-17.0.0.595.qdz",
    's5' : "http://download.altera.com/akdlm/software/acdsinst/17.0std/595/ib_installers/stratixv-17.0.0.595.qdz",
}

quartus_url_161std = {
    'setup' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/QuartusSetup-16.1.0.196-linux.run",
    'a2' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/arria-16.1.0.196.qdz",
    'a10_part1' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/arria10_part1-16.1.0.196.qdz",
    'a10_part2' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/arria10_part2-16.1.0.196.qdz",
    'a10_part3' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/arria10_part3-16.1.0.196.qdz",
    'a5' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/arriav-16.1.0.196.qdz",
    'c4' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/cyclone-16.1.0.196.qdz",
    'm2' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/max-16.1.0.196.qdz",
    'm10' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/max10-16.1.0.196.qdz",
    's4' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/stratixiv-16.1.0.196.qdz",
    's5' : "http://download.altera.com/akdlm/software/acdsinst/16.1/196/ib_installers/stratixv-16.1.0.196.qdz"
    
}

quartus_url_171lite = quartus_url_171std
quartus_url_171lite['setup'] = "http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/QuartusLiteSetup-17.1.0.590-linux.run"

quartus_versions = {
    '16.1std' : quartus_url_161std,
    '17.0pro' : quartus_url_170pro,
    '17.0std' : quartus_url_170std,
    '17.1pro' : quartus_url_171pro,
    '17.1std' : quartus_url_171std,
    '17.1lite' : quartus_url_171lite,
    '18.0pro' : quartus_url_180pro,
    '18.0std' : quartus_url_180std
}


import os
import subprocess
import sys
import argparse



def match_wanted_parts(version, devices):
    # work out what devices we have available
    # and filter down to the list we want
    parts = quartus_versions[version].keys()
    parts.remove('setup')
    wanted_parts = []
    for part in parts:
        if part.split("_",1)[0] in devices:
            wanted_parts.append(part)
    return wanted_parts


def download_quartus(version, devices):
    # find which pieces we need to fetch
    parts = match_wanted_parts(version, devices)
    parts.append('setup')
    # convert that to a list of URLs
    urls = {x: quartus_versions[version][x] for x in parts}.values()
    print urls
    command = ['puf', '-c']
    command = command + urls
    process = subprocess.Popen(command, bufsize=1)
    try:
        process.wait()
    except KeyboardInterrupt:
        try:
            process.terminate()
        except OSError:
            pass
    rc = process.wait()
    return rc, urls
#    for line in iter(p.stdout.readline, b''):
#        print line
#    p.stdout.close()
#    p.wait()
#    return p.returncode


def install_quartus(version, installdir):
    setup = quartus_versions[version]['setup']
    leafname = os.path.basename(setup)
    os.chmod(leafname, 0755)
    print(leafname)
    target = os.path.abspath(installdir)
    args = ['--mode', 'unattended', '--unattendedmodeui', 'minimal']
    numeric_version = ''.join(i for i in version if i.isdigit() or i=='.')
    float_version = float(numeric_version)
    if float_version > 17.1:
        args = args + ['--accept_eula', '1']
    process = subprocess.Popen(['./'+leafname] + args + ['--installdir', target])
    rc = process.wait()
    return rc
#            ./$QUARTUS_SCRIPT --mode unattended --unattendedmodeui minimal --installdir $QUARTUS_DIR && \
    


parser = argparse.ArgumentParser(description='Download and install Quartus.')
parser.add_argument('--download-only', action='store_true', help='Only download, don\'t install')
parser.add_argument('--install-only', action='store_true', help='Only install, don\'t download')
parser.add_argument('--prune', action='store_true', help='Delete install files when finished')
parser.add_argument('version', help='Quartus version, eg 18.0pro, 17.1lite, 16.1std')
parser.add_argument('target', help='Directory to install Quartus in')
parser.add_argument('device', nargs='+', help='Device to download/install in Quartus, eg s5 (Stratix 5), a10 (Arria 10), m2 (MAX II), c10gx (Cyclone 10GX)')
args = parser.parse_args(sys.argv[1:])

version = args.version
target = args.target
parts = ['setup'] + match_wanted_parts(version, args.device)
if not args.install_only:
    print("Downloading Quartus %s parts %s\n" % (version, parts))
    rc, urls = download_quartus(version, args.device)
if not args.download_only:
    print("Installing Quartus\n")
    install_quartus(version, target)
if args.prune and not args.install_only:
    for url in urls:
        leafname = url[url.rfind("/")+1:]
        if os.path.exists(leafname):
            os.remove(leafname)
