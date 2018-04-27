#!/usr/bin/python
import time
import os
import datetime
ap=open( './review', 'r' )
aq=ap.readline()
ap.close()
x=int(time.time())
g=open( './review', 'w' )
g.write(str(x))
g.write('\n')
g.write(str(x) + '\n')
g.close()
y=open( './review', 'a' )
y.write(str(x) + '\n')
with open('./review', 'rb' ) as f:
    first = f.readline()
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b"\n":
        f.seek(-2, os.SEEK_CUR)
    last = f.readline()
l=str(aq)
k=int(aq)
w=int(last)
v=int(first)
duration = w - k
min = duration / 60
veh = str(min)
print veh + " minutes since the last time you ran this instruction set"
y.close()
flee=1525442400
mega=int(x)
load=flee-mega
lock=load / 60
what=str(lock)
print what + " minutes until the date that has been selected"
