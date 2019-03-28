#!/usr/bin/python
import time
import os

#a useful comment because ..
with open('/CoolDirectory/thePast','rb') as aim:
    womb = aim.readline()
    aim.seek(-2, os.SEEK_END)
    while aim.read(1) != b"\n":
        aim.seek(-2, os.SEEK_CUR)
    tomb = aim.readline()

action = int(round(time.time()))
strenf = open('/CoolDirectory/thePast', 'a')
strenf.write(str(action) + "\n")
strenf.close()

move = int(action)
stop = int(tomb)

result = move - stop

if result <= 60:
    ext = "seconds"
    ncc = str(result) + " " + str(ext)

if result > 60:
    aah = result / 60
    ooh = result % 60
    exp = "minutes"
    ext = "seconds"
    ncc = str(aah) + " " + str(exp) + " " + str(ooh) + " " + str(ext)

if result > 3599:
    eeh = result / 3600
    iih = result % 3600
    aah = iih / 60
    ooh = iih % 60
    exm = "hours"
    exp = "minutes"
    ext = "seconds"
    ncc = str(eeh) + " " + str(exm) + " " + str(aah) + " " + str(exp) + " " + str(ooh) + " " + str(ext)

erect = str(ncc)
outro = str(erect)

print "you have been busy for " + outro
