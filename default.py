'''
Copyright 2014 Mikel Azkolain

This file is part of script.sysinforeporter.

script.sysinforeporter is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

script.sysinforeporter is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with script.sysinforeporter.  If not, see <http://www.gnu.org/licenses/>.
'''

import xbmc, xbmcgui
import os, sys, platform, struct

def inline_if(condition, if_true, if_false):
    if condition:
        return if_true
    else:
        return if_false

xbmc.log("**** BEGIN script.sysinforeporter DUMP ****")

#XBMC Info
xbmc.log("[XBMC environment related info.]")
xbmc.log("System.BuildVersion: %s" % xbmc.getInfoLabel("System.BuildVersion"))

infolabel_list = [
    "System.Platform.Linux",
    "System.Platform.Linux.RaspberryPi",
    "System.Platform.Windows",
    "System.Platform.OSX",
    "System.Platform.IOS",
    "System.Platform.Darwin",
    "System.Platform.ATV2",
    "System.Platform.Android",
]
for item in infolabel_list:
    value = inline_if(xbmc.getCondVisibility(item), "yes", "no")
    xbmc.log("%s: %s" % (item, value))

#Python version
xbmc.log("[Python environment related info.]")

#os.name
xbmc.log("os.name: %s" % os.name)

#sys.platform
xbmc.log("sys.platform: %s" % sys.platform)

#platform.python_version
xbmc.log("platform.python_version(): %s" % platform.python_version())

#platform.
xbmc.log("platform.uname(): (%s)" % ', '.join(platform.uname()))

#platform.architecture()
xbmc.log("platform.architecture(): (%s)" % ', '.join(platform.architecture()))

#Calculate the size in bits of c_void_p
cvoidp_size = struct.calcsize('P') * 8
xbmc.log("c_void_p size: %s" % cvoidp_size)

xbmc.log("**** END script.sysinforeporter DUMP ****")

d = xbmcgui.Dialog()
d.ok("script.sysinforeporter", "System information dumped successfully.")
