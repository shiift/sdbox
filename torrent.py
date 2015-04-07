#!/usr/bin/python

import sys
import subprocess
import re
import os

if len(sys.argv) == 1 :
    print "Enter the parameter in the format: torrent.py [URL]"
elif len(sys.argv) != 2:
    exit()

url = sys.argv[1]

if "kickass" in url:
    torrentname = re.findall('(?<=\?title\=).*', url)
    torrentname[0] += '.torrent'

    subprocess.call(['wget', '-qNO' + torrentname[0] + '.gz', url, '--no-check-certificate', '--header="Accept-Encoding: gzip"'])
    subprocess.call(['gunzip', '-d', torrentname[0] + '.gz'])
    subprocess.call(['mv', torrentname[0], 'torrents/'])
else:
    torrentname = re.findall('(?<=/)\w+\.torrent', url)

    subprocess.call(['wget', '-qNO' + 'torrents/' + torrentname[0], url])
